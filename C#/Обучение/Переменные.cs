using System;

namespace Обучение
{
    class Переменные
    {
        public void Консоль()
        {
            Console.Write("Сравнение 2 больше 3 - ");
            Console.WriteLine(2 < 3);
            Console.WriteLine();

            bool x = 2 > 3;
            Console.WriteLine($"Сравнение 2 больше 3 - {x}\n");

            x = 2 == 3;
            Console.Write($"Сравнение 2 больше 3 - {x}\n");

            int a = 16;
            Console.WriteLine($"Остаток от деления - {a%5}\n");
            Console.WriteLine($"Побитовый сдвиг вниз 16 >> 1 - {a >>= 1}\n");
            Console.WriteLine($"Побитовый сдвиг вверх 16 << 2 - {a <<= 2}\n");
            int b = 100;
            int c = 3;
            //decimal d =(decimal) b / c;
            //decimal d = (double)b / c;
            Console.WriteLine((decimal)b / c);
            Console.WriteLine((double)b / c);

            Console.WriteLine($"Бинарный код 0b100001 - {0b100001}\n");
            Console.WriteLine($"Байт код 0xA1 - {0xA1}\n");
            Console.WriteLine($"Число в степени код 3.2e4 - {3.2e4}\n");
            Console.WriteLine($"Число в -степени код 1.2e-3 - {1.2e-3}\n");
            Console.WriteLine($"Символы юникода \u0420 - {"\u0420"}\n");
            Console.WriteLine($"Символы ASCII \x5A - {"\x5A"}\n");

            DateTime myDr = new DateTime(2005, 10, 11);
            Console.WriteLine($"Мой день рождения: {myDr}\n");
            Console.WriteLine($"День недели рождения: {myDr.DayOfWeek}\n");
            DateTime Today = DateTime.Now;
            Console.WriteLine($"Нынешний день: {Today}\n");
            Console.WriteLine($"Число: {Today.Day}\n");
            Console.WriteLine($"Число: {(Today - myDr).Days}\n");
        }
    }
}
