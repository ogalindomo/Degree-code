import java.awt.Graphics;
import java.awt.Color;
public class Sun implements CelestialObject
{
   private static Sun sun = new Sun(0,0);
   private int x, y, r;
   private Color color;
   public static Sun getInstance()
   {
       return sun;
   }
   public void appear(Graphics g)
    {
        g.setColor(color);
        g.fillOval(x - r, y - r, r * 2, r * 2); 
    }
   private Sun(int centerX, int centerY)
   {
      x = centerX;
      y = centerY;
      r = 24;
      this.color = new Color(251, 145, 84);
   }
   public void setPosition(int x, int y)
   {
      this.x = x; 
      this.y = y;
   }
   public int getX(){return x;}
   public int getY(){return y;}
}
