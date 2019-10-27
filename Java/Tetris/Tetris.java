/*
 * Tetris
 * Maxim 27.10.2019
 */

import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Tetris extends JPanel {

	//Variables
	protected static int block = 50, x = 10;

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
	
		while(true) {
			tetris.game();
			tetris.repaint();
			try {
				Thread.sleep(125);
			} catch (Exception e) {}
		}
	}

	//Logic block
	private void game() {
		x++;
	}
	
	//Drawing graphics
	public void paint(Graphics ctx) {
		super.paint(ctx);
		setBackground(Color.black);
		
		ctx.setColor(Color.white);
		ctx.fillRect(50, x, 50, 50);
	}
}