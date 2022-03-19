#include <iostream>
#include <cstdlib>
#include "sort.h"

inline int randomGenerator(int max){
    return (rand() % max);
}

int main(){
    const int N = 2048;
    int vect[N];
    
    for(auto& elem : vect)
        elem = randomGenerator(N);

    //START_BENCHMARK
    sort(vect, N);
    //STOP_BENCHMARK

    for(auto& elem : vect){
        std::cout << elem << std::endl;
    } 

}