using System;

namespace Обучение
{
    class Урок
    {
        Переменные переменные = new Переменные();

        static void Main(string[] args)
        {
            Урок урок = new Урок();
            урок.ВыводНаКонсоль();
            Console.ReadKey();
        }

        void ВыводНаКонсоль()
        {
            переменные.Консоль();
        }
    }
}
