using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        Game game = new Game();

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            LabelHuman.Text = "Камень";
            game.human = 1;
            game.Logic();
            StepGame();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            LabelHuman.Text = "Ножнецы";
            game.human = 2;
            game.Logic();
            StepGame();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            LabelHuman.Text = "Бумага";
            game.human = 3;
            game.Logic();
            StepGame();
        }

        private void StepGame()
        {
            if (game.result == 1)
            {
                game.Win++;
            }
            else if (game.result == 2)
                game.Draw++;
            else
                game.Defeat++;

            LabelWin.Text = game.Win.ToString();
            LabelDraw.Text = game.Draw.ToString();
            LabelDefeat.Text = game.Defeat.ToString();

            LabelBot.Text = game.StepBot;
            LabelResult.Text = game.ResultGame;
        }
    }
}
