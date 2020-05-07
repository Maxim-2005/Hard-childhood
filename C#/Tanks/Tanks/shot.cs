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
            vector = Vector();
            position0 = position;
            position = Position();
            pen = new Pen(Color.DarkOrange, 3);
            g.DrawLine(pen, position, position0);
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
