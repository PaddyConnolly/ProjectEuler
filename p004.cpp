#include <iostream>

using namespace std;

int makePalindrome(int n);

int main() {

    for (int i = 999; i >= 100; i--) {
        int palindrome = makePalindrome(i);

        for (int i = 999; i * i >= palindrome; i--) {
            if (palindrome % i == 0) {
                auto other = palindrome / i;
                if (100 <= other <= 999) {
                    cout << palindrome << endl;
                    return 0;
                }
            }
        }
    }

}

int makePalindrome(int n) {
    int result = n * 1000;  // 123 -> 123000
    result += n / 100;  // 123000 -> 123001
    result += n / 10 % 10 * 10; // 123001 -> 123021
    result += n % 10 * 100;  // 123021 -> 123321 
    return result;
}