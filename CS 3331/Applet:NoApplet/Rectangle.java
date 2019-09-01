import java.awt.Color;
import java.awt.Graphics;

public class Rectangle extends Shape
{
   public void appear(Graphics g, int x, int y)
   {
        g.setColor(color);
        g.fillRect(x - radius, y - radius, radius * 2, radius * 3 /2); 
   }  
}
