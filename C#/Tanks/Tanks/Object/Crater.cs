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
            g.FillEllipse(new SolidBrush(Color.FromArgb(128, 128, 128, 128)),
                new RectangleF(-32, -32, 64, 64));
            g.ResetTransform();
        }
    }
}
