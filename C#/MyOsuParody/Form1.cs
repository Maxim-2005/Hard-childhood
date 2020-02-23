using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Media;
using System.Windows.Forms;

namespace MyOsuParody
{
    public partial class Form1 : Form
    {
        //Variable's and object's
        private Random random = new Random();
        private Bitmap target = Resource1.cursor;
        private Point point = Point.Empty;
        private Pen pen = new Pen(Color.Black, 2);
        private SoundPlayer soundPlayer = new SoundPlayer(Resource1.hit);
        private int score;
        //private Bitmap circle = Resource1.circle;

        //Star window
        public Form1()
        {
            //Hide cursor
            Cursor.Hide();

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

            Point position = this.PointToClient(Cursor.Position);
            //ctx.DrawImage(circle, 100, 100, 100, 100); ;
            Rectangle cursorPosition = new Rectangle(position.X - 50, position.Y - 50, 100, 100);
            Rectangle targetPosition = new Rectangle(point.X, point.Y, 100, 100);

            ctx.DrawEllipse(pen, targetPosition);
            ctx.DrawImage(target, cursorPosition);

            int katetX =cursorPosition.X - targetPosition.X;
            int katetY =cursorPosition.Y - targetPosition.Y;
            int Hipotinuza = (int) Math.Sqrt(katetX*katetX + katetY*katetY);

            label1.Text = Hipotinuza.ToString();
        }

        //Update window
        private void timer1_Tick(object sender, EventArgs e)
        {
            Refresh();
        }

        //Move circle
        private void RandomTarget()
        {
            point.X = Width/2 + random.Next(-4, 4) * 100;
            point.Y = Height/2 + random.Next(-3, 3) * 100;
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            StepGame();
        }

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            StepGame();
        }

        //Step game
        private void StepGame()
        {
            score++;
            soundPlayer.Play();
            RandomTarget();
        }
    }
}
