using System;
using System.Drawing;

namespace Fish.fish
{
    abstract class AFish
    {
        public Bitmap bitmap;
        public PointF position;
        public PointF target;
        public float speed;

        private Random random = new Random();

        //Расчет Позиции
        public PointF Position()
        {
            if (Math.Abs(position.X - target.X) < speed*2 &&
                Math.Abs(position.Y - target.Y) < speed*2)
                Target();
            else
            {
                if (position.X < target.X)
                    position.X += speed;
                else
                    position.X -= speed;

                if (position.Y < target.Y)
                    position.Y += speed;
                else
                    position.Y -= speed;
            }
            return position;
        }

        //Расчет цели
        public PointF Target()
        {
            target.X = random.Next(20, 1000);
            target.Y = random.Next(20, 1000);

            bitmap.RotateFlip(RotateFlipType.RotateNoneFlipNone);
            if (position.X > target.X)
            {
                bitmap.RotateFlip(RotateFlipType.Rotate180FlipY);
            }

            return target;
        }
    }
}
