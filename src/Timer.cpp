#include "Timer.h"

Timer::Timer(std::string s){
    stopped = false;
    this->outputName = s;
    this->m_startTimePoint = std::chrono::high_resolution_clock::now();
}

void Timer::stop(){
    std::chrono::time_point<std::chrono::high_resolution_clock> endTimePoint = std::chrono::high_resolution_clock::now();

    long start        = std::chrono::time_point_cast<std::chrono::microseconds>(m_startTimePoint).time_since_epoch().count();
    long end          = std::chrono::time_point_cast<std::chrono::microseconds>(endTimePoint).time_since_epoch().count();

    long duration = end - start;
    std::cout << "\n" << this->outputName << " : " << duration << "\n";
    stopped = true;
}

    
Timer::~Timer(){
    if(!stopped) stop();
}
