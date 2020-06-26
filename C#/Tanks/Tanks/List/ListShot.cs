using System;
using System.Collections.Generic;
using System.Drawing;
using System.Threading.Tasks;

namespace Tanks
{
    class ListShot
    {
        public List<Shot> listShot = new List<Shot>();
        public List<Bang> listBang = new List<Bang>();

        //Новый выстрел
        async public void NewShot(dynamic unit)
        {
            listShot.Add(new Shot(unit));
            await Task.Run(() => Console.Beep(250, 10));
        }

        //Удаление выстрела
        public void RemoveShot(Shot shot)
        {
            listBang.Add(new Bang(shot.position));
            listShot.Remove(shot);
        }

        //Отрисовываем список снарядов
        public void DrawListShot(Graphics g)
        {
            foreach (Shot shot in listShot)
                shot.DrawShot(g);
            foreach (Bang bang in listBang)
                bang.DrawBang(g);
        }
    }
}
