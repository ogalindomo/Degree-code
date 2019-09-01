import java.awt.*;
import javax.swing.*;
import java.applet.*;
public class AnimationApplet extends java.applet.Applet {

	protected Timer timer = null;  
	protected int delay;
	
	public void init() {
		timer = new Timer(delay, e -> repaint());
	}
	public void start() {
		timer.start();
	}


	public void stop() {
		timer.stop();
	}

	public void paint(Graphics g) {
		// <paint the current frame>
	}
	// <other methods and fields>} 
}