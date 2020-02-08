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
        }
    }
}
