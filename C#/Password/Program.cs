using System;

namespace Password
{
    class Program
    {
        static void Main(string[] args)
        {
            //Переменные
            string password = "1234", _password = "";

            //Проверка пароля
            while (password != _password)
            {
                Console.Write("Введите пароль: ");
                _password = Console.ReadLine();
                if (password != _password) Console.WriteLine("Доступ запрещен");
            }

            //Доступ
            Console.WriteLine("Доступ разрешен");
            Console.ReadKey();
        }
    }
}
