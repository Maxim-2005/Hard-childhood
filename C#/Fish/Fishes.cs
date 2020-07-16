using System;
using System.Collections.Generic;
using System.Drawing;

namespace Fish
{
    class Fishes
    {
        private Random random = new Random();
        public List<object> ListFish = new List<object>();

        public Fishes()
        {
            for (byte i = 0; i < 5; i++)
            {
                NewFish(new FishOne());
                NewFish(new FishTwo());
                NewFish(new FishThree());
            }
        }

        private void NewFish(dynamic fish)
        {
            ListFish.Add(fish);
            fish.position = Position();
            fish.target = Position();
        }

        //Расчет позиции
        public PointF Position()
        {
            PointF position = new PointF();
            position.X = random.Next(20, 1900);
            position.Y = random.Next(20, 1060);
            return position;
        }

        public void DrawListFish(Graphics g)
        {
            foreach (dynamic fish in ListFish)
            {
                //fish.Position();
                fish.Target();
                fish.DrawFish(g);
            }
        }
    }
}
