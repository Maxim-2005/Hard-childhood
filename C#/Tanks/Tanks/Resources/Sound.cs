using System;
using System.Threading.Tasks;

namespace Tanks
{
    class Sound
    {
        //Звук выстрела
        async public static void Shot()
        {
            await Task.Run(() => Console.Beep(400, 50));
        }

        //Звук взрыва
        async public static void Bang()
        {
            await Task.Run(() => Console.Beep(100, 100));
        }

        #region//Звук заставки
        public static void SW()
        //261 - до 1
        //293 - ре 2
        //329 - ми 3
        //349 - фа 4
        //392 - соль 5
        //440 - ля 6
        //493 - си 7
        {
            Console.Beep(440, 500);
            Console.Beep(440, 500);
            Console.Beep(440, 500);
            Console.Beep(349, 350);
            Console.Beep(523, 150);
            Console.Beep(440, 500);
            Console.Beep(349, 350);
            Console.Beep(523, 150);
            Console.Beep(440, 1000);
            Console.Beep(659, 500);
            Console.Beep(659, 500);
            Console.Beep(659, 500);
            Console.Beep(698, 350);
            Console.Beep(523, 150);
            Console.Beep(415, 500);
            Console.Beep(349, 350);
            Console.Beep(523, 150);
            Console.Beep(440, 1000);
        }

        //Звук заставки
        async public static void Music()
        {
            await Task.Run(() =>
            {
                Console.Beep(349, 250);
                Console.Beep(330, 250);
                Console.Beep(293, 250);
                Console.Beep(261, 250);
                Console.Beep(392, 500);
                Console.Beep(392, 350);
                Console.Beep(349, 250);
                Console.Beep(329, 250);
                Console.Beep(293, 250);
                Console.Beep(261, 250);
                Console.Beep(392, 500);
                Console.Beep(392, 350);

                Console.Beep(349, 250);
                Console.Beep(440, 250);
                Console.Beep(440, 250);
                Console.Beep(349, 250);
                Console.Beep(329, 250);
                Console.Beep(392, 250);
                Console.Beep(392, 250);
                Console.Beep(329, 250);
                Console.Beep(293, 250);
                Console.Beep(329, 250);
                Console.Beep(349, 250);
                Console.Beep(293, 250);
                Console.Beep(261, 500);
                Console.Beep(261, 500);

                Console.Beep(349, 250);
                Console.Beep(440, 250);
                Console.Beep(440, 250);
                Console.Beep(349, 250);
                Console.Beep(329, 250);
                Console.Beep(392, 250);
                Console.Beep(392, 250);
                Console.Beep(329, 250);
                Console.Beep(293, 250);
                Console.Beep(329, 250);
                Console.Beep(349, 250);
                Console.Beep(293, 250);
                Console.Beep(261, 500);
                Console.Beep(261, 500);
            });
        }
        #endregion
    }
}
