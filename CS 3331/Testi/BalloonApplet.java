import java.awt.*; import javax.swing.Timer;
public class BalloonApplet extends java.applet.Applet {
/** Dimension of this applet. */ protected Dimension dim;
/** Animation timer. */ private Timer timer;
/** Balloon to draw and animate. */ private Balloon balloon;
/** Overridden here to create the animation timer and a balloon. */ public void init() {
  dim = getSize();
balloon = createBalloon();
timer = new Timer(5, e -> repaint());
}
/** Create a balloon to animate. */ protected Balloon createBalloon() {
return new GrowingShrinkingBalloon(dim.width/2, dim.height/2, Color.GREEN); }
/** Overridden here to draw the balloon. */ public void paint(Graphics g) {
balloon.draw(g, dim.width, dim.height); }
/** Overridden here to start the animation timer. */ public void start() {
        timer.start();
    }
/** Overridden here to stop the animation timer. */ public void stop() {
        timer.stop();
    }
    public Balloon getBalloon()
    {
        
        return balloon; 
    }
}
