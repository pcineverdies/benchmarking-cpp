#include <chrono>
#include <iostream>
#include <cstring>

class Timer{
private:
    std::chrono::time_point<std::chrono::high_resolution_clock> m_startTimePoint;
    std::string outputName;
    bool stopped;

public:
    Timer(std::string s);

    void stop();
    
    ~Timer();
};