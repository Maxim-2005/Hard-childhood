using System.Drawing;

namespace Tanks
{
    class Car : Unit
    {
        private Bitmap bitmap = new Bitmap(Properties.Resources.Машинка);
        private Rectangle body = new Rectangle(new Point(0, 0), new Size(64, 64));

        //Отрисовка машинки
        public void DrawUnit(Graphics g, Point cursor)
        {
            target = cursor;
            Position();
            Vector();

            //Машинка
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vector);
            g.DrawImage(bitmap, -30, -27, body, GraphicsUnit.Pixel);
            g.ResetTransform();
        }
    }
}
