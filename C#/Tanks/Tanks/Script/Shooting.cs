using System.Collections.Generic;

namespace Tanks
{
    class Shooting
    {
        private Shot shot;
        private Bang bang;
        private Crater crater;

        //Расчет стрельбы
        public void ActShot(List<ListUnit> ListParty, ListShot listShot)
        {
            //Расчет пуль
            for (int i = 0; i < listShot.listShot.Count; i++)
            {
                shot = listShot.listShot[i];
                shot.MoveShot();

                if (shot.speed < 5)
                    listShot.RemoveShot(shot);
            }

            //Расчет взрывов
            for (int i = 0; i < listShot.listBang.Count; i++)
            {
                bang = listShot.listBang[i];
                if (bang.time > 96)
                    //************** РАСТЧЕТ ДАМАЖА **************
                    listShot.RemoveBang(bang);
                else
                    bang.time += 8;
            }
        }
    }
}
