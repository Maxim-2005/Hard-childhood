using System;
using System.Collections.Generic;
using System.Drawing;

namespace Tanks
{
    class Actions
    {
        private List<ListUnit> ListParty;
        private ListShot listShot;
        private readonly Random random = new Random();

        //Перебор всех юнитов
        public void ActUnit(List<ListUnit> ListParty, ListShot listShot)
        {
            this.ListParty = ListParty;
            this.listShot = listShot;

            foreach (ListUnit party in ListParty)
                foreach (dynamic unit in party.listUnits)
                    if (unit.act != Act.DEAD)
                        Logic(unit);
        }

        //Логига действий
        private void Logic(dynamic unit)
        {
            {
                switch (unit.act)
                {
                    case Act.WAIT:
                        ActWait(unit);
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
                ActDEAD(unit);

            //Поиск цели
            else
            {
                //Поиск ближайщего танка
                float findDelta = unit.vision, minDelta = unit.vision;
                foreach (ListUnit party in ListParty)
                    foreach (dynamic findUnit in party.listUnits)
                    {
                        if (findUnit.act != Act.DEAD && findUnit.color != unit.color)
                            findDelta = unit.Delta(unit.position, findUnit.position);

                        if (findDelta < minDelta)
                        {
                            minDelta = findDelta;
                            unit.target = findUnit.position;
                        }
                    }

                //Проверка на атаку
                if (minDelta < unit.vision)
                    unit.act = Act.FIRE;

                //Проверка на движение
                else if (minDelta < unit.vision*2)
                    unit.act = Act.MOVE;

                //Поиск цели
                else
                {
                    unit.taeget = new PointF(
                        unit.position.X + random.Next(-128, 128),
                        unit.position.Y + random.Next(-128, 128));
                    unit.act = Act.FIND;
                }
            }
        }

        //Процесс поиска
        private void ActFind(dynamic unit)
        {
            if (unit.Delta(unit.position, unit.target) > unit.speed*64)
{
                unit.PositionUnit();
                unit.vector = unit.Vector(unit.vector, unit.speed);
            }
            else
                unit.act = Act.WAIT;
        }

        //Процесс перемещения
        private void ActMove(dynamic unit)
        {
            if (unit.Delta(unit.position, unit.target) > unit.vision)
            {
                unit.PositionUnit();
                unit.vector = unit.Vector(unit.vector, unit.speed);
            }
            else
                unit.act = Act.WAIT;
        }

        //Процесс атаки
        private void ActFire(dynamic unit)
        {
            if (unit.timeShot < 120)
            {
                unit.timeShot++;
                unit.vector = unit.Vector(unit.vector, unit.speed);
            }
            else
            {
                listShot.NewShot(unit);
                unit.timeShot = 0;
                unit.act = Act.WAIT;
            }
        }

        //Убийство танка
        private void ActDEAD(dynamic unit)
        {
            unit.act = Act.DEAD;
            unit.speed = 0.0f;
            unit.life = 0.0f;
            unit.color = Color.Black;
        }
    }
}