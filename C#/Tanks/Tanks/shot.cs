using System;
using System.Drawing;

namespace Tanks
{
    class Shot : AObject
    {
        private PointF position0;
        Pen pen;

        //Отрисовка пульки
        public void DrawShot(Graphics g)
        {
            position = Position();
            pen = new Pen(Color.DarkOrange, 3);
            g.DrawLine(pen, position, position0);
        }

        //Расчет позиции пульки
        public PointF Position()
        {
            vector = Vector();
            position0 = position;
            position.X += speed * (float)Math.Cos(vector);
            position.Y += speed * (float)Math.Sin(vector);

            return position;
        }

        //Угол на цель
        private float Vector()
        {
            float katetX = target.X - position.X;
            float katetY = target.Y - position.Y;
            vector = (float)(Math.Atan2(katetY, katetX) * 180 / Math.PI + 90);
            if (vector < 0) vector += 360;

            return vector;
        }
    }
}
