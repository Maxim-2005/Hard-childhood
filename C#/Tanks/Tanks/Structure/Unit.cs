using System;
using System.Drawing;
using System.Windows.Forms;

namespace Tanks
{
    abstract class Unit : AObject
    {
        private static uint ID;

        public uint id = ++ID; //Номер танка
        public Act act; //Действие
        public float life; //Хитпоинты
        public float vision; //Обзор
        private Font font = new Font("Arial", 10, FontStyle.Bold, GraphicsUnit.Point);
        private SolidBrush color = new SolidBrush(Color.Yellow);
        private Pen penR = new Pen(Color.Red, 5);
        private Pen penG = new Pen(Color.Green, 5);
        public float Centre;
        public float angle;
        public byte timeShot;

        //Номер и полоска жизни
        public void DrawInfo(Graphics g)
        {
            if (life <= 0)
                life = 0;
            //Наименование
            g.TranslateTransform(position.X, position.Y);
            g.DrawString(act.ToString(), font, color, -10, -50);
            g.ResetTransform();
            //Жизнь
            g.TranslateTransform(position.X, position.Y);
            g.DrawLine(penG, -30, 30, Centre, 30);
            g.DrawLine(penR, Centre, 30, 30, 30);
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
        public PointF PositionUnit()
        {
            if (vector == angle)
                position = Position();

            return position;
        }
    }
}
