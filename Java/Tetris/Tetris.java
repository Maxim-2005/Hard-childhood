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
		//x++;
	}
	
	//Drawing graphics
	public void paint(Graphics ctx) {
		super.paint(ctx);
		setBackground(Color.black);
		
		ctx.setColor(Color.white);
		ctx.fillRect(x*block, y*block, 50, 50);
	}
}