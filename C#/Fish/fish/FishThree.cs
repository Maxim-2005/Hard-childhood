using Fish.fish;
using System.Drawing;

namespace Fish
{
    class FishThree : AFish, IFish
    {
        private readonly Bitmap bitmap = new Bitmap(Properties.Resources.latest2);

        public FishThree()
        {
            speed = 3;
        }

        //Отрисовка рыбки
        public void DrawFish(Graphics g)
        {
            Position(bitmap);
            g.DrawImage(bitmap, position);
        }
    }
}
