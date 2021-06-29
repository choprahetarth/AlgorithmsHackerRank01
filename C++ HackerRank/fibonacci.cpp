''' Problem Here - https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking '''
#include <iostream>

using namespace std;

int fibonacci(int n) {
    int fibb;
    if (n==0){
        fibb = 0;
    }
    else if (n==1){
        fibb = 1;
    }
    else if (n>1){
        fibb = fibonacci(n-1)+fibonacci(n-2);
    }
    return fibb;

}

int main() {
    int n;
    cin >> n;
    cout << fibonacci(n);
    return 0;
}