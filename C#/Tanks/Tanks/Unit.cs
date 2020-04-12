using System;
using System.Drawing;

namespace Tanks
{
    abstract class Unit
    {
        public int id; //Номер танка
        public PointF position; //Позиция на карте
        public PointF target; //Цель танка
        public float vector; //Угол повората корпуса
        public float speed = 1; //Скорость танка

        //Расчет поворота танка
        public float Vector()
        {
            float katetX = target.X - position.X;
            float katetY = target.Y - position.Y;
            vector = (float)(Math.Atan2(katetY, katetX) * 180 / Math.PI + 90);

            return vector;
        }

        //Расчет позиции танка
        public PointF Position()
        {
            position.X += speed * (float)Math.Cos(vector);
            position.Y += speed * (float)Math.Sin(vector);
            return position;
        }
    }
}
