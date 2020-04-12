using System;
using System.Collections.Generic;
using System.Drawing;

namespace Tanks
{
    class ListTanks : List<Tank>
    {
        public byte count = 10;

        private List<Tank> listTanks = new List<Tank>();
        private List<Car> listCar = new List<Car>();
        private Random random = new Random();

        //Создание списка танков
        public List<Tank> CreateListTanks()
        {
            for (byte i = 1; i <= count; i++)
            {
                listTanks.Add(new Tank
                {
                    id = i,
                    position = StartPosition(),
                    speed = 1
                });
            }
            return listTanks;
        }

        //Создание списка машин
        public List<Car> CreateListCar()
        {
            for (byte i = 1; i <= count; i++)
            {
                listCar.Add(new Car
                {
                    id = i,
                    position = StartPosition(),
                    speed = 3
                });
            }
            return listCar;
        }

        //Стартовая позиция
        public Point StartPosition()
        {
            Point position = new Point();
            position.X = random.Next(1280);
            position.Y = random.Next(720);
            return position;
        }

        //Отрисовка списка танков
        public void DrawListTank(Graphics g, Point cursor)
        {
            foreach (Tank tank in listTanks)
            {
                tank.DrawTank(g, cursor);
            }
        }

        //Отрисовка списка машин
        public void DrawListCar(Graphics g, Point cursor)
        {
            foreach (Car car in listCar)
            {
                car.DrawCar(g, cursor);
            }
        }
    }
}