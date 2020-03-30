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
        Bitmap bitmap = new Bitmap(Properties.Resources.unnamed);
        Rectangle body = new Rectangle(new Point(0, 0), new Size(128, 128));
        Rectangle tower = new Rectangle(new Point(128, 0), new Size(128, 128));

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
        Point position = new Point(0, 600);

        private void FormTanks_Paint(object sender, PaintEventArgs e)
        {
            x++;
            label1.Text = x.ToString();
            g = e.Graphics;

            position.X++;
            position.Y--;

            g.DrawImage(bitmap, position.X, position.Y, body, GraphicsUnit.Pixel) ;
            g.DrawImage(bitmap, position.X, position.Y, tower, GraphicsUnit.Pixel);
        }
    }
}