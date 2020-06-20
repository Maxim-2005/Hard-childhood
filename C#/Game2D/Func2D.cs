﻿/*
 * Project: Библиотека для расчетов в 2D
 * Version: 1.0.0.1
 * Data:    20.06.2020
 * Author:  Maxim
 */

using System;
using System.Drawing;

namespace Game2D
{
    public static class Func2D
    {
        ///<summary>
        ///Расчет расстояния между точками (int)
        ///<summary>
        public static int Delta(Point point1, Point point2)
        {
            int CathetX = point1.X - point2.X;
            int CathetY = point1.Y - point2.Y;

            return (int)Math.Sqrt(CathetX * CathetX + CathetY * CathetY);
        }

        ///<summary>
        ///Расчет расстояния между точками (float)
        ///<summary>
        public static float Delta(PointF point1, PointF point2)
        {
            float CathetX = point1.X - point2.X;
            float CathetY = point1.Y - point2.Y;

            return (float)Math.Sqrt(CathetX * CathetX + CathetY * CathetY);
        }
    }
}
