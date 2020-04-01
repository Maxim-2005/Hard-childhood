using System.Drawing;

namespace Tanks
{
    class ListTanks
    {
        Tank tank;

        public void DrawListTank(Graphics g)
        {
            for (byte i = 0; i < 10; i++)
            {
                tank = new Tank();
                tank.DrawTank(g);
            }
        }
    }
}
