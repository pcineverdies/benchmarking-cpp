# benchmarking-cpp

Light benchmarking environment, so you can test the speed of snippets of C++ code.

## Background
During my bachelor's thesis, I needed to test the speed of some C++ functions; the final goal was to proove that using the AVX-512 Intel's extension you could get some performance advantages. 

Since I had some decent scripts to analyze execution time of little snippets, I put all together in this project.


## What does it do

In your C++ code you specify a starting point and a stop point for the measure of time (for instance, immediately before and after the call of a function).

The scripts executes your code _N_ times, it measuers time in milliseconds and then calculates the mean, stdev and median of the values so obtained.  

Using the values it draws a lollipop chart about the distribution of execution time.

## How to use it

1.  Download the project;
2.  Create a folder inside it (we will call it `myFolder`) where you will put everything you need to run your C++ code;
3.  To identify the fragment of code you want to test, wrap it inside the lines

    ```c++
    //+timer
    ...
    //-timer
    ```

    If you want to measure the execution time of the function `sort(int*,int)`, you can write

    ```c++
    //+timer
    sort(array,N);
    //-timer
    ```

    **!!!** Make sure the comments are written as above, or the script will raise an error. The two comments need to be in order and in the same file! 


3. Create a file inside `myFolder/` called `config.json` having the following format:

    ```json
    {
        "ProjectName" : "myProject",
        "SourceFile"  : "myfile.cpp",
        "CompilerCommand" : "g++ -o ex myFile.cpp",
        "NumberIterations" : 2048,
        "Timeout" : 3600
    }
    ```
- `ProjectName` is the name of your project;
- `SourceFile` is the name of the file where you inserted the comments as shown in 3.;  
- `CompilerCommand` is the command you would write in terminal to compile it;
- `Timeout` is the maximum time you want to wait before stop an execution (and the whole benchmarking). You should decided it based on the complexity of your code and the possibility of having endless loops. 

5. Run the benchmark using the command

    ```bash
    python3 main.py myFolder
    ```

    where the argument is the name of the folder you created.

At the end of the execution, if nothing went wrong, you will have on the screen the result of the computation; the script will create the folder `myFolder/results/` where you can find the chart, the file containing all the measures (if you want to elaborate it more than it does) and the same recap about mean, stdev and median inside a `.txt` file. 

## What is still missing

Tons of things:
    
- Options to modify the chart inside the `config.json` file;
- Display of the state of the benchmark (for instance, the number of remaining tests it needs to execute);
- ???
