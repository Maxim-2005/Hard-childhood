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
        int id; //Номер танка
        Point position; //Позиция на карте
        Point target; //Цель танка
        float vector; //Угол повората корпуса
        float vectorTower; //Угол поворота башни
        Random random = new Random();

        //Отрисовка танка
        public void DrawTank(Graphics g)
        {
            position = Position();
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
        private Point Position()
        {
            position.X = random.Next(1280);
            position.Y = random.Next(720);
            return position;
        }
    }
}
