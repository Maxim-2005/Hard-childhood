using System.Drawing;

namespace Tanks
{
    abstract class AObject
    {
        public PointF position; //Позиция на карте
        public PointF target; //Цель танка
        public float speed; //Скорость танка
    }
}
