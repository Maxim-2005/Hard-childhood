using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MyOsuParody
{
    public partial class Form1 : Form
    {
        //Variable's and object's
        private Random random = new Random();
        private Bitmap target = Resource1.cursor;
        private Point point = Point.Empty;
        private int score;
        //private Bitmap circle = Resource1.circle;

        //Star window
        public Form1()
        {
            InitializeComponent();

            SetStyle(ControlStyles.OptimizedDoubleBuffer |
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.UserPaint, true);

            UpdateStyles();
            RandomTarget();

        }

        //Paint window
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics ctx = e.Graphics;
            ctx.SmoothingMode = SmoothingMode.AntiAlias;
            label1.Text = score.ToString();

            Point position = this.PointToClient(Cursor.Position);

            //ctx.DrawImage(circle, 100, 100, 100, 100); ;
            Rectangle cursorPosition = new Rectangle(position.X - 75, position.Y - 75, 150, 150);
            Rectangle targetPosition = new Rectangle(point.X, point.Y, 100, 100);

            ctx.DrawEllipse(new Pen(Color.Black, 2), targetPosition);
            ctx.DrawImage(target, cursorPosition);
        }

        //Update window
        private void timer1_Tick(object sender, EventArgs e)
        {
            Refresh();
            score++;
        }

        //Move circle
        private void RandomTarget()
        {
            point.X = 400 + random.Next(-4, 4) * 100;
            point.Y = 250 + random.Next(-3, 3) * 100;
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            RandomTarget();
        }

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            RandomTarget();
        }
    }
}
