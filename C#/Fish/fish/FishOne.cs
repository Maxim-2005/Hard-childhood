using Fish.fish;
using System.Drawing;

namespace Fish
{
    class FishOne : AFish, IFish
    {
        public FishOne()
        {
            bitmap = new Bitmap(Properties.Resources.latest);
            speed = 0.7f;
        }

        //Отрисовка рыбки
        public void DrawFish(Graphics g)
        {
            g.DrawImage(bitmap, position);
        }
    }
}
