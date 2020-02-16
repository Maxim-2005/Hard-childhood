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
        //private Bitmap circle = Resource1.circle;

        //Star window
        public Form1()
        {
            InitializeComponent();

            SetStyle(ControlStyles.OptimizedDoubleBuffer |
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.UserPaint, true);

            UpdateStyles();

        }

        //Paint window
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics ctx = e.Graphics;
            ctx.SmoothingMode = SmoothingMode.AntiAlias;
            int score = 0;
            score++;
            label1.Text = score.ToString();

            var position = this.PointToClient(Cursor.Position);

            point.X = 400 + random.Next(-4, 4) * 100;
            point.Y = 250 + random.Next(-3, 3) * 100;

            //ctx.DrawImage(circle, 100, 100, 100, 100); ;
            ctx.DrawEllipse(new Pen(Color.Black, 2), point.X, point.Y, 100, 100);
            ctx.DrawImage(target, position.X - 75, position.Y - 75, 150, 150);
        }

        //Update window
        private void timer1_Tick(object sender, EventArgs e)
        {
            Refresh();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
