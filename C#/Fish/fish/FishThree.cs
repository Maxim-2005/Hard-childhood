using Fish.fish;
using System.Drawing;

namespace Fish
{
    class FishThree : AFish, IFish
    {
        public FishThree()
        {
            bitmap = new Bitmap(Properties.Resources.latest2);
            speed = 1;
        }

        //Отрисовка рыбки
        public void DrawFish(Graphics g)
        {
            g.DrawImage(bitmap, position);
        }
    }
}
