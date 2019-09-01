package c4.aspects;
import  c4.base.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public privileged aspect pressDisc {
	pointcut letsee (BoardPanel d) : this(d) && execution(* *.locateSlot(..));
	pointcut capturePlayer (C4Dialog l): this(l) && call (* *.configureUI(..));
	pointcut getPanel (C4Dialog l): this(l) && call(private BoardPanel makeBoardPanel(..));
	pointcut drawing (BoardPanel l): this(l) && call(private void drawChecker(Graphics, Color, int, int, int));
	private int pressedSlot = -1;
	
	after(C4Dialog l)returning(BoardPanel panel): getPanel(l) 
	{
		panel.addMouseListener(new MouseAdapter() {
			public void mousePressed(MouseEvent e)
			{
				pressedSlot = panel.locateSlot(e.getX(), e.getY());
				//System.out.println("Pressed slot: "+pressedSlot);
				panel.repaint();
			}
			
			public void mouseReleased(MouseEvent e)
			{
				pressedSlot = -1;
				panel.repaint();
			}
		});
	}

	void around(BoardPanel l, Graphics g, Color color, int slot, int y, int margin): drawing(l) && args(g,color,slot,y,margin) 
	{
		if(slot == pressedSlot && y == -1 && l.board.isSlotOpen(pressedSlot))
			proceed(l,g,color,slot,y, margin+5);
		else
			proceed(l,g,color,slot,y,margin);
	}
}
