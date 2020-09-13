#include <iostream>
#include <math.h>

using namespace std;

bool isPrime(int n);

int main()  {
    
    int count = 0;
    int prime = 1;

    while (count < 10001) {
        prime ++;
        if (isPrime(prime)) {
            count ++;
        }
    }

    cout << prime << endl; 

}


bool isPrime(int n) {
    if (n <= 1) {
        return false;
    } else if (n <= 3) {
        return true;
    } else if (n % 2 == 0) {
        return false;
    } else {
        for (int i = 3; i <= sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}