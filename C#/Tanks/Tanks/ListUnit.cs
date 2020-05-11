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

        //Создание списка танков
        public List<object> CreateListUnit(Color color, int x)
        {
            for (byte i = 1; i <= count; i++)
            {
                listUnits.Add(new Tank
                {
                    color = color,
                    position = StartPosition(x),
                    speed = 1
                });

                listUnits.Add(new Car
                {
                    color = color,
                    position = StartPosition(x),
                    speed = 2
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
                listShot.NewShot(unit);
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