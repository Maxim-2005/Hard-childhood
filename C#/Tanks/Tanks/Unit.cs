using System;
using System.Drawing;

namespace Tanks
{
    abstract class Unit
    {
        private static uint ID;

        public uint id = ++ID; //Номер танка
        public PointF position; //Позиция на карте
        public PointF target; //Цель танка
        public float vector; //Угол повората корпуса
        public float speed = 1; //Скорость танка
        private Font font = new Font("Arial", 10, FontStyle.Bold, GraphicsUnit.Point);
        private SolidBrush color = new SolidBrush(Color.Yellow);
        private Pen pen = new Pen(Color.Red, 3);

        //Номер и полоска жизни
        public void DrawInfo(Graphics g)
        {
            //Наименование
            g.TranslateTransform(position.X, position.Y);
            g.DrawString(id.ToString(), font, color, -10, -50);
            g.ResetTransform();
            //Жизнь
            g.TranslateTransform(position.X, position.Y);
            g.DrawLine(pen, -30, -30,  30, -30);
            g.ResetTransform();
        }

        //Расчет поворота танка
        public float Vector()
        {
            float katetX = target.X - position.X;
            float katetY = target.Y - position.Y;
            vector = (float)(Math.Atan2(katetY, katetX) * 180 / Math.PI + 90);

            return vector;
        }

        //Расчет позиции танка
        public PointF Position()
        {
            position.X += speed * (float)Math.Cos(vector);
            position.Y += speed * (float)Math.Sin(vector);
            return position;
        }
    }
}
