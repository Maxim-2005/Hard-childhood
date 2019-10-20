package com.hikkicoders.galaxyzombies;

import android.content.Intent;
import android.media.MediaPlayer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;
import android.widget.TextView;

public class level_04 extends AppCompatActivity {

    //Переменные текста
    TextView textViewNoFuel;

    //Переменные звука
    MediaPlayer zombie1, zombie2, zombie3, zombie4;

    //Переменные Анимации
    Animation myscale, myalpha;

    //Переменные елеменотов экрана
    ImageView imageViewBoat, imageViewTree,
            imageViewKey, imageViewCase, imageViewCanistra,
            imageViewHikkiMid, imageViewHikkiTree, imageViewFox,
            imageViewZombie1, imageViewZombie2, imageViewZombie3;

    String step;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_level_04);

        //Присваеваем значение тексту
        textViewNoFuel = findViewById(R.id.textViewNoFuel);

        //Присваеваем значение переменным
        zombie1 = MediaPlayer.create(this, R.raw.zombd);
        zombie2 = MediaPlayer.create(this, R.raw.zombh);
        zombie3 = MediaPlayer.create(this, R.raw.zombr);
        zombie4 = MediaPlayer.create(this, R.raw.zombw);

        //Присваеваем значение анимации
        myscale = AnimationUtils.loadAnimation(this, R.anim.myscale);
        myalpha = AnimationUtils.loadAnimation(this, R.anim.myalpha);

        //Присваиваем значение елементам экрана
        imageViewBoat = findViewById(R.id.imageViewBoat);
        imageViewTree = findViewById(R.id.imageViewTree);
        imageViewKey = findViewById(R.id.imageViewKey);
        imageViewCase = findViewById(R.id.imageViewCase);
        imageViewCanistra = findViewById(R.id.imageViewCanistra);
        imageViewHikkiMid = findViewById(R.id.imageViewHikkiMid);
        imageViewHikkiTree = findViewById(R.id.imageViewHikkiTree);
        imageViewFox = findViewById(R.id.imageViewFox);
        imageViewZombie1 = findViewById(R.id.imageViewZombie1);
        imageViewZombie2 = findViewById(R.id.imageViewZombie2);
        imageViewZombie3 = findViewById(R.id.imageViewZombie3);

        //Слушатели
        View.OnClickListener onClickListener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                if (step == "Boat") {
                    finish();
                    System.exit(0);
                }

                textViewNoFuel.setVisibility(View.INVISIBLE);
                imageViewHikkiTree.setVisibility(View.INVISIBLE);
                imageViewCanistra.setVisibility(View.INVISIBLE);
                imageViewZombie1.setVisibility(View.INVISIBLE);
                imageViewZombie2.setVisibility(View.INVISIBLE);
                imageViewZombie3.setVisibility(View.INVISIBLE);
                imageViewFox.setVisibility(View.INVISIBLE);
                imageViewKey.setVisibility(View.INVISIBLE);
                imageViewCanistra.setVisibility(View.INVISIBLE);

                switch (view.getId()) {

                    case R.id.imageViewTree:
                        step = "Tree";
                        imageViewTree.startAnimation(myscale);
                        imageViewHikkiMid.setVisibility(View.INVISIBLE);
                        imageViewHikkiTree.setVisibility(View.VISIBLE);
                        imageViewFox.setVisibility(View.VISIBLE);
                        imageViewKey.setVisibility(View.VISIBLE);
                        break;

                    case R.id.imageViewFox:
                        imageViewFox.startAnimation(myscale);
                        if (step == "Tree") {
                            step = "Fox";
                            imageViewFox.setVisibility(View.GONE);
                            imageViewZombie1.setVisibility(View.VISIBLE);
                            imageViewZombie2.setVisibility(View.VISIBLE);
                            imageViewZombie3.setVisibility(View.VISIBLE);
                            imageViewHikkiTree.setVisibility(View.VISIBLE);
                            imageViewKey.setVisibility(View.VISIBLE);
                        }
                        break;

                    case R.id.imageViewKey:
                        imageViewKey.startAnimation(myscale);
                        if (step == "Fox") {
                            step = "Key";
                            imageViewKey.setVisibility(View.INVISIBLE);
                            imageViewHikkiMid.setVisibility(View.VISIBLE);
                        }
                        break;

                    case R.id.imageViewCase:
                        imageViewCase.startAnimation(myscale);
                        imageViewHikkiMid.setVisibility(View.VISIBLE);
                        if (step == "Key") {
                            step = "Case";
                            imageViewCase.setVisibility(View.INVISIBLE);
                            imageViewCanistra.setVisibility(View.VISIBLE);
                        }
                        break;

                    case R.id.imageViewCanistra:
                        imageViewCanistra.startAnimation(myscale);
                        if (step == "Case") {
                            step = "Can";
                            imageViewCanistra.setVisibility(View.INVISIBLE);
                        }
                        break;

                    case R.id.imageViewBoat:
                        imageViewBoat.startAnimation(myscale);
                        imageViewHikkiMid.setVisibility(View.VISIBLE);
                        textViewNoFuel.setVisibility(View.VISIBLE);
                        if (step == "Can") {
                            step = "Boat";
                            textViewNoFuel.setVisibility(View.INVISIBLE
                            );
                        }
                        break;

                    case R.id.imageViewHikkiMid:
                        imageViewHikkiMid.startAnimation(myscale);
                        break;

                }
            }
        };

        imageViewBoat.setOnClickListener(onClickListener);
        imageViewTree.setOnClickListener(onClickListener);
        imageViewKey.setOnClickListener(onClickListener);
        imageViewCase.setOnClickListener(onClickListener);
        imageViewCanistra.setOnClickListener(onClickListener);
        imageViewHikkiMid.setOnClickListener(onClickListener);
        imageViewFox.setOnClickListener(onClickListener);

    }

    public void btnExit(View view) {
        finish();
        System.exit(0);
    }
}
