using System.Drawing;

namespace Tanks
{
    class Car : Unit, IDrawn
    {
        private static Size size = new Size(64, 64);
        private readonly Bitmap bitmap = new Bitmap(Properties.Resources.Машинка);
        private readonly Rectangle body = new Rectangle(new Point(0, 0), size);

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

            DrawInfo(g);
        }
    }
}
