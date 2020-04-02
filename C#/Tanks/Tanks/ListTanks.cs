using System.Collections.Generic;
using System.Drawing;

namespace Tanks
{
    class ListTanks : List<Tank>
    {
        public Tank tank = new Tank();
        public List<Tank> listTanks = new List<Tank>();

        //Создание списка танков
        public List<Tank> CreateListTanks()
        {
            for (byte i = 1; i <= 10; i++)
            {
                listTanks.Add(new Tank()
                {
                    id = i,
                    position = tank.Position()
                });
            }
            return listTanks;
        }

        //Отрисовка списка танков
        public void DrawListTank(Graphics g)
        {
            foreach (Tank tank in listTanks)
            {
                tank.DrawTank(g);
            }
        }
    }
}