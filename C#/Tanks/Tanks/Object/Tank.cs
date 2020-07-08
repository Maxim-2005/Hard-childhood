using System.Drawing;

namespace Tanks
{
    class Tank : Unit, IDrawn
    {
        private static Size size = new Size(128, 128);
        private readonly Bitmap bitmap = new Bitmap(Properties.Resources.unnamed);
        private readonly Rectangle body = new Rectangle(new Point(0, 0), size);
        private readonly Rectangle tower = new Rectangle(new Point(128, 0), size);
        private float vectorTower; //Угол поворота башни
        private Pen pen;

        /// <summary>
        /// Конструктор танка
        /// </summary>
        public Tank(Color color)
        {
            this.color = color;
            speed = 1;
            life = 40;
            vision = 512;
            timeShot = 60;
            act = Act.WAIT;
        }

        //Отрисовка танка
        public void DrawUnit(Graphics g)
        {
            vectorTower = Vector(vectorTower, speed*2);

            #region Отрисовка по частям
            //Корпус
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vector);
            g.DrawImage(bitmap, -62, -59, body, GraphicsUnit.Pixel);
            g.ResetTransform();

            //Башня
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vectorTower);
            g.DrawImage(bitmap, -64, -58, tower, GraphicsUnit.Pixel);
            g.ResetTransform();

            //Цвет команды
            pen = new Pen(color, 3);
            g.DrawEllipse(pen, position.X-7, position.Y, 10, 10);

            DrawInfo(g);
            #endregion
        }
    }
}
