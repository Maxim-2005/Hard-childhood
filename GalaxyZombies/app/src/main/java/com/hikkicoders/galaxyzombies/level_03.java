package com.hikkicoders.galaxyzombies;

import android.content.Intent;
import android.media.MediaPlayer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;

public class level_03 extends AppCompatActivity {

    //Обьекты
    ImageView hero1, hero2, hero3, hero4, hero5, hero6, hero7, low, win;
    ImageView wood1, wood2, wood3, wood4, wood5, wood6, wood7, wood8, wood9, wood10, wood11, wood12, wood13, wood14;
    Animation click;
    String step, step2;

    //переменые звука
    MediaPlayer raw1, raw2, raw3, raw4;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_level_03);

        //Другое
        click = AnimationUtils.loadAnimation(this, R.anim.click);
        low = findViewById(R.id.low);
        win = findViewById(R.id.win);

        //Зыуки
        raw1 = MediaPlayer.create(this,R.raw.zombd);
        raw2 = MediaPlayer.create(this,R.raw.zombh);
        raw3 = MediaPlayer.create(this,R.raw.zombr);
        raw4 = MediaPlayer.create(this,R.raw.zombw);

        //Персонаж
        hero1 = findViewById(R.id.hero1);
        hero2 = findViewById(R.id.hero2);
        hero3 = findViewById(R.id.hero3);
        hero4 = findViewById(R.id.hero4);
        hero5 = findViewById(R.id.hero5);
        hero6 = findViewById(R.id.hero6);
        hero7 = findViewById(R.id.hero7);

        //Дерево
        wood1 = findViewById(R.id.wood1);
        wood2 = findViewById(R.id.wood2);
        wood3 = findViewById(R.id.wood3);
        wood4 = findViewById(R.id.wood4);
        wood5 = findViewById(R.id.wood5);
        wood6 = findViewById(R.id.wood6);
        wood7 = findViewById(R.id.wood7);
        wood8 = findViewById(R.id.wood8);
        wood9 = findViewById(R.id.wood9);
        wood10 = findViewById(R.id.wood10);
        wood11 = findViewById(R.id.wood11);
        wood12 = findViewById(R.id.wood12);
        wood13 = findViewById(R.id.wood13);
        wood14 = findViewById(R.id.wood14);

        //Слушатель
        View.OnClickListener onClickListener = new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                if (step == "wood3") {
                    Intent intent = new Intent(level_03.this, level_04.class);
                    startActivity(intent);
                    finish();
                    System.exit(0);
                }

                if (step2 == "low") {
                    Intent intent = new Intent(level_03.this, level_03.class);
                    startActivity(intent);
                    finish();
                    System.exit(0);
                }

                switch (v.getId()) {
                    case R.id.wood1:
                        wood1.startAnimation(click);
                        step = "wood1";
                        //hero1.setVisibility(View.GONE);
                        hero1.setVisibility(View.INVISIBLE);
                        //hero1.setAlpha(0.0f);
                        hero2.setVisibility(View.VISIBLE);
                        break;

                    case R.id.wood2:
                        wood2.startAnimation(click);
                        step = "wood2";
                        low.setVisibility(View.VISIBLE);
                        step2 = "low";
                        break;

                    case R.id.wood3:
                        wood3.startAnimation(click);
                        if (step == "wood5") {
                            hero6.setVisibility(View.INVISIBLE);
                            hero7.setVisibility(View.VISIBLE);
                            step = "wood3";
                            win.setVisibility(View.VISIBLE);
                        } else {
                            low.setVisibility(View.VISIBLE);
                            step2 = "low";
                        }
                        break;

                    case R.id.wood4:
                        wood4.startAnimation(click);
                        step = "wood4";
                        low.setVisibility(View.VISIBLE);
                        step2 = "low";
                        wood4.startAnimation(click);
                        break;

                    case R.id.wood5:
                        wood5.startAnimation(click);
                        if (step == "wood7") {
                            hero5.setVisibility(View.INVISIBLE);
                            hero6.setVisibility(View.VISIBLE);
                            step = "wood5";
                            wood5.startAnimation(click);
                        } else {
                            low.setVisibility(View.VISIBLE);
                            step2 = "low";
                        }
                        break;

                    case R.id.wood6:
                        wood6.startAnimation(click);
                        step = "wood6";
                        low.setVisibility(View.VISIBLE);
                        step2 = "low";
                        wood6.startAnimation(click);
                        break;

                    case R.id.wood7:
                        wood7.startAnimation(click);
                        if (step == "wood11") {
                            hero5.setVisibility(View.VISIBLE);
                            hero4.setVisibility(View.INVISIBLE);
                            step = "wood7";
                            wood7.startAnimation(click);
                        } else {
                            low.setVisibility(View.VISIBLE);
                            step2 = "low";
                        }
                        break;

                    case R.id.wood8:
                        wood8.startAnimation(click);
                        step = "wood8";
                        low.setVisibility(View.VISIBLE);
                        step2 = "low";
                        wood8.startAnimation(click);
                        break;

                    case R.id.wood9:
                        wood9.startAnimation(click);
                        step = "wood9";
                        low.setVisibility(View.VISIBLE);
                        step2 = "low";
                        wood9.startAnimation(click);
                        break;

                    case R.id.wood10:
                        wood10.startAnimation(click);
                        step = "wood10";
                        low.setVisibility(View.VISIBLE);
                        step2 = "low";
                        wood10.startAnimation(click);
                        break;

                    case R.id.wood11:
                        wood11.startAnimation(click);
                        if (step == "wood13") {
                            step = "wood11";
                            wood11.startAnimation(click);
                            hero3.setVisibility(View.INVISIBLE);
                            hero4.setVisibility(View.VISIBLE);
                        } else {
                            low.setVisibility(View.VISIBLE);
                            step2 = "low";
                        }
                        break;

                    case R.id.wood12:
                        wood12.startAnimation(click);
                        step = "wood12";
                        low.setVisibility(View.VISIBLE);
                        step2 = "low";
                        wood12.startAnimation(click);
                        break;

                    case R.id.wood13:
                        wood13.startAnimation(click);
                        if (step == "wood1") {
                            step = "wood13";
                            hero2.setVisibility(View.INVISIBLE);
                            hero3.setVisibility(View.VISIBLE);
                            wood13.startAnimation(click);
                        } else {
                            low.setVisibility(View.VISIBLE);
                            step2 = "low";
                        }
                        break;

                    case R.id.wood14:
                        wood14.startAnimation(click);
                        step = "wood14";
                        low.setVisibility(View.VISIBLE);
                        step2 = "low";
                        wood14.startAnimation(click);
                        break;
                }
            }
        };

        wood1.setOnClickListener(onClickListener);
        wood2.setOnClickListener(onClickListener);
        wood3.setOnClickListener(onClickListener);
        wood4.setOnClickListener(onClickListener);
        wood5.setOnClickListener(onClickListener);
        wood6.setOnClickListener(onClickListener);
        wood7.setOnClickListener(onClickListener);
        wood8.setOnClickListener(onClickListener);
        wood9.setOnClickListener(onClickListener);
        wood10.setOnClickListener(onClickListener);
        wood11.setOnClickListener(onClickListener);
        wood12.setOnClickListener(onClickListener);
        wood13.setOnClickListener(onClickListener);

    }

    public void btnExit(View view) {
        finish();
        System.exit(0);
    }
}
