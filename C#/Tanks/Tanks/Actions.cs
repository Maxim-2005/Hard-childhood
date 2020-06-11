using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tanks
{
    class Actions
    {
        public void ActUnit(List<ListUnit> ListParty, ListShot listShot)
        {
            foreach(ListUnit party in ListParty)
                foreach(dynamic unit in party.listUnits)
                {
                    unit.PositionUnit();
                    unit.vector = unit.Vector(unit.vector, unit.speed);
                }
        }
    }
}
