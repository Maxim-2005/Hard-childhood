using System.Drawing;

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
            Sound.Bang();
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
