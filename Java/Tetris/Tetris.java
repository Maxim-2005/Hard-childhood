/*
 * Tetris
 * Maxim 27.10.2019
 */

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.KeyListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.util.Random;

public class Tetris extends JPanel {

	//Variables
	protected static int block = 50, speed = 500,  x= 3, y = -3, randForm, test;
	public int ground[][][] = new int [20][10][1]; 
	public int form[][][] = { //Figure /Block / x,y or r,g,b
		{{1, 2}, {2, 2}, {0, 1}, {1, 1}, {0xff0000}}, // Z red
		{{1, 2}, {2, 2}, {1, 1}, {1, 0}, {0xffa500}}, // L orange
		{{1, 2}, {2, 2}, {1, 1}, {2, 1}, {0xffff00}}, // O yellow
		{{0, 2}, {1, 2}, {1, 1}, {2, 1}, {0x00ff00}}, // S green
		{{0, 2}, {1, 2}, {2, 2}, {3, 2}, {0x00ffff}}, // I aqua
		{{1, 2}, {2, 2}, {2, 1}, {2, 0}, {0x0000ff}}, // J blue
		{{1, 2}, {0, 1}, {1, 1}, {2, 1}, {0xff00ff}}  // T purple
	};
	
	Random random = new Random();

	public static void main(String[] args){
		
		//Application window
		JFrame jFrame = new JFrame("Tetris");
		JFrame.setDefaultLookAndFeelDecorated(true);
		jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		jFrame.setSize(block*10+17, block*20+40);
		jFrame.setResizable(false);
		jFrame.setLocationRelativeTo(null);	
		jFrame.setVisible(true);
		Tetris tetris = new Tetris();
		jFrame.add(tetris);
		//Press key
		jFrame.addKeyListener(new KeyAdapter() {
			public void keyPressed(KeyEvent event) {
				tetris.repaint();
				speed = 500;
				switch(event.getKeyCode()) {
					case 37: x--; break; //Left
					case 38: tetris.rotate(); break; //Rotate
					case 39: x++; break; //Right
					case 40: speed = 50; break; //Down
				}
			}
		});

		while(true) {
			tetris.game();
			tetris.repaint();
			
			//Fall speed
			try {
				Thread.sleep(speed);
			} catch (Exception e) {}
		}
	}

	//Logic block
	private void game() {
		test = 0;
		for (int i = 0; i < 4; i++) {
			if (form[randForm][i][1]+y+1 < 20) test++;
		}
		if (test >= 4) y++; else {
			for (int i = 0; i <4; i++) {
				ground[form[randForm][i][1]+y][form[randForm][i][0]+x][0] = form[randForm][4][0];
			}
			random();
		}
	}
	
	//Random
	private void random() {
		speed = 1;
		randForm = random.nextInt(7);
		x = 3;
		y = -3;
	}
	
	//Rotate figure
	private void rotate() {
		int temp;
		for (int i = 0; i < 4; i++) {
			temp = form[randForm][i][0];
			form[randForm][i][0] = -form[randForm][i][1]+3;
			form[randForm][i][1] = temp;
		}
	}
	
	//Drawing graphics
	public void paint(Graphics ctx) {
		super.paint(ctx);
		//setBackground(Color.black);
		
		//Down
		for (int i = 0; i < 20; i++){
			for (int j = 0; j < 10; j++){
				ctx.setColor(new Color(ground[i][j][0]));
				ctx.fillRect(j*block, i*block, block, block);
			}
		}
		//Figure
		for (int i = 0; i < 4; i++){
			ctx.setColor(new Color(form[randForm][4][0]));
			ctx.fillRect(block*form[randForm][i][0]+x*block, block*form[randForm][i][1]+y*block, block, block);
		}
		
		//Grid
		ctx.setColor(Color.white);
		for (int i = 0; i <= 20; i++) ctx.drawLine(0, block*i, block*10, block*i);
		for (int i = 0; i <= 10; i++) ctx.drawLine(block*i, 0, block*i, block*20);
	}
}