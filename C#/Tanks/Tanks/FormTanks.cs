using System;
using System.Drawing;
using System.Windows.Forms;

namespace Tanks
{
    public partial class FormTanks : Form
    {
        Graphics g;
        ListTanks listTanks;

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
            listTanks.DrawListTank(g);
        }

        private void FormTanks_Load(object sender, EventArgs e)
        {
            listTanks = new ListTanks();
        }
    }
}