using System;
using System.Collections.Generic;
using System.Drawing;

namespace Tanks
{
    class ListShot
    {
        public List<Shot> listShot = new List<Shot>();

        //Новый выстрел
        public void NewShot(dynamic unit)
        {
            listShot.Add(new Shot()
            {
                color = unit.color,
                position = unit.position,
                target = unit.target,
                vector = (float)Math.Atan2(unit.target.Y - unit.position.Y, unit.target.X - unit.position.X)
            });
        }
        //Отрисовываем список снарядов
        public void DrawListShot(Graphics g)
        {
            foreach (Shot shot in listShot)
            {
                shot.DrawShot(g);
            }
        }
    }
}
