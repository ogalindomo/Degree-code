import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;

import javax.swing.Timer;

/**
 *  Sample NoApplet to display a text banner that moves horizontally from
 *  right to left. When the banner moves completely off the left end
 *  of the viewing area, it reappears from the right.
 *  See Section 5.5.2 on pages 188-193.
 */
@SuppressWarnings("serial")
public class ScrollingBanner extends NoApplet {

    /** Banner text. */
    private String text;
    
    /** Font to display the banner. */
    private Font font = new Font("Sans serif", Font.BOLD, 24);
    
    /** Dimension of the screen. */
    protected Dimension dim;

    /** Current position of the banner text. */
    private int x, y;

    /** Animation speed. A new frame is painted as every <code>delay</code>
     * milliseconds. */
    private int delay = 10;

    /** Animation timer to refresh the screen periodically. */
    private Timer timer;

    /** Distance of the banner to be moved upon screen refreshing. */
    private int offset = 1;

    public ScrollingBanner(String[] args) {
    	super(args);
    }
    
    /** Initialize the data structure including the animation timer. */
    public void init() {
        // get parameters "delay" and "text"
        String att = getParameter("delay");
        if (att != null) {
            delay = Integer.parseInt(att);
        }
        att = getParameter("text");
        if (att != null) {
            text = att;
        } else {
            text = "Go Miners!";
        }

        // set initial position of the text
        dim = getSize();
        x = dim.width;
        y = font.getSize();

        // start the animation timer
        timer = new Timer(delay, e -> repaint());
    }

    /** Move the banner text <code>offset</code> pixels to the left. */ 
    @Override
    public void paint(Graphics g) {
    	super.paint(g);
        
        // get the font metrics to determine the length of the text
        g.setFont(font);
        FontMetrics fm = g.getFontMetrics();
        int height = fm.stringHeight(text);

        // adjust the position of text from the previous frame
        y -= offset;

        // if the text is completely off to the left end
        // move the position back to the right end
        if ( y < -height) {
            x = dim.width;
        }

        // set the pen color and draw the background
        g.setColor(Color.black);
        g.fillRect(0,0,dim.width, dim.height);

        // set the pen color, then draw the text
        g.setColor(Color.green);
        g.drawString(text, x, y);
    }

    /** Start the animation. */
    @Override
    public void start() {
        timer.start();
    }

    /** Stop the animation. */
    @Override
    public void stop() {
        timer.stop();
    }
    
    public static void main(String[] args) {
    	new ScrollingBanner(new String[] {"width=250", "height=50"}).run();
    }
}