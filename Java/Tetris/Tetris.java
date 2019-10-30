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

public class Tetris extends JPanel {

	//Variables
	protected static int block = 50, x = 0, y=0;
	public int form[][][] = {
		{{1, 2}, {0, 1}, {1, 1}, {2, 1}, {255, 0, 255}}, //I
		{{1, 2}, {0, 1}, {1, 1}, {2, 1}, {255, 0, 255}}, //J
		{{1, 2}, {0, 1}, {1, 1}, {2, 1}, {255, 0, 255}}, //L
		{{1, 2}, {0, 1}, {1, 1}, {2, 1}, {255, 0, 255}}, //O
		{{1, 2}, {0, 1}, {1, 1}, {2, 1}, {255, 0, 255}}, //S
		{{1, 2}, {0, 1}, {1, 1}, {2, 1}, {255, 0, 255}}, //T
		{{1, 2}, {0, 1}, {1, 1}, {2, 1}, {255, 0, 255}}  //Z
	};

	public static void main(String[] args){
		
		//Application window
		JFrame jFrame = new JFrame("Tetris");
		JFrame.setDefaultLookAndFeelDecorated(true);
		jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		jFrame.setSize(block*10, block*20);
		jFrame.setResizable(false);
		jFrame.setLocationRelativeTo(null);	
		jFrame.setVisible(true);
		Tetris tetris = new Tetris();
		jFrame.add(tetris);
		
		//Press key
		jFrame.addKeyListener(new KeyAdapter() {
			public void keyPressed(KeyEvent event) {
				switch(event.getKeyCode()) {
					case 37: x--; break; //Left
					case 38: y--; break; //Down
					case 39: x++; break; //Right
					case 40: y++; break; //Up
				}
			}
		});

		while(true) {
			tetris.game();
			tetris.repaint();
			try {
				Thread.sleep(1);
			} catch (Exception e) {}
		}
	}

	//Logic block
	private void game() {
		//y++;
	}
	
	//Drawing graphics
	public void paint(Graphics ctx) {
		super.paint(ctx);
		setBackground(Color.black);
		
		for (int i = 0; i < 4; i++){
			ctx.setColor(new Color(form[0][4][0], form[0][4][1], form[0][4][2]));
			ctx.fillRect(block*form[0][i][0]+x*block, block*form[0][i][1]+y*block, block, block);
		}
	}
}