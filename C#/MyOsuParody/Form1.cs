using System;
using System.Diagnostics;
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
        private int score, time, step, hipotinuza, scoreAll;
        private Stopwatch stopwatch = new Stopwatch();
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
            stopwatch.Start();

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
            hipotinuza = (int) Math.Sqrt(katetX*katetX + katetY*katetY);
        }

        //Update window
        private void timer1_Tick(object sender, EventArgs e)
        {
            Refresh();
        }

        //Move circle
        private void RandomTarget()
        {
            Point a = point;
            point.X = Width / 2 + random.Next(-4, 4) * 100;
            point.Y = Height / 2 + random.Next(-3, 3) * 100;
            if (a == point) RandomTarget();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            StepGame();
        }

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            StepGame();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        //Step game
        private void StepGame()
        {
            time =(int)stopwatch.Elapsed.TotalMilliseconds;
            step++;
            soundPlayer.Play();

            //Information panel
            score = (200*180) / time + 600 / hipotinuza;
            label1.Text = ("Score: " + score.ToString());
            label2.Text = ("Timer: " + time.ToString());
            label3.Text = ("Accuracy: " + hipotinuza.ToString());
            label4.Text = ("Steps: " + step.ToString());    
            label5.Text = ("scoreAll: " + scoreAll.ToString());
            scoreAll += score;
            RandomTarget();
            stopwatch.Restart();
        }
    }
}
