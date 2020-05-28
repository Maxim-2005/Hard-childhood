using System.Collections.Generic;
using System.Drawing;

namespace Tanks
{
    class Game
    {
        private List<ListUnit> ListParty;
        private ListShot listShot;

        //Старт игры
        public void StartGame()
        {
            ListParty = new List<ListUnit>();

            //Цвет█Позиция█Танки█Машинки█
            // #1
            ListParty.Add(new ListUnit());
            // #2
            ListParty.Add(new ListUnit(Color.Red, new Point(30, 20)));
            // #3
            ListParty.Add(new ListUnit(Color.Blue, new Point(70, 20), 2, 1));
            // #4
            ListParty.Add(new ListUnit(new Point(70, 80), 2, 1));
            // #5
            ListParty.Add(new ListUnit(Color.Yellow, new Point(30, 80), 1));

            listShot = new ListShot();

            //Sound.Music();
        }

        //Шаг игры
        public void StepGame(Graphics g, Point cursor)
        {
            foreach (ListUnit party in ListParty)
                party.DrawListUnit(g, cursor, listShot);

            listShot.DrawListShot(g);
        }
    }
}
