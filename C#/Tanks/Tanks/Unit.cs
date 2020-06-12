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
        public float life { get; set; } //Хитпоинты
        private Font font = new Font("Arial", 10, FontStyle.Bold, GraphicsUnit.Point);
        private SolidBrush color = new SolidBrush(Color.Yellow);
        private Pen pen = new Pen(Color.Red, 3);
        private float angle;
        public byte timeShot;

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
        public PointF PositionUnit()
        {
            if (vector == angle)
                position = Position();

            return position;
        }
    }
}
