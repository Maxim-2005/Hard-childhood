using System;
using System.Drawing;

namespace Tanks
{
    class Tank
    {
        Bitmap bitmap = new Bitmap(Properties.Resources.unnamed);
        Rectangle body = new Rectangle(new Point(0, 0), new Size(128, 128));
        Rectangle tower = new Rectangle(new Point(128, 0), new Size(128, 128));

        //Танк
        public int id; //Номер танка
        public Point position; //Позиция на карте
        public Point target; //Цель танка
        public float vector; //Угол повората корпуса
        public float vectorTower; //Угол поворота башни
        public Random random = new Random();

        //Отрисовка танка
        public void DrawTank(Graphics g)
        {
            //Корпус
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vector);
            g.DrawImage(bitmap, -63, -78, body, GraphicsUnit.Pixel);
            g.ResetTransform();

            //Башня
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(vectorTower);
            g.DrawImage(bitmap, -64, -60, tower, GraphicsUnit.Pixel);
            g.ResetTransform();
        }

        //Расчет позиции танка
        public Point Position()
        {
            position.X = random.Next(1280);
            position.Y = random.Next(720);
            return position;
        }
    }
}
