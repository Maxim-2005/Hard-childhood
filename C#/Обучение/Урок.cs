using System;
using Обучение2;
using Целое = System.Int32;
using Дробь = System.Double;
using Строка = System.String;
using КвадратМаксима = System.Console;

namespace Обучение
{
    struct Точка
    {
        public int X;
        public int Y;
        public string name;
        public void vivod()
        {
            Console.WriteLine(name + " " + X + " " + Y);
        }
    }

    class Урок
    {
        Переменные переменные = new Переменные();
        Условие условие = new Условие();
        Тд тд = new Тд();

        static void Main(string[] args)   
        {                                 
            Урок урок = new Урок();       
            урок.ВыводНаКонсоль();        
            Console.ReadKey();            
        }                                 
        
        unsafe
        void ВыводНаКонсоль()
        {                                 
            //переменные.Консоль();       
            //условие.Console2();         
            //тд.Данные();                
            //тд.Структуры();             
            Целое дурак = 5;              
            Дробь дебил = 0.3;
            Строка iks = "Дережабль";
            КвадратМаксима.WriteLine(дурак + " " + дебил + " " + iks);

            //Объект структуры
            Точка тчк = new Точка();
            тчк.X = 1_234_567;
            тчк.Y = 987_654_321;
            тчк.name ="Maxim";
            тчк.vivod();

            //Указатели
            int k = 125;
            int* Указатель = &k;
            Console.WriteLine("Регистор памяти: " + (long) Указатель);

            //Динамический тип данных
            dynamic D = 1;
            Console.WriteLine(D);

            D = "Maxim";
            Console.WriteLine(D);

            //Округление
            Console.WriteLine(Math.Round(Math.PI, 15));
            Console.WriteLine(Math.Abs(-123));
            Console.WriteLine(Math.Pow(3, 3));
            Console.WriteLine(Math.Sqrt(16));
            Console.WriteLine(Math.Min(16, 35));
            Console.WriteLine(Math.Max(16, 35));
            Console.WriteLine(Math.Sin(90));
            Console.WriteLine(Math.Cos(90));

            //

            //

            //
        }
    }
}