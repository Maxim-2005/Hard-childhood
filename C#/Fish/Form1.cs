using System;
using System.Drawing;
using System.Windows.Forms;

namespace Fish
{
    public partial class Form1 : Form
    {
        private Fishes fishes = new Fishes();
        public Graphics g;

        public Form1()
        {
            InitializeComponent();

            SetStyle(ControlStyles.OptimizedDoubleBuffer |
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.UserPaint, true);

            UpdateStyles();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Refresh();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            g = e.Graphics;
            fishes.DrawListFish(g);
        }

        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            if (FormBorderStyle == FormBorderStyle.Sizable)
                FormBorderStyle = FormBorderStyle.None;
            else FormBorderStyle = FormBorderStyle.Sizable;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //fishes = new Fishes();
        }
    }
}
