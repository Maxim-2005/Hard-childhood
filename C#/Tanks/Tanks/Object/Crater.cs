using System.Drawing;

namespace Tanks
{
    class Crater
    {
        public PointF position;
        public ushort time;

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
            g.FillEllipse(new SolidBrush(Color.FromArgb(64/time+64, 32, 16, 0)),
                new RectangleF(-32, -32, 64, 64));
            g.ResetTransform();
        }
    }
}
