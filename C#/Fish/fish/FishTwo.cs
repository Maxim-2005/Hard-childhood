using Fish.fish;
using System.Drawing;

namespace Fish
{
    class FishTwo : AFish, IFish
    {
        private readonly Bitmap bitmap = new Bitmap(Properties.Resources.latest1);

        public FishTwo()
        {
            speed = 2;
        }

        //Отрисовка рыбки
        public void DrawFish(Graphics g)
        {
            Position(bitmap);
            g.DrawImage(bitmap, position);
        }
    }
}
