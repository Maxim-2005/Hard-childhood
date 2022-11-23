package com.example.spasezombie;

import android.content.Intent;
import android.graphics.Color;
import android.media.AudioManager;
import android.media.SoundPool;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

public class knb extends AppCompatActivity {

    //Объекты
    ImageView kam, noj, bum, imageViewUser, imageViewComp;
    TextView textKNB, textViewGame, textViewWin, textViewLose, textViewDraw;
    int scoreGame, scoreWin, scoreLose, scoreDraw;

    //Звук
    final SoundPool soundPool = new SoundPool(3, AudioManager.STREAM_MUSIC, 0);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.knb);

        //Присваеваем значение переменным
        kam = findViewById(R.id.kam);
        noj = findViewById(R.id.noj);
        bum = findViewById(R.id.bum);

        textKNB = findViewById(R.id.textKNB);
        textViewGame = findViewById(R.id.textViewGame);
        textViewWin = findViewById(R.id.textViewWin);
        textViewLose = findViewById(R.id.textViewLose);
        textViewDraw = findViewById(R.id.textViewDraw);

        imageViewUser = findViewById(R.id.imageViewUser);
        imageViewComp = findViewById(R.id.imageViewComp);

        //Загружаем файл
        soundPool.load(this, R.raw.sound, 1);


        //Создаем объекты
        final Player user = new Player();
        final Player comp = new Player();

        //Слушатели
        View.OnClickListener onClickListener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {
            switch (view.getId()) {
                case R.id.kam:
                    user.hand = Player.Hands.KAM;
                    imageViewUser.setImageResource(R.drawable.kam);
                    break;
                case R.id.noj:
                    imageViewUser.setImageResource(R.drawable.noj);
                    user.hand = Player.Hands.NOJ;
                    break;
                case R.id.bum:
                    imageViewUser.setImageResource(R.drawable.bum);
                    user.hand = Player.Hands.BUM;
                    break;
            }

            //Воспроизводим звук
            soundPool.play(1,1,1,1,0,1);

            //Выбор компьютера
            comp.hand = Player.randomMetod();

            switch (comp.hand) {
                case KAM:
                    imageViewComp.setImageResource(R.drawable.kam);
                    break;
                case NOJ:
                    imageViewComp.setImageResource(R.drawable.noj);
                    break;
                case BUM:
                    imageViewComp.setImageResource(R.drawable.bum);
                    break;
            }

            if (user.hand == comp.hand) {
                textKNB.setText("НИЧЬЯ");
                textKNB.setTextColor(Color.YELLOW);
                scoreDraw++;
            } else if (user.hand == Player.Hands.KAM && comp.hand == Player.Hands.NOJ ||
                    user.hand == Player.Hands.NOJ && comp.hand == Player.Hands.BUM ||
                    user.hand == Player.Hands.BUM && comp.hand == Player.Hands.KAM) {
                textKNB.setText("ПОБЕДА");
                textKNB.setTextColor(Color.GREEN);
                scoreWin++;
            } else {
                textKNB.setText("ПОРАЖЕНИЕ");
                textKNB.setTextColor(Color.RED);
                scoreLose++;

                imageViewUser.setAlpha(128);

            }

            scoreGame++;
            textViewGame.setText(String.valueOf(scoreGame));
            textViewDraw.setText(String.valueOf(scoreDraw));
            textViewWin.setText(String.valueOf(scoreWin));
            textViewLose.setText(String.valueOf(scoreLose));
            }
        };

        kam.setOnClickListener(onClickListener);
        noj.setOnClickListener(onClickListener);
        bum.setOnClickListener(onClickListener);

    }
    public void Click2(View view) {
        Intent intent = new Intent(knb.this, MainActivity.class);
        startActivity(intent);
        finish();
        System.exit(0);
    }
    public void ClickExit(View view) {
        finish();
        System.exit(0);
    }
}