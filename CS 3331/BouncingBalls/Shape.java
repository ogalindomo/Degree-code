 

import java.awt.Color;
import java.awt.Graphics;
public abstract class Shape implements Bounceable
{
   protected int x, y, dx, dy;
   protected Color color;
   protected int radius;
   public void set(int coordinatex, int coordinatey, Color paint, int r, int changex, int changey)
   {
       x = coordinatex;
       y = coordinatey;
       color = paint;
       radius = r;
       dx = changex;
       dy = changey;
   }
   public int getx()
   {
       return x;
   }
   public int gety()
   {
       return y;
   }
   public int getr()
   {
       return radius;
   }
   public int getdx()
   {
       return dx;
   }
   public int getdy()
   {
       return dy;
   }
   public void setx()
   {
       x = x + dx; 
   }
   public void sety()
   {
       y = y + dy; 
   }
   public void setdx(int newdx)
   {
      dx = newdx; 
   }
   public void setdy(int newdy)
   {
      dy = newdy; 
   }
}
