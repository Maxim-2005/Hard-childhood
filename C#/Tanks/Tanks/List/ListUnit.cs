using System;
using System.Collections.Generic;
using System.Drawing;
using System.Security.Principal;

namespace Tanks
{
    class ListUnit
    {
        public byte count = 1;

        private Size window = FormTanks.window;
        public List<object> listUnits = new List<object>();
        private Random random = new Random();

        /// <summary>Команда: Пусто</summary>
        public ListUnit()
        {
            Color color = Color.FromArgb(255, Color.FromArgb(random.Next(0xFFFFFF+1)));
            CreateListUnit(color, new Point(50, 50), count, count);
        }

        /// <summary>Команда: Цвет и позиция</summary>
        public ListUnit(Color color, Point start)
        {
            CreateListUnit(color, start, count, count);
        }

        /// <summary>Цвет: ... Позиция: ... Танки: ... Машинки: ... </summary>
        public ListUnit(Color color, Point start, byte tank, byte car)
        {
            CreateListUnit(color, start, tank, car);
        }

        /// <summary> Команда: Цвет и Позиция и Число юнитов <summary> \\\
        public ListUnit(Color color, Point start, byte unit)
        {
            CreateListUnit(color, start, unit, unit);
        }

        /// <summary>Позиция танков и машинок : Пусто/summary>
        public ListUnit(Point start, byte tank, byte car)
        {
            Color color = Color.FromArgb(255, Color.FromArgb(random.Next(0xFFFFFF + 1)));
            CreateListUnit(color, start, tank, car);
        }

        //Создание списка танков
        public List<object> CreateListUnit(Color color, Point start, byte  tank, byte  car)
        {
            for (byte i = 1; i <= tank; i++)
                NewUnit(new Tank(color), start);

            for (byte i = 1; i <= car; i++)
                NewUnit(new Car(color), start);

            return listUnits;
        }

        //Добавляем юнита в список
        private void NewUnit(dynamic unit, Point start)
        {
            listUnits.Add(unit);
            unit.position = StartPosition(start);
        }

        //Отрисовка списка танков
        public void DrawListUnit(Graphics g, Point cursor, ListShot listShot)
        {
            foreach (dynamic unit in listUnits)
            {
                unit.DrawUnit(g, cursor);

                unit.timeShot++;
                if (unit.timeShot > 60)
                {
                    listShot.NewShot(unit);
                    unit.timeShot = 0;
                }
            }
        }

        //Стартовая позиция
        public Point StartPosition(Point start)
        {
        
            Point position = new Point();
            position.X = window.Width * start.X / 100 + random.Next(-200, 200);
            position.Y = window.Height * start.Y / 100 + random.Next(-200, 200);

            return position;
        }
    }
}