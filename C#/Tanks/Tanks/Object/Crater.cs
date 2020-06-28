using System.Drawing;

namespace Tanks
{
    class Crater
    {
        public PointF position;
        public byte time;

        /// <summary>
        /// Конструктор воронки
        /// </summary>
        public Crater(PointF position)
        {
            this.position = position;
        }

        public void DrawCrater(Graphics g)
        {
            g.TranslateTransform(position.X, position.Y);
            g.FillEllipse(new SolidBrush(Color.FromArgb(126, 0, 0, 0)),
                new RectangleF(-time / 2, -time / 2, time, time));
            g.ResetTransform();
        }
    }
}
