using System;
using System.Drawing;
using System.Text.RegularExpressions;

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
        private float angle;

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
        public float Vector(float vector, float speed)
        {
            //Угол на цель
            float katetX = target.X - position.X;
            float katetY = target.Y - position.Y;
            angle = (float)(Math.Atan2(katetY, katetX) * 180 / Math.PI + 90);
            if (angle < 0) angle += 360;

            //Текущий угол
            if (Math.Abs(vector - angle) > speed)
            {
                if ((vector < angle && (angle - vector) < 180) ^ ((angle - vector) > -180))
                    vector = (vector - speed+360)%360;
                else
                    vector = (vector + speed)%360;
            }
            else
                vector = angle;

            return vector;
        }

        //Расчет позиции танка
        public PointF Position()
        {
            if (vector == angle)
            {
                position.X += speed * (float)Math.Cos(vector);
                position.Y += speed * (float)Math.Sin(vector);
            }
            return position;
        }
    }
}
