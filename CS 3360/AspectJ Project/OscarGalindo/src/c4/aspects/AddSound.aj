package c4.aspects;
import c4.base.*;
import java.io.*;
import javax.sound.sampled.*;
import java.awt.Color;

public privileged aspect AddSound {
	pointcut somebodyWon (BoardPanel d) : this(d) && execution(* *.drawPlacedCheckers(..));
	private BoardPanel panel;
	private boolean playedWin = false;
	pointcut getPanel (C4Dialog l): this(l) && call(private BoardPanel makeBoardPanel(..));
	pointcut letsee(BoardPanel l): this(l) && execution(int locateSlot(..));
	
	after(C4Dialog l)returning(BoardPanel s): getPanel(l) 
	{
		panel = s;		
	}
	
	before(c4.base.BoardPanel.ClickListener l): target(l) && call(* *.*(..))
	{
		if(panel.dropColor == Color.BLUE && !panel.board.hasWinningRow())
    		placedDisk("Blue");
    	else if(panel.dropColor == Color.RED && !panel.board.hasWinningRow())
    		placedDisk("Red");
	}
	
	after(C4Dialog l): this(l) && execution(* *.newButtonClicked(..))
	{
		playedWin = false;
	}
	
	after (BoardPanel d) : somebodyWon(d)
	{
		if(d.board.hasWinningRow() && !playedWin)
		{
			placedDisk("Win");
			playedWin = true;
			//won = true;
		}
	}
	
	private void placedDisk(String s)
	{
		try
		{
			InputStream pathSoundFile;
			if(s.equals("Blue"))
				pathSoundFile =  getClass().getResourceAsStream("diskplacement.wav");//new FileInputStream("/Users/oscargalindo/eclipse-workspace/C4Aspect/src/c4/aspects/");
			else if(s.equals("Red"))
				pathSoundFile =  getClass().getResourceAsStream("Button.wav");//"Button.wav");//new FileInputStream("/Users/oscargalindo/eclipse-workspace/C4Aspect/src/c4/aspects/Button.wav");
			else
				pathSoundFile =  getClass().getResourceAsStream("bellringing.wav");//new FileInputStream("/Users/oscargalindo/eclipse-workspace/C4Aspect/src/c4/aspects/bellringing.wav");
			playSound(pathSoundFile);
		}
		catch (Exception e)
		{
			System.out.println("Audio file not found.");
		}
	}
	
	public void playSound(InputStream access)
    {
          try{
              InputStream bufferedIn = new BufferedInputStream(access);
              AudioInputStream audioIn = AudioSystem.getAudioInputStream(bufferedIn);
              Clip clip = AudioSystem.getClip();
              clip.open(audioIn);
              clip.start(); 
            }
          catch(UnsupportedAudioFileException | IOException | LineUnavailableException e1){
              System.out.println("Selected Audio File is not compatible.");};
    }
}