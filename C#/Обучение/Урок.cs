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
            Console.WriteLine(name);
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
        }

        Точка точка = new Точка();


    }
}