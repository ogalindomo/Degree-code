package c4.aspects;
import java.awt.*;
import c4.base.*;
public privileged aspect EndGame {
	private BoardPanel panel;
	pointcut madeMove(C4Dialog l): this(l) && execution(* *.makeMove(..));
	pointcut getPanel (C4Dialog l): this(l) && call(private BoardPanel makeBoardPanel(..));
	pointcut noMore(BoardPanel l): this(l) && execution(int locateSlot(..));	
	ColorPlayer lastPlayer;
	
	before(C4Dialog l): madeMove(l)
	{
		lastPlayer = l.player;
	}
	
	after(C4Dialog l) : madeMove(l)
	{
		if(l.board.isWonBy(lastPlayer))
		{
			System.out.println("Color: "+l.player.color+" Won");
			panel.setDropColor(lastPlayer.color());
			if(lastPlayer.color() == Color.BLUE)
				l.showMessage("Blue Wins");
			else
				l.showMessage("Red Wins");
		}
	}
	
	int around(BoardPanel d): noMore(d)
	{
		if(!d.board.hasWinningRow())
			return proceed(d);
		return -1;
	}
	
	after(C4Dialog l)returning(BoardPanel s): getPanel(l) 
	{
		panel = s;
	}
	
	/*after(BoardPanel l): this(l) && execution(* *.drawPlacedCheckers(..))
	{
		System.out.println("Won: "+l.board.hasWinningRow());
	}*/
	
}
