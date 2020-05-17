using System;
using System.Drawing;

namespace Tanks
{
    class Shot : AObject
    {
        private PointF position0;
        private Pen pen;

        /// <summary>
        /// Конструктор снаряда
        /// </summary>
        public Shot()
        {
            speed = 16;
        }

        //Отрисовка пульки
        public void DrawShot(Graphics g)
        {
            position0 = position;
            position = Position();
            pen = new Pen(color, 3);
            g.DrawLine(pen, position, position0);
        }
    }
}
