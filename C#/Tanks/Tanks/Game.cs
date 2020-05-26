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

            ListParty.Add(new ListUnit(Color.Red, new Point(30, 20)));
            ListParty.Add(new ListUnit(Color.Blue, new Point(70, 80)));
            ListParty.Add(new ListUnit());

            listShot = new ListShot();

            Sound.Music();
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
