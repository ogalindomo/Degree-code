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
public class Clock extends NoApplet {
    
    /** Refresh display once per second. */
    private Timer timer = new Timer(1000, e -> repaint());
    
    /** Font to display the time. */
    private Font font = new Font("Monospaced", Font.BOLD, 41);
    
    /** Color to display the time. */
    private Color color = new Color(231,222,120);
    
    TimeDisplay clk = new DigitalClock();

    public Clock(String[] args) {
    	super(args);
    }

    /** Start the timer. */
    @Override
    public void start() {
        timer.start();
    }

    /** Stop the timer to prevent from wasting CPU time. */
    @Override
    public void stop() {
        timer.stop();
    }

    /** Display the current time. */ 
    @Override
    public void paint(Graphics g) {
        Color painting = new Color(12,160, 209);
        //TimeDisplay clk2 = new AnalogClock();
        //clk2.paint(g,painting);
    	clk.paint(g,painting);
        // Calendar calendar = Calendar.getInstance();
        // int hours = calendar.get(Calendar.HOUR_OF_DAY);
        // int minutes = calendar.get(Calendar.MINUTE);
        // int seconds = calendar.get(Calendar.SECOND);
        // g.setFont(font);
        // g.setColor(color);
        // g.drawString(String.format("%d:%02d:%02d", hours, minutes, seconds), 10, 60);
    }
    public static void main(String[] args) {
    	new Clock(new String[] {"width=250", "height=100"}).run();
    }
}