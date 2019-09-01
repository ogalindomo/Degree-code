import java.awt.Color;
import java.awt.Graphics;

public class CircleBall extends Shape
{
   public void appear(Graphics g, int x, int y)
   {
        g.setColor(color);
        g.fillOval(x - radius, y - radius, radius * 2, radius * 2); 
   }
}
