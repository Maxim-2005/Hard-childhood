using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Tanks
{
    class Shooting
    {
        private ListShot listShot;

        //Расчет стрельбы
        async public void ActShot(List<ListUnit> ListParty, ListShot listShot)
        {
            this.listShot = listShot;

            foreach (Shot shot in listShot.listShot)
            {
                await Task.Run(() => Console.Beep(100, 100));
                shot.MoveShot();

                if (shot.speed < 5)
                    listShot.RemoveShot(shot);
            }
        }
    }
}
