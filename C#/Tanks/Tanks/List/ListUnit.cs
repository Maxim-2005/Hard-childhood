using System;
using System.Collections.Generic;
using System.Drawing;
using System.Security.Principal;

namespace Tanks
{
    class ListUnit
    {
        public byte count = 10;

        private Size window = FormTanks.window;
        private List<object> listUnits = new List<object>();
        private Random random = new Random();

        /// <summary>
        /// Команда
        /// </summary>
        public ListUnit(Color color, int x)
        {
            CreateListUnit(color, x);
        }
        
        //Создание списка танков
        public List<object> CreateListUnit(Color color, int x)
        {
            for (byte i = 1; i <= count; i++)
            {
                listUnits.Add(new Tank
                {
                    color = color,
                    position = StartPosition(x)
                });

                listUnits.Add(new Car
                {
                    color = color,
                    position = StartPosition(x)
                });
            }

            return listUnits;
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
        public Point StartPosition(int x)
        {
            
            Point position = new Point();
            position.X = window.Width * x / 100 + random.Next(-200, 200);
            position.Y = random.Next(50, window.Height-50);
            return position;
        }
    }
}