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

        a = (1 + y) * ((x + (y / (pow(x , 2) + 4))) / (exp(-1 * x - 2)) + (1 \ (pow(x , 2) + 4)))
        b = (1 + cos(y - 2)) / ((pow(x , 4) / 2) + (2 * sin(z) * cos(z)))

        cout << "A = " << a << endl;
        cout << "B = " << b;

        return 0;
    }
}
