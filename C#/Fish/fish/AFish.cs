using System;
using System.Drawing;

namespace Fish.fish
{
    abstract class AFish
    {
        public PointF position = new PointF();
        public PointF target;
        private byte time = 0;
        public float speed;
        private byte x = 2;

        private float vector;
        private Random random = new Random();

        //Расчет Позиции
        public PointF Position(Bitmap bitmap)
        {
            if (time == 60)
                time = 0;
            if (target.X > position.X)
            {
                if (x == 1 && time == 0)
                {
                    bitmap.RotateFlip(RotateFlipType.RotateNoneFlipX);
                    x = 2;
                }
                position.X++;
            }
            else
            {
                if (x == 2 && time == 0)
                {
                    bitmap.RotateFlip(RotateFlipType.Rotate180FlipY);
                    x = 1;
                }
                position.X--;
            }

            if (target.Y > position.Y)
                position.Y++;
            else
                position.Y--;

            time++;
            return position;
        }


        //Расчет цели
        public PointF Target()
        {
            if (position == target)
            {
                target.X = random.Next(20, 1000);
                target.Y = random.Next(20, 1000);
            }
            return target;
        }
    }
}
