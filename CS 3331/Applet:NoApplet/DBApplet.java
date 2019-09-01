import java.awt.*;

/** 
 * Double-buffered scrolling banner. See Section 5.5.3 on page 194.
 */
@SuppressWarnings("serial")
public class DBApplet extends NoApplet

{
  
    private Image image;
    private Graphics offscreen;
    protected Dimension dim;
    
    public DBApplet(String[] args) {
        super(args);
    }
    
    @Override
    public void update(Graphics g) {
        if (image == null) {
            image = createImage(dim.width, dim.height);
            offscreen = image.getGraphics();
        }
        paint(offscreen);
        g.drawImage(image, 0, 0, this);
    }

    @Override
    public void paint(Graphics g) {
        update(g);
    }
}
