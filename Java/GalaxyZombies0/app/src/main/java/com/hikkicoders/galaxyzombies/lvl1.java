package com.hikkicoders.galaxyzombies;

import android.graphics.Color;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;

import java.lang.invoke.MethodHandles;

public class lvl1 extends AppCompatActivity {

    //View
    ImageView imageViewDoor, imageViewWindow, imageViewBad, imageViewZombieW, imageViewHikkiB, imageViewHikkiD, imageViewZombieD, imageViewHikkiR;
    Animation myalpha, mycombo, myrotate, myscale, mytrans;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lvl1);

        imageViewBad = findViewById (R.id.imageViewBad);
        imageViewWindow = findViewById (R.id.imageViewWindow);
        imageViewDoor = findViewById (R.id.imageViewDoor);
        imageViewZombieW = findViewById (R.id.imageViewZombieW);
        imageViewHikkiB = findViewById (R.id.imageViewHikkiB);
        imageViewHikkiD = findViewById (R.id.imageViewHikkiD);
        imageViewZombieD = findViewById (R.id.imageViewZombieD);
        imageViewHikkiR = findViewById (R.id.imageViewHikkiR);

        myalpha = AnimationUtils.loadAnimation (this, R.anim.myalpha);
        mycombo = AnimationUtils.loadAnimation (this, R.anim.mycombo);
        myrotate = AnimationUtils.loadAnimation (this, R.anim.myrotate);
        myscale = AnimationUtils.loadAnimation (this, R.anim.myscale);
        mytrans = AnimationUtils.loadAnimation (this, R.anim.mytrans);

        //Слушатели
        View.OnClickListener onClickListener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Animation anim = null;
                switch (view.getId()) {

                    case R.id.imageViewBad:
                        break;
                    case R.id.imageViewWindow:
                        break;
                    case R.id.imageViewDoor:
                        break;
                    case R.id.imageViewHikkiB:
                        imageViewHikkiB.startAnimation(myalpha);
                        break;
                }
            }
        };

        imageViewBad.setOnClickListener(onClickListener);
        imageViewWindow.setOnClickListener(onClickListener);
        imageViewDoor.setOnClickListener(onClickListener);

    }
}
