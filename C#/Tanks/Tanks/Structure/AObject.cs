using System;
using System.Drawing;

namespace Tanks
{
    abstract class AObject
    {
        public Color color; //Цвет команды
        public PointF position; //Позиция на карте
        public PointF target; //Цель
        public float vector; //Угол повората
        public float speed; //Скорость

        //Расчет позиции
        public PointF Position()
        {
            position.X += speed * (float)Math.Cos(vector);
            position.Y += speed * (float)Math.Sin(vector);

            return position;
        }

        ///<summary>
        ///Расчет расстояния между точками (float)
        ///<summary>
        public float Delta(PointF point1, PointF point2)
        {
            float CathetX = point1.X - point2.X;
            float CathetY = point1.Y - point2.Y;

            return (float)Math.Sqrt(CathetX * CathetX + CathetY * CathetY);
        }
    }
}
