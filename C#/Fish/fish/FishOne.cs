using Fish.fish;
using System.Drawing;

namespace Fish
{
    class FishOne : AFish, IFish
    {
        private readonly Bitmap bitmap = new Bitmap(Properties.Resources.latest);

        public FishOne()
        {
            speed = 1;
        }

        //Отрисовка рыбки
        public void DrawFish(Graphics g)
        {
            Position(bitmap);
            g.DrawImage(bitmap, position);
        }
    }
}
