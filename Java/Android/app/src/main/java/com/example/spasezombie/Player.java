package com.example.spasezombie;

        import java.util.Random;

public class Player {

    //Подкласс руки
    enum Hands { KAM, NOJ, BUM }

    Hands hand;

    //Рандомнй выбор
    public static Hands randomMetod(){
        Hands[] randomMetod = Hands.values();
        Random random = new Random();
        int i = random.nextInt(randomMetod.length);
        return randomMetod[i];
    }
}