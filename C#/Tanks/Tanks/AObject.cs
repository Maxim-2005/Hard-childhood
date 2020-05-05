using System.Drawing;

namespace Tanks
{
    abstract class AObject
    {
        public PointF position; //Позиция на карте
        public PointF target; //Цель
        public float vector; //Угол повората
        public float speed; //Скорость
    }
}
