using System.Drawing;

namespace Tanks
{
    class Car : Unit, IDrawn
    {
        private static Size size = new Size(64, 64);
        private readonly Bitmap bitmap = new Bitmap(Properties.Resources.Машинка);
        private readonly Rectangle body = new Rectangle(new Point(0, 0), size);
        Pen pen;

        /// <summary>
        /// Конструктор машинки
        /// </summary>
        public Car(Color color)
        {
            this.color = color;
            speed = 2;
            life = 10;
            vision = 1024;
            act = Act.WAIT;
        }

        //Отрисовка машинки
        public void DrawUnit(Graphics g)
        {
                        
            //Машинка
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vector);
            g.DrawImage(bitmap, -30, -27, body, GraphicsUnit.Pixel);
            g.ResetTransform();

            //Цвет команды
            pen = new Pen(color, 3);
            g.DrawEllipse(pen, position.X - 7, position.Y, 10, 10);

            DrawInfo(g);
        }
    }
}
