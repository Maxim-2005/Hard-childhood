using System;

namespace Обучение2
{
    class Условие
    {
        public void Console2()
        {

            bool a = true & true; //И
            bool b = false ^ false; //Либо
            bool x = a | b; // Или
            if (x)
            {
                Console.Write("Условие верно");
            }
            else
            {
                Console.WriteLine("Условие не верно");
            }

            Console.WriteLine($"Сравнение + и + - {true & true}\n");
            Console.WriteLine($"Сравнение + и + - {false & false}\n");
            Console.WriteLine($"Сравнение + и + - {false & true}\n");

            Console.WriteLine($"Сравнение + или + - {true | true}\n");
            Console.WriteLine($"Сравнение + или + - {false | false}\n");
            Console.WriteLine($"Сравнение + или + - {false | true}\n");

            Console.WriteLine($"Сравнение + и + - {true ^ true}\n");
            Console.WriteLine($"Сравнение + и + - {false ^ false}\n");
            Console.WriteLine($"Сравнение + и + - {false ^ true}\n");

            int i = 2147400000;
            bool y = true;
            do
            {
                //y = i < 10;
                Console.WriteLine(i++);
            }
            while (y);
        }
    }
}
