import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.FontMetrics;
import java.awt.Graphics;

import javax.swing.Timer;

public class ScrollingBanner3 extends ScrollingBanner
{
    private int x, y;
    private int offset = -1;
    private Font font = new Font("Sans serif", Font.BOLD, 24);
    private int delay = 10;
    private String text;
    private Timer timer;
    public ScrollingBanner3(String[] args) {
        super(args);
    }
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
    @Override
    public void paint(Graphics g) {
        super.paint(g);
        g.setFont(font);
        FontMetrics fm = g.getFontMetrics();
        int length = fm.stringWidth(text);
        // get the font metrics to determine the length of the text
        // adjust the position of text from the previous frame
        //int length = fm.stringWidth(text);
        y += offset;

        // if the text is completely off to the left end
        // move the position back to the right end
        if (y < - length){
            y = dim.height;
        }
        
        g.setColor(Color.black);
        g.fillRect(0,0,dim.width, dim.height);

        // set the pen color, then draw the text
        g.setColor(Color.green);
        g.drawString(text, x, y);
        // set the pen color and draw the background
    }
    public static void main(String[] args) {
    	new ScrollingBanner3(new String[] {"width=250", "height=50"}).run();
    }
}
