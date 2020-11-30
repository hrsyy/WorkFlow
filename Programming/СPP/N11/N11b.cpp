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

        a = ((3 + exp(y - 1))) / (1 + pow(x, 2) * abs(y - tan(z)));
        b = 1 + abs(y - x) + (pow((y - x), 2) / 2) + (pow(abs(y - x), 2) / 3);

        cout << "A = " << a << endl;
        cout << "B = " << b;

        return 0;
    }
}