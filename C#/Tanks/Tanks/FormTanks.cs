using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Tanks
{
    public partial class FormTanks : Form
    {
        public Graphics g;
        private ListUnit listUnit;
        private Point cursor;
        Shot shot;

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
            listUnit = new ListUnit();
            listUnit.CreateListUnit();

            //SW();
            Sound();

            shot = new Shot();
            shot.position = new PointF(50, 50);
            shot.target = new PointF(1000, 600);
            shot.speed = 20;
        }
        
        //Обновление окна
        private void FormTanks_Paint(object sender, PaintEventArgs e)
        {
            g = e.Graphics;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            cursor = PointToClient(Cursor.Position);
            listUnit.DrawListUnit(g, cursor);

            shot.DrawShot(g);
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

        //Звук заставки
        private void SW()
                    //261 - до 1
        //293 - ре 2
        //329 - ми 3
        //349 - фа 4
        //392 - соль 5
        //440 - ля 6
        //493 - си 7
        {
            Console.Beep(440, 500);
            Console.Beep(440, 500);
            Console.Beep(440, 500);
            Console.Beep(349, 350);
            Console.Beep(523, 150);
            Console.Beep(440, 500);
            Console.Beep(349, 350);
            Console.Beep(523, 150);
            Console.Beep(440, 1000);
            Console.Beep(659, 500);
            Console.Beep(659, 500);
            Console.Beep(659, 500);
            Console.Beep(698, 350);
            Console.Beep(523, 150);
            Console.Beep(415, 500);
            Console.Beep(349, 350);
            Console.Beep(523, 150);
            Console.Beep(440, 1000);
        }

        //Звук заставки
        async private void Sound()
        {
            await Task.Run(() =>
            {
                Console.Beep(349, 250);
                Console.Beep(330, 250);
                Console.Beep(293, 250);
                Console.Beep(261, 250);
                Console.Beep(392, 500);
                Console.Beep(392, 350);
                Console.Beep(349, 250);
                Console.Beep(329, 250);
                Console.Beep(293, 250);
                Console.Beep(261, 250);
                Console.Beep(392, 500);
                Console.Beep(392, 350);

                Console.Beep(349, 250);
                Console.Beep(440, 250);
                Console.Beep(440, 250);
                Console.Beep(349, 250);
                Console.Beep(329, 250);
                Console.Beep(392, 250);
                Console.Beep(392, 250);
                Console.Beep(329, 250);
                Console.Beep(293, 250);
                Console.Beep(329, 250);
                Console.Beep(349, 250);
                Console.Beep(293, 250);
                Console.Beep(261, 500);
                Console.Beep(261, 500);

                Console.Beep(349, 250);
                Console.Beep(440, 250);
                Console.Beep(440, 250);
                Console.Beep(349, 250);
                Console.Beep(329, 250);
                Console.Beep(392, 250);
                Console.Beep(392, 250);
                Console.Beep(329, 250);
                Console.Beep(293, 250);
                Console.Beep(329, 250);
                Console.Beep(349, 250);
                Console.Beep(293, 250);
                Console.Beep(261, 500);
                Console.Beep(261, 500);
            });
        }
    }
}