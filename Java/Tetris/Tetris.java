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
	protected static int block = 50, speed = 500,  x= 3, y = -3, look, color, test;
	private int form[][] = new int [4][2];
	public int ground[][][] = new int [20][10][1]; 
	public int forms[][][] = { //Figure /Block / x,y or r,g,b
		{{1, 2}, {2, 2}, {0, 1}, {1, 1}, {0xA05A46}}, // Z red
		{{1, 2}, {2, 2}, {1, 1}, {1, 0}, {0x6A4A57}}, // L orange
		{{1, 2}, {2, 2}, {1, 1}, {2, 1}, {0xFAC865}}, // O yellow
		{{0, 2}, {1, 2}, {1, 1}, {2, 1}, {0xC24448}}, // S green
		{{0, 2}, {1, 2}, {2, 2}, {3, 2}, {0x534D63}}, // I aqua
		{{1, 2}, {2, 2}, {2, 1}, {2, 0}, {0xF9DEC5}}, // J blue
		{{1, 2}, {0, 1}, {1, 1}, {2, 1}, {0xF7F4F7}}  // T purple
	};
	
	Random random = new Random();
	private static Color colorBlock;

	public static void main(String[] args){
		
		//Application window
		JFrame jFrame = new JFrame("Tetris");
		JFrame.setDefaultLookAndFeelDecorated(true);
		jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		jFrame.setSize(block*16+17, block*20+40);
		jFrame.setResizable(false);
		jFrame.setLocationRelativeTo(null);	
		jFrame.setVisible(true);
		Tetris tetris = new Tetris();
		jFrame.add(tetris);
		tetris.newBlock();
		
		//Press key
		jFrame.addKeyListener(new KeyAdapter() {
			public void keyPressed(KeyEvent event) {
				tetris.repaint();
				speed = 500;
				switch(event.getKeyCode()) {
					case 37: tetris.move(-1); break; //Left
					case 38: tetris.rotate(); break; //Rotate
					case 39: tetris.move(+1); break; //Right
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
			if (form[i][1]+y+1 < 20 && ground[form[i][1]+y+1][form[i][0]+x][0] == 0) test++;
		}
		if (test >= 4) y++; else {
			for (int i = 0; i <4; i++) {
				ground[form[i][1]+y][form[i][0]+x][0] = color;
			}
			clear();
			newBlock();
		}
	}
	
	//Random
	private void newBlock() {
		speed = 500;
		color = forms[look][4][0];
		colorBlock = new Color(color);
		for (int i = 0; i < 4; i++) {
			form[i][0] = forms[look][i][0];
			form[i][1] = forms[look][i][1];
		}
		look = random.nextInt(7);
		x = 3;
		y = -1;
	}
	
	//Move
	private void move(int move) {
		test = 0;
		for (int i = 0; i < 4; i++) {
			if (form[i][0]+x+move < 10 && form[i][0]+x+move >= 0) test++;

		}
		if (test >= 4)
			x = x+move;
	}
	
	//Rotate figure
	private void rotate() {
		int temp;
		for (int i = 0; i < 4; i++) {
			temp = form[i][0];
			form[i][0] = -form[i][1]+3;
			form[i][1] = temp;
		}
	}
	
	//Clear
	private void clear() {
		int temp;
		for (int i = 0; i < 20; i++) {
			temp = 0;
			for (int j = 0; j < 10; j++)
				if (ground[i][j][0] > 0) temp++;
		
		if (temp >= 10)
		for (int j = 0; j < 10; j++)
			ground[i][j][0] = 0;
		}
	}
	
	//Drawing graphics
	public void paint(Graphics ctx) {
		
		//Background Side bar
		ctx.setColor(Color.black);
		ctx.fillRect(block*10, 0, block*6+1, block*20);
		
		//Frame
		ctx.setColor(Color.white);
		ctx.drawRect(block*11-5, block*1-5, block*4+5, block*4+5);
		
		//Side bar
		for (int i = 0; i < 4; i++){
			ctx.setColor(new Color(forms[look][4][0]));
			ctx.fillRect(block*forms[look][i][0]+11*block, block*forms[look][i][1]+1*block, block-1, block-1);
		}
		
		//Down
		for (int i = 0; i < 20; i++){
			for (int j = 0; j < 10; j++){
				ctx.setColor(new Color(ground[i][j][0]));
				ctx.fillRect(j*block, i*block, block, block);
			}
		}
		//Figure
		for (int i = 0; i < 4; i++){
			ctx.setColor(colorBlock);
			ctx.fillRect(block*form[i][0]+x*block, block*form[i][1]+y*block, block, block);
		}
		
		//Grid
		ctx.setColor(Color.black);
		for (int i = 0; i <= 20; i++) ctx.drawLine(0, block*i, block*10, block*i);
		for (int i = 0; i <= 10; i++) ctx.drawLine(block*i, 0, block*i, block*20);
	}
}