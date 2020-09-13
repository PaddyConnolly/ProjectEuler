#include <iostream>

using namespace std;

int main() {

    int result = 0;
    // Sum of Squares
    int s1 = 0;
    for (int i = 1; i <= 100; i++) {
        s1 += (i * i);
    }
    result += s1;

    // Square of sum
    int s2= 0;
    for (int i = 1; i <= 100; i++) {
        s2 += i;
    }

    result -= (s2 * s2);
    
    cout << abs(result) << endl;

}