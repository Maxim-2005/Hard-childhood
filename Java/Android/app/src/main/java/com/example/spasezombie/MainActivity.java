package com.example.spasezombie;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
// Основной код
/*
Комментарии
 */

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void Click1(View view) {
        Intent intent = new Intent(MainActivity.this, knb.class);
        startActivity(intent);
        finish();
        System.exit(0);
    }

    public void Click_xMif(View view) {
        Intent intent = new Intent(MainActivity.this, Wed.class);
        startActivity(intent);
        finish();
        System.exit(0);
    }

    public void ClickExit(View view) {
        finish();
        System.exit(0);
    }

    public void zalSlavi(View view) {
        Intent intent = new Intent(MainActivity.this, FullscreenActivity.class);
        startActivity(intent);
    }
}
