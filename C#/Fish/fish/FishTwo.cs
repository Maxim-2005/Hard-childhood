using Fish.fish;
using System.Drawing;

namespace Fish
{
    class FishTwo : AFish, IFish
    {
        public FishTwo()
        {
            bitmap = new Bitmap(Properties.Resources.latest1);
            speed = 1.2f;
        }

        //Отрисовка рыбки
        public void DrawFish(Graphics g)
        {
            g.DrawImage(bitmap, position);
        }
    }
}
