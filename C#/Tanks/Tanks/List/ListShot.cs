using System.Collections.Generic;
using System.Drawing;

namespace Tanks
{
    class ListShot
    {
        public List<Shot> listShot = new List<Shot>();
        public List<Bang> listBang = new List<Bang>();
        public List<Crater> listCrater = new List<Crater>();

        //Новый выстрел
        public void NewShot(dynamic unit)
        {
            listShot.Add(new Shot(unit));
        }

        //Удаление выстрела
        public void RemoveShot(Shot shot)
        {
            listBang.Add(new Bang(shot.position));
            listShot.Remove(shot);
        }

        //Удаление взрыва
        public void RemoveBang(Bang bang)
        {
            listCrater.Add(new Crater(bang.position));
            listBang.Remove(bang);
        }

        //Отрисовываем список снарядов
        public void DrawListCrater(Graphics g)
        {
            foreach (Crater crater in listCrater)
                crater.DrawCrater(g);
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
