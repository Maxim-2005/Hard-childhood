package com.hikkicoders.galaxyzombies;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;

public class Level_01 extends AppCompatActivity {

    //View
    ImageView imageViewDoor, imageViewWindow, imageViewBad,
            imageViewZombieW, imageViewZombieD,
            imageViewHikkiB, imageViewHikkiD, imageViewHikkiR, btnExit;

    Animation myalpha, mycombo, myrotate, myscale, mytrans, animzombiew, animzombied;

    String step;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.level_01);

        imageViewBad = findViewById(R.id.imageViewBad);
        imageViewWindow = findViewById(R.id.imageViewWindow);
        imageViewDoor = findViewById(R.id.imageViewDoor);
        imageViewZombieW = findViewById(R.id.imageViewZombieW);
        imageViewHikkiB = findViewById(R.id.imageViewHikkiB);
        imageViewHikkiD = findViewById(R.id.imageViewHikkiD);
        imageViewZombieD = findViewById(R.id.imageViewZombieD);
        imageViewHikkiR = findViewById(R.id.imageViewHikkiR);

        myalpha = AnimationUtils.loadAnimation(this, R.anim.myalpha);
        mycombo = AnimationUtils.loadAnimation(this, R.anim.mycombo);
        myrotate = AnimationUtils.loadAnimation(this, R.anim.myrotate);
        myscale = AnimationUtils.loadAnimation(this, R.anim.myscale);
        mytrans = AnimationUtils.loadAnimation(this, R.anim.mytrans);

        animzombiew = AnimationUtils.loadAnimation(this, R.anim.animzombiew);
        animzombied = AnimationUtils.loadAnimation(this, R.anim.animzombied);

        //Слушатели
        View.OnClickListener onClickListener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                imageViewZombieW.setVisibility(View.INVISIBLE);
                imageViewHikkiB.setVisibility(View.INVISIBLE);
                imageViewHikkiD.setVisibility(View.INVISIBLE);
                imageViewZombieD.setVisibility(View.INVISIBLE);
                imageViewHikkiR.setVisibility(View.INVISIBLE);

                if (step == "hikki") {
                    Intent intent = new Intent(Level_01.this, level_02.class);
                    startActivity(intent);
                    finish();
                    System.exit(0);
                }

                switch (view.getId()) {

                    case R.id.imageViewWindow:
                        step = "window";
                        clickWindow();
                        break;

                    case R.id.imageViewDoor:
                        if (step == "window") {
                            step = "door";
                            clickDoor();
                        }
                        break;

                    case R.id.imageViewBad:
                        if (step == "door") {
                            step = "bad";
                            clickBed();
                        }
                        break;

                    case R.id.imageViewHikkiB:
                        if (step == "bad"){
                            step = "hikki";
                            clickHikkiB();
                        }
                        break;
                }
            }
        };

        imageViewBad.setOnClickListener(onClickListener);
        imageViewWindow.setOnClickListener(onClickListener);
        imageViewDoor.setOnClickListener(onClickListener);
        imageViewHikkiB.setOnClickListener(onClickListener);
    }

    private void clickWindow() {
        imageViewZombieW.startAnimation(animzombiew);
        imageViewHikkiR.setVisibility(View.VISIBLE);
        imageViewZombieW.setVisibility(View.VISIBLE);
    }

    private void clickDoor () {
        imageViewZombieD.startAnimation(animzombied);
        imageViewZombieD.setVisibility(View.VISIBLE);
        imageViewHikkiD.setVisibility(View.VISIBLE);
    }

    private void clickBed (){
        imageViewHikkiB.setVisibility(View.VISIBLE);
        imageViewZombieD.setVisibility(View.VISIBLE);
    }

    private void clickHikkiB (){
        imageViewHikkiB.startAnimation(myalpha);
    }

    public void Exit(View view) {
        finish();
        System.exit(0);
    }

    public void btnExit(View view) {
        finish();
        System.exit(0);
    }
}
