'''solution to: https://www.hackerrank.com/challenges/30-review-loop/problem '''
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n; 
    string s,m;
    std::cin>>n;
    //std::cout<<n<<s<<m;

    for (int k=0; k<n;k++){
        std::cin>>s;
    for (int i=0; i<s.size();i=i+2){
        std::cout<<s[i];
    }
    std::cout<< " ";
    for (int j=1; j<s.size(); j=j+2)  {
        std::cout<<s[j];
    }
    std::cout<<endl;
    }
      
    
    return 0;

}
