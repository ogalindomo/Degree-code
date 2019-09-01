import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Image;

public abstract class DBAnimationApplet extends AnimationApplet {
	   private Image image;
	   private Graphics offScreen;
	   protected Dimension dim;
	   
	   
	   public void init() {
		   dim = getSize();
		   image = createImage(dim.width, dim.height);
		   offScreen = image.getGraphics();
	      super.init();

	   }

	   public final void update(Graphics g) {
	       paintFrame(offScreen);
	       g.drawImage(image, 0, 0, this);
	   }

	   public final void paint(Graphics g) {
	       update(g); 
	   }

	   protected abstract void paintFrame(Graphics g);
	}