using System.Drawing;

namespace Tanks
{
    class Shot : AObject
    {
        Pen pen;

        //Отрисовка пульки
        public void DrawShot(Graphics g, Point cursor)
        {
            target = cursor;
            pen = new Pen(Color.DarkOrange, 3);
            g.DrawLine(pen, position, target);
        }
    }
}
