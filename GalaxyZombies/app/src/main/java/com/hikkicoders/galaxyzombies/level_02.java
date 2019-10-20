package com.hikkicoders.galaxyzombies;

import android.content.Intent;
import android.media.MediaPlayer;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;

public class level_02 extends AppCompatActivity {

    //переменые картинок
    ImageView imageViewbrevno, imageViewolen , imageViewkamen, imageViewhero1, imageViewhero2, imageViewZombi;

    //ПЕРЕМЕНЫЕ ЗDERB
    MediaPlayer z1, z2, z3, z4;

    //коментарий
    Animation click, transrock, combo, trans;

    String step;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_level_02);

        //пр.зн.об.
        imageViewbrevno = findViewById(R.id.imageViewbrevno);
        imageViewolen = findViewById(R.id.imageViewolen);
        imageViewkamen = findViewById(R.id.imageViewkamen);
        imageViewhero1 = findViewById(R.id.imageViewhero1);
        imageViewhero2 = findViewById(R.id.imageViewhero2);
        imageViewZombi = findViewById(R.id.imageViewZombi);

        trans = AnimationUtils.loadAnimation(this, R.anim.trans);
        click = AnimationUtils.loadAnimation(this, R.anim.click);
        transrock = AnimationUtils.loadAnimation(this, R.anim.transrock);
        combo = AnimationUtils.loadAnimation(this, R.anim.combo);

        //прис.знач.звук.
        z1 = MediaPlayer.create (this, R.raw.zombd);
        z2 = MediaPlayer.create (this, R.raw.zombh);
        z3 = MediaPlayer.create (this, R.raw.zombr);
        z4 = MediaPlayer.create (this, R.raw.zombw);

        //слущатель
        View.OnClickListener onClickListener = new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                imageViewhero1.setVisibility(View.INVISIBLE);
                imageViewhero2.setVisibility(View.INVISIBLE);

                if (step == "olen") {
                    Intent intent = new Intent(level_02.this, level_03.class);
                    startActivity(intent);
                    finish();
                    System.exit(0);
                }

                switch (v.getId()) {


                    case R.id.imageViewbrevno:
                        z1.start();
                        step = "brevno";
                        imageViewbrevno.startAnimation(click);
                        imageViewhero1.setVisibility(View.VISIBLE);
                        break;

                    case R.id.imageViewkamen:
                        imageViewkamen.startAnimation(click);
                        if (step == "brevno") {
                            step = "kamen";
                            imageViewkamen.startAnimation(transrock);
                            imageViewhero1.setVisibility(View.VISIBLE);
                        }
                        break;

                    case R.id.imageViewolen:
                        imageViewolen.startAnimation(click);
                        if (step == "kamen") {
                            step = "olen";
                            imageViewolen.startAnimation(trans);
                            imageViewhero1.setVisibility(View.VISIBLE);
                            imageViewkamen.startAnimation(click);
                            imageViewolen.setVisibility(View.VISIBLE);
                            imageViewZombi.startAnimation(combo);
                        }
                        break;
                }
            }
        };

        imageViewbrevno.setOnClickListener(onClickListener);
        imageViewolen.setOnClickListener(onClickListener);
        imageViewkamen.setOnClickListener(onClickListener);

    }

    public void btnExit(View view) {
        finish();
        System.exit(0);
    }
}
