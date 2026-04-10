#include <iostream>

using namespace std;

int global_uninitialized;
int global_initialized = 10;
int *ptr = new int;

int get_sum_till_n(int n)
{
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum += i;
    }
    return sum;
}

int factorial(int n)
{
    if (n < 0)
        return -1;
    else if (n == 0 || n == 1)
        return 1;
    int temp = n * factorial(n - 1);
    cout << "\ntemp memory address is:" << &temp;
    return temp;
}

int main()
{
    cout << "\naddress of global uninitialized variable is: " << &global_uninitialized;
    cout << "\naddress of global initialized variable is: " << &global_initialized;
    cout << "\naddress of heap allocated variable is: " << ptr;
    cout << "\nsum of 10 values is: " << get_sum_till_n(10);
    int fact = factorial(10);
    cout << "\nfactorial of 5 values is: " << fact;
    return 0;
}