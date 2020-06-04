using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace K_N_B
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        System.Random rnd = new System.Random();
        public byte human = 0;
        public byte bot = rnd.Next(1, 3);

        private void button1_Click(object sender, EventArgs e)
        {
            human = 1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            human = 2;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            human = 3;
        }

        private void label1_Click_1(object sender, EventArgs e)
        {
        }
    }
}
