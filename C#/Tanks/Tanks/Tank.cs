using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tanks
{
    class Tank
    {
        Bitmap bitmap = new Bitmap(Properties.Resources.unnamed);
        Rectangle body = new Rectangle(new Point(0, 0), new Size(128, 128));
        Rectangle tower = new Rectangle(new Point(128, 0), new Size(128, 128));

        //Танк
        int x = 0;
        public void DrawTank(Graphics g, Point position)
        {
            x++;
            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(x);
            g.DrawImage(bitmap, -63, -78, body, GraphicsUnit.Pixel);
            g.ResetTransform();

            g.TranslateTransform(position.X, position.Y);
            g.RotateTransform(x);
            g.DrawImage(bitmap, -64, -60, tower, GraphicsUnit.Pixel);
            g.ResetTransform();
        }
    }
}
