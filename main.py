from distutils.core import run_setup
from distutils.util import execute
import sys
import json
import secrets
import string
import subprocess

def randomName():
    result = ""
    asciiCode = list(string.ascii_letters)
    for _ in range(10):
        result = result + secrets.choice(asciiCode)
    return result

def executeCommand(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    return process.returncode

def main():

    if(len(sys.argv)<2):
        return
    
    projectName = sys.argv[1]

    command = "rm -rf ./" + projectName + "/results"
    executeCommand(command)
    command = "mkdir ./" + projectName + "/results"
    executeCommand(command)

    

    randName = randomName()
    print(randName)

    # Recuperare il file, modificarlo e gestire situazioni
    # Compilare e gestire situazioni
    # Eseguire gli altri scrpit e gestire situazioni
    

if __name__ == "__main__":
    main()

