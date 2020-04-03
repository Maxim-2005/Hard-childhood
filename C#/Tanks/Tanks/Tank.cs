using System;
using System.Drawing;

namespace Tanks
{
    class Tank
    {
        public int id; //Номер танка
        public PointF position; //Позиция на карте

        private Bitmap bitmap = new Bitmap(Properties.Resources.unnamed);
        private Rectangle body = new Rectangle(new Point(0, 0), new Size(128, 128));
        private Rectangle tower = new Rectangle(new Point(128, 0), new Size(128, 128));
        private PointF target; //Цель танка
        private float vector; //Угол повората корпуса
        private float vectorTower; //Угол поворота башни
        private float speed = 1; //Скорость танка

        //Отрисовка танка
        public void DrawTank(Graphics g, Point cursor)
        {
            target = cursor;
            Position();
            Vector();
            vectorTower = vector+15;

            //Корпус
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vector);
            g.DrawImage(bitmap, -63, -78, body, GraphicsUnit.Pixel);
            g.ResetTransform();

            //Башня
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vectorTower);
            g.DrawImage(bitmap, -68, -76, tower, GraphicsUnit.Pixel);
            g.ResetTransform();
        }

    //Расчет поворота танка
    private float Vector()
        {
            float katetX = target.X - position.X;
            float katetY = target.Y - position.Y;
            vector = (float)(Math.Atan2(katetY, katetX) * 180 / Math.PI + 90);
            
            return vector;
        }

    //Расчет позиции танка
    private PointF Position()
        {
            position.X += speed*(float)Math.Cos(vector);
            position.Y += speed*(float)Math.Sin(vector);
            return position;
        }
    }
}
