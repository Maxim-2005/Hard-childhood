using System;
using System.Drawing;
using System.Windows.Forms;

namespace Tanks
{
    public partial class FormTanks : Form
    {
        public Graphics g;
        private ListTanks listTanks, listCar;
        private Point cursor;

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

            listCar = new ListTanks();
            listCar.CreateListCar();
        }

        //Обновление окна
        private void FormTanks_Paint(object sender, PaintEventArgs e)
        {
            g = e.Graphics;
            cursor = PointToClient(Cursor.Position);
            listTanks.DrawListTank(g, cursor);
            listCar.DrawListCar(g, cursor);
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