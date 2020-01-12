/*
 * Tetris
 * Maxim 27.10.2019
 */

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Font;
import java.awt.Image;
import java.awt.event.KeyListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.util.Random;

public class Tetris extends JPanel {

	//Variables
	protected static int block = 50, speed = 500, look, color, test, line, step;
	private int form[][] = new int [4][2];
	public int ground[][][] = new int [20][10][1]; 
	public int forms[][][] = { //Figure /Block / x,y or r,g,b
		{{1, 2}, {0, 1}, {2, 2}, {1, 1}, {0xA05A46}}, // Z red
		{{1, 1}, {1, 0}, {2, 2}, {1, 2}, {0x6A4A57}}, // L orange
		{{2, 2}, {1, 2}, {1, 1}, {2, 1}, {0xFAC865}}, // O yellow
		{{1, 2}, {0, 2}, {1, 1}, {2, 1}, {0xC24448}}, // S green
		{{1, 2}, {2, 2}, {0, 2}, {3, 2}, {0x534D63}}, // I aqua
		{{2, 1}, {2, 0}, {2, 2}, {1, 2}, {0xF9DEC5}}, // J blue
		{{1, 1}, {0, 1}, {1, 2}, {2, 1}, {0xF7F4F7}}  // T purple
	};
	
	Random random = new Random();
	private static Color colorBlock;
	private static Image image = new ImageIcon("Logo.png").getImage();

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
		for (int i = 0; i < 4; i++)
			if (form[i][1]+1 < 20 && ground[form[i][1]+1][form[i][0]][0] == 0)
				test++;
		if (test >= 4)
			for (int i = 0; i < 4; i++)
				form[i][1]++;
		else {
			for (int i = 0; i < 4; i++)
				ground[form[i][1]][form[i][0]][0] = color;
			clear();
			newBlock();
		}
	}
	
	//New block
	private void newBlock() {
		speed = 500-line*5;
		color = forms[look][4][0];
		colorBlock = new Color(color);
		step++;
		for (int i = 0; i < 4; i++) {
			form[i][0] = forms[look][i][0]+3;
			form[i][1] = forms[look][i][1]-1;
		}
		look = random.nextInt(7);
	}
	
	//Move
	private void move(int move) {
		test = 0;
		for (int i = 0; i < 4; i++) {
			if (form[i][0]+move < 10 && form[i][0]+move >= 0 && ground[form[i][1]][form[i][0] + move][0] == 0)
				test++;
		}
		if (test >= 4)
			for (int i = 0; i < 4; i++)
				form[i][0] += move;
	}
	
	//Rotate figure
	private void rotate() {
		
		//Cloning with rotation
		int tempBlock[][] = new int[4][2];
		for (int i = 0; i < 4; i++) {
			tempBlock[i][0] = -form[i][1]+form[0][1]+form[0][0];
			tempBlock[i][1] = form[i][0]-form[0][0]+form[0][1];
		}
		
		//Rotation check
		int temp = 0;
		for (int i = 0; i < 4; i++)
			if (tempBlock[i][0] >= 0 && tempBlock[i][0] < 10 && ground[tempBlock[i][1]][tempBlock[i][0]][0] == 0)
				temp++;

			
		//Rotation
		if (temp >= 4 && color != 0xFAC865) //******** наговнокодил с квадратом ********
			for (int i = 0; i < 4; i++) {
				form[i][0] = tempBlock[i][0];
				form[i][1] = tempBlock[i][1];
			}
	}
	
	//Clear
	private void clear() {
		int temp;
		for (int i = 0; i < 20; i++) {
			temp = 0;
			for (int j = 0; j < 10; j++)
				if (ground[i][j][0] > 0) temp++;
		
			if (temp >= 10){
				line++;
				for (int iClear = i; iClear > 0; iClear--)
					for (int j = 0; j < 10; j++)
						if (iClear > 0) 
							ground[iClear][j][0] = ground[iClear-1][j][0];
			}
		}
	}
	
	//Drawing graphics
	public void paint(Graphics ctx) {
		
		//Background Side bar
		ctx.setColor(Color.black);
		ctx.fillRect(block*10, 0, block*6+1, block*20);
		
		//Frame
		//ctx.setColor(Color.white);
		//ctx.drawRect(block*11-5, block*1-5, block*4+5, block*4+5);
		
		//Side bar
		for (int i = 0; i < 4; i++){
			ctx.setColor(new Color(forms[look][4][0]));
			ctx.fillRect(block*forms[look][i][0]+11*block, block*forms[look][i][1]+1*block, block-1, block-1);
		}
		
		//Game info
		ctx.setFont(new Font("Courier New", Font.BOLD, 24));
		ctx.setColor(Color.white);
		ctx.drawString(("Speed: " + speed), 11*block, 300);
		ctx.drawString(("Line: " + line), 11*block, 400);
		ctx.drawString(("Level: " + (line/10)), 11*block, 500);
		ctx.drawString(("Step: " + step), 11*block, 600);
		
		//Down
		for (int i = 0; i < 20; i++){
			for (int j = 0; j < 10; j++){
				ctx.setColor(new Color(ground[i][j][0]));
				ctx.fillRect(j*block, i*block, block, block);
			}
		}
		
		//Image
		ctx.drawImage(image, block*9, block*17, null);
		
		//Figure
		for (int i = 0; i < 4; i++){
			ctx.setColor(colorBlock);
			ctx.fillRect(block*form[i][0], block*form[i][1], block, block);
		}
		
		//Grid
		ctx.setColor(Color.white);
		for (int i = 0; i <= 20; i++) ctx.drawLine(0, block*i, block*10, block*i);
		for (int i = 0; i <= 10; i++) ctx.drawLine(block*i, 0, block*i, block*20);
	}
}