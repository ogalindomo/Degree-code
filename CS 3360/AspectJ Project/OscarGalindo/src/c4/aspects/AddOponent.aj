package c4.aspects;
import java.awt.Color;
import c4.base.BoardPanel;
import c4.base.C4Dialog;
import c4.base.ColorPlayer;
public privileged aspect AddOponent {
	private ColorPlayer C4Dialog.oponent = new ColorPlayer("Red", Color.RED);
	private ColorPlayer C4Dialog.original;
	private BoardPanel panel;
	
	pointcut getPanel (C4Dialog l): this(l) && call(private BoardPanel makeBoardPanel(..));
	pointcut capturePlayer (C4Dialog l): this(l) && call (* *.configureUI(..));
	pointcut madeMove (C4Dialog d) : this(d) && call(* *.dropInSlot(..));
	pointcut drawDroppable(BoardPanel l):  target(l) && call (* *.drawDroppableCheckers(..));
	pointcut new_game (C4Dialog l): target(l) && call (* *.startNewGame(..));
	
	after(C4Dialog d): madeMove(d)
	{
		if(panel.dropColor == Color.BLUE)
		{
			d.msgBar.setText("Blue' Turn");
			d.player = d.original;
		}
		else if(panel.dropColor == Color.RED)
		{
			d.msgBar.setText("Red' Turn");
			d.player = d.oponent;
		}
	}

	before(C4Dialog l):capturePlayer(l)
	{
		l.original = l.player;
	}
	
	after(C4Dialog l)returning(BoardPanel s): getPanel(l) 
	{
		panel = s;
	}
	
	after(C4Dialog d): new_game(d)
	{
		panel.setDropColor(Color.BLUE);
		d.msgBar.setText("Blue' Turn");
		d.player = d.original;
	}
	
	before(c4.base.BoardPanel.ClickListener l): target(l) && call(* *.*(..))
	{
		if(panel.dropColor == Color.BLUE)
    		panel.setDropColor(Color.RED);
    	else if(panel.dropColor == Color.RED)
    		panel.setDropColor(Color.BLUE);
	}
	
	/*after(BoardPanel l): drawDroppable(l){
		if(l.dropColor == Color.BLUE)
			l.setDropColor(Color.RED);
		else if(l.dropColor == Color.RED)
			l.setDropColor(Color.BLUE);
	}*/
}
