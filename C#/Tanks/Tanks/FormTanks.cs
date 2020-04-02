using System;
using System.Drawing;
using System.Windows.Forms;

namespace Tanks
{
    public partial class FormTanks : Form
    {
        Graphics g;
        ListTanks listTanks;

        //Окно приложения
        public FormTanks()
        {
            InitializeComponent();

            SetStyle(ControlStyles.OptimizedDoubleBuffer |
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.UserPaint, true);

            UpdateStyles();
        }

        //Загрузка окна
        private void FormTanks_Load(object sender, EventArgs e)
        {
            listTanks = new ListTanks();
            listTanks.CreateListTanks();
        }

        //Обновление окна
        private void FormTanks_Paint(object sender, PaintEventArgs e)
        {
            g = e.Graphics;
            listTanks.DrawListTank(g);
        }

        //Таймер
        private void timer1_Tick(object sender, EventArgs e)
        {
            Refresh();
        }

        //Старт || Стоп
        private void FormTanks_Click(object sender, EventArgs e)
        {
            if (timer.Enabled == false)
                timer.Enabled = true;
            else timer.Enabled = false;
        }
    }
}