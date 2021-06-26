'''
The link of the problem  - https://www.hackerrank.com/challenges/c-tutorial-basic-data-types/problem
'''
#include <iostream>
#include <cstdio>
#include <iomanip>

int main() {
    int a;
    long b;
    char c;
    float d;
    double e; 
    std::cin>>a>>b>>c>>d>>e;
    std::cout<<a<<"\n"<<b<<"\n"<<c<<"\n";
    std::cout<<std::fixed<<std::setprecision(3)<<d<<"\n";
    std::cout<<std::fixed<<std::setprecision(9)<<e;
    return 0;
}
