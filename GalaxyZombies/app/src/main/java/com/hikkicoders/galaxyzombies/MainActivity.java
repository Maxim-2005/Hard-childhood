package com.hikkicoders.galaxyzombies;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void btnStart(View view) {
        Intent intent = new Intent(MainActivity.this, Level_01.class);
        startActivity(intent);
    }

    public void btnExit(View view) {
        finish();
        System.exit(0);
    }

    public void btnCont(View view) {
        Intent intent = new Intent(MainActivity.this, Level_01.class);
        startActivity(intent);
    }
}
