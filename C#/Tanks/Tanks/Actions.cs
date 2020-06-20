using System.Collections.Generic;
using Game2D;

namespace Tanks
{
    class Actions
    {
        private List<ListUnit> ListParty;

        //Перебор всех юнитов
        public void ActUnit(List<ListUnit> ListParty, ListShot listShot)
        {
            //this.ListParty = ListParty;

            foreach (ListUnit party in ListParty)
                foreach (dynamic unit in party.listUnits)
                    if (unit.act != Act.DEAD) Logic(unit);
        }

        //Логига действий
        private void Logic(dynamic unit)
        {
            {
                switch (unit.act)
                {
                    case Act.WAIT:
                        goto case Act.FIRE;
                        //ActWait(unit);
                        break;

                    case Act.FIND:
                        ActFind(unit);
                        break;

                    case Act.MOVE:
                        ActMove(unit);
                        break;

                    case Act.FIRE:
                        ActFire(unit);
                        break;

                    default:
                        unit.act = Act.WAIT;
                        break;
                }
            }
        }

        //Процесс ожидания
        private void ActWait(dynamic unit)
        {
            //Если танк мёртв
            if (unit.life <= 0)
                unit.act = Act.DEAD;

            //Поиск цели
            FindTarget(unit);
        }

        //Процесс поиска
        private void ActFind(dynamic unit)
        {

        }
         
        //Процесс перемещения
        private void ActMove(dynamic unit)
        {

        }

        //Процесс атаки
        private void ActFire(dynamic unit)
        {
            unit.PositionUnit();
            unit.vector = unit.Vector(unit.vector, unit.speed);
        }

        //Поиск цели
        private float FindTarget(dynamic unit)
        {
            foreach (ListUnit party in ListParty)
                foreach (dynamic findUnit in party.listUnits)
                    Func2D.Delta(unit.position, findUnit.position);

            return 0;
        }
    }
}