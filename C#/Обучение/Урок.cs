using System;
using Обучение2;

namespace Обучение
{
    class Урок
    {
        Переменные переменные = new Переменные();
        Условие условие = new Условие();

        static void Main(string[] args)
        {
            Урок урок = new Урок();
            урок.ВыводНаКонсоль();
            Console.ReadKey();
        }

        void ВыводНаКонсоль()
        {
            //переменные.Консоль();
            условие.Console2();
        }
    }
}
