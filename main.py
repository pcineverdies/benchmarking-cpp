#!/usr/bin/env python3

from subprocess import TimeoutExpired
import sys
sys.path.append("./src/")

from utils import * 

def randomName():
    result = ""
    asciiCode = list(string.ascii_letters)
    for _ in range(10):
        result = result + secrets.choice(asciiCode)
    return result

def executeCommand(command, cwdA=None):
    if cwdA != None:
        process = subprocess.Popen(command, cwd = cwdA, shell=True,  stdout=subprocess.PIPE)
    else:        
        process = subprocess.Popen(command,  shell=True, stdout=subprocess.PIPE)
    process.wait()
    return process.returncode

def deleteTempFiles(folder, fileName,resultsToo = True):
    command = "rm -rf " + fileName + ".cpp " + fileName
    executeCommand(command, folder)
    if resultsToo:
        command = "rm -rf results"
        executeCommand(command, folder)


def openJSON(pathName):
    try:
        with open(pathName) as json_file:
            data = json.load(json_file)
            return data
    except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
        print("Can't open config file!")
        print("Make sure you choose the correct folder!")
        exit()


def changeSourceFile(folder, fileName):
    randName = randomName()
    
    startTimer = "Timer " + randName + "(\"" + randName + "\");"
    stopTimer  = randName + ".stop();"
    foundStart = False
    foundStop  = False
    outputFile = randName + ".cpp"

    try:
        with open(folder + outputFile, 'a') as output: 
            output.write("#include \"../src/Timer.h\"\n")
            sourceFile = fileinput.input(folder + fileName, inplace=False)
            for line in sourceFile: 
                if line.find("//+timer") != -1 and not foundStart:
                    output.write(line.rstrip().replace('//+timer', startTimer)+"\n")
                    foundStart = True
                elif line.find("//+timer") != -1 and foundStart:
                    raise ValueError
                elif line.find("//-timer") != -1 and foundStart and not foundStop:
                    output.write(line.rstrip().replace('//-timer', stopTimer)+"\n")
                    foundStop = True
                elif line.find("//-timer") != -1 and not foundStart:
                    raise ValueError
                elif line.find("//-timer") != -1 and foundStop:
                    raise ValueError
                else:
                    output.write(line.rstrip()+"\n")
            
            if not foundStart or not foundStop:
                raise ValueError

    except ValueError:
        print("The source file is not well formatted")
        deleteTempFiles(folder, randName)
        exit()      

    except:
        print("Could not elaborate the source file!")
        print("Make sure the file exists!")
        deleteTempFiles(folder, randName)
        exit()


    return randName

def changeCompilerCommand(compilerCommand, sourceFile, outputName):
    compilerCommand = compilerCommand.replace(sourceFile, outputName + ".cpp")
    compilerCommand += " ./../src/Timer.cpp"

    if not "-o" in compilerCommand:
        compilerCommand = compilerCommand + " -o " + outputName
        return compilerCommand

    compilerCommand = compilerCommand.split()

    compilerCommand.remove(compilerCommand[compilerCommand.index('-o')+1])
    compilerCommand.insert((compilerCommand.index('-o')+1), outputName)
    compilerCommand = ' '.join(compilerCommand)

    return compilerCommand

def runBenchmarking(NumberIterations, folder, outputName, timeoutInput):
    try:
        with open(folder + "results/data.txt", 'a') as dataFile: 
            for _ in range(NumberIterations):
                process = subprocess.Popen("./"+outputName,  shell=True, cwd = folder, stdout=subprocess.PIPE)
                process.wait(timeout=timeoutInput)
                if process.returncode != 0:
                    raise Exception

                output = process.stdout.read().decode("ascii").split()
                time = output[output.index(outputName)+2]
                dataFile.write(time + "\n")

    except TimeoutExpired:
        print("An execution did not terminated within the timeout!")
        deleteTempFiles(folder, outputName)
        exit()        

    except:
        print("Something went wrong during the benchmarking")
        deleteTempFiles(folder, outputName)
        exit()

def main():

    if(len(sys.argv)<2):
        print("No folder name as argument!")
        return
    
    projectName = sys.argv[1]
    folder = "./" + projectName + "/"

    jsonPath = folder + "config.json"
    config = openJSON(jsonPath)

    neededKeys = [ "ProjectName","SourceFile","CompilerCommand","NumberIterations", "Timeout"]
    if (neededKeys - config.keys()):
        print("Config file is not correct. Please check you inserted the right keys!")
        exit()

    sourceFile = config["SourceFile"]

    command = "rm -rf results"
    if executeCommand(command, folder)!=0:
        print("Could not delete results folder!")
        exit()
    command = "mkdir results"
    if executeCommand(command, folder)!=0:
        print("Could not create results folder!")
        exit()

    outputName = changeSourceFile(folder, sourceFile)

    compilerCommand = changeCompilerCommand(config["CompilerCommand"], sourceFile, outputName)

    if executeCommand(compilerCommand, folder)!=0:
        print("Something went wrong during the compiling of code.")
        print("Make sure you wrote the command correctly")
        deleteTempFiles(folder, outputName)
        exit()
        
    runBenchmarking(int(config["NumberIterations"]), folder, outputName, config["Timeout"])

    analyzer.analyzeData(folder + "results/data.txt")
    plot.plot(config["ProjectName"], folder)

    deleteTempFiles(folder, outputName, resultsToo = False)


if __name__ == "__main__":
    main()

