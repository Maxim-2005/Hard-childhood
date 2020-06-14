using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WindowsFormsApp1
{
    class Bot
    {
        Random random = new Random();
        public int bot;

        public void RndBot()
        {
            bot = random.Next(1, 4);
        }
    }
}
