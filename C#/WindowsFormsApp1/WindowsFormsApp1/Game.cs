using System;
using System.Collections.Generic;
using System.Linq;
using System.Media;
using System.Text;
using System.Threading.Tasks;

namespace WindowsFormsApp1
{
    class Game
    {
        Bot bot = new Bot();
        public byte human = 0;
        public int result, Win, Defeat, Draw;
        public string StepBot, ResultGame;

        public void Logic()
        {
            bot.RndBot();

            if (bot.bot == 1) StepBot = "Камень";
            else if
                (bot.bot == 2) StepBot = "Ножнецы";
            else 
                StepBot = "Бумага";

            if (human == bot.bot)
            {
                result = 2;
                ResultGame = "Ничья";
            }

            else if ((human == 1 & bot.bot == 2) ||
                    (human == 2 & bot.bot == 3) ||
                    (human == 3 & bot.bot == 1))
            {
                result = 1;
                ResultGame = "Победа";
            }

            else
            {
                result = 3;
                ResultGame = "Поражение";
            }
        }
    }
}
