#include <iostream>
#include <cmath>

using namespace std;


int main()
{
    setlocale(LC_ALL, "russian");
    {
        double x;
        double y;
        double z;
        double a;
        double b;

        cout << "Введите число Х: ";
        cin >> x;
        cout << "Введите число Y: ";
        cin >> y;
        cout << "Введите число Z: ";
        cin >> z;

        a = ((sqrt(abs(x - 1))) - (pow(abs(y), 1 / 3))) / (1 + (pow(x , 2) / 2) + (pow(y , 2) / 4));
        b = x * (atan(z) + exp(-x-3));

        cout << a << endl;
        cout << b;

        return 0;
    }
}