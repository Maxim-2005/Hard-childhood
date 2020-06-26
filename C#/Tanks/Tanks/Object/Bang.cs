using System.Drawing;
using System.Security.Cryptography.X509Certificates;
using System.Threading;

namespace Tanks
{
    class Bang
    {
        public PointF position;
        public byte time;

        /// <summary>
        /// Конструктор взрыва
        /// </summary>
        public Bang(PointF position)
        {
            this.position = position;   
        }

        public void DrawBang(Graphics g)
        {
            g.TranslateTransform(position.X, position.Y);
            g.FillEllipse(new SolidBrush(Color.FromArgb(192 - time, time + 128, time, 0)),
                new RectangleF(-time/2, -time/2, time, time));
            g.ResetTransform();
        }
    }
}
