import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.util.Calendar;
import javax.swing.Timer;


/**
 *  Sample NoApplet to display the current time continuously.
 *  See Section 4.7 on pages 149-154.
 */
@SuppressWarnings("serial")
public class CuckooDigitalClock extends Clock {
    public CuckooDigitalClock(String[] args) {
    	super(args);
    }
    @Override
    public void paint(Graphics g) {
    	super.paint(g);
        Calendar calendar = Calendar.getInstance();
        int hours = calendar.get(Calendar.HOUR_OF_DAY);
        int minutes = calendar.get(Calendar.MINUTE);
        int seconds = calendar.get(Calendar.SECOND);
        if(minutes == 0 & seconds == 0)
        {
          play(getCodeBase(),"cuckoo.au"); 
        }
        g.drawString(String.format("%d:%02d:%02d", hours, minutes, seconds), 10, 60);
    }
}