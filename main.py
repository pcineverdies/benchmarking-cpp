#!/usr/bin/env python3

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

def openJSON(pathName):
    with open(pathName) as json_file:
        data = json.load(json_file)
        return data

def changeSourceFile(folder, fileName):
    randName = randomName()
    
    startTimer = "Timer " + randName + "(\"" + randName + "\");"
    stopTimer  = randName + ".stop();"
    outputFile = randName + ".cpp"

    with open(folder + outputFile, 'a') as output: 
        output.write("#include \"../src/Timer.h\"\n")
        sourceFile = fileinput.input(folder + fileName, inplace=False)
        for line in sourceFile: 
            if line.find("//+timer") != -1:
                output.write(line.rstrip().replace('//+timer', startTimer)+"\n")
            elif line.find("//-timer") != -1:
                output.write(line.rstrip().replace('//-timer', stopTimer)+"\n")
            else:
                output.write(line.rstrip()+"\n")

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

def runBenchmarking(NumberIterations, folder, outputName):
    with open(folder + "results/data.txt", 'a') as dataFile: 
        for _ in range(NumberIterations):
            process = subprocess.Popen("./"+outputName,  shell=True, cwd = folder, stdout=subprocess.PIPE)
            process.wait()
            output = process.stdout.read().decode("ascii").split()
            dataFile.write(output[output.index(outputName)+2] + "\n")


def main():

    if(len(sys.argv)<2):
        return
    
    projectName = sys.argv[1]
    folder = "./" + projectName + "/"

    jsonPath = folder + "config.json"
    config = openJSON(jsonPath)

    sourceFile = config["SourceFile"]

    command = "rm -rf results"
    executeCommand(command, folder)
    command = "mkdir results"
    executeCommand(command, folder)

    outputName = changeSourceFile(folder, sourceFile)

    compilerCommand = changeCompilerCommand(config["CompilerCommand"], sourceFile, outputName)

    executeCommand(compilerCommand, folder)

    runBenchmarking(config["NumberIterations"], folder, outputName)

    analyzer.analyzeData(folder + "results/data.txt")
    plot.plot(config["ProjectName"], folder)

    command = "rm -rf " + outputName + ".cpp " + outputName
    executeCommand(command, folder)


if __name__ == "__main__":
    main()

