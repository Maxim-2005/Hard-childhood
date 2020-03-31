using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Tanks
{
    public partial class FormTanks : Form
    {
        Graphics g;
        Tank tank = new Tank();
        Random random = new Random();

        public FormTanks()
        {
            InitializeComponent();

            SetStyle(ControlStyles.OptimizedDoubleBuffer |
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.UserPaint, true);

            UpdateStyles();
        }

        int x;
        private void timer1_Tick(object sender, EventArgs e)
        {
            Refresh();
        }

        private void FormTanks_Click(object sender, EventArgs e)
        {
            if (timer.Enabled == false)
                timer.Enabled = true;
            else timer.Enabled = false;
        }
        


        private void FormTanks_Paint(object sender, PaintEventArgs e)
        {
            x++;
            label1.Text = x.ToString();
            g = e.Graphics;

            Point position = Point.Empty;

            //for (byte i = 0; i < 10; i++)
            //{
                position.X = 500;
                position.Y = 300;
                tank.DrawTank(g, position);
            //}
        }
    }
}