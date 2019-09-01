import java.awt.Color;
import java.awt.Graphics;
public interface Bounceable
{
   public void appear(Graphics g, int x, int y);
   public void set(int coordinatex, int coordinatey, Color paint, int r, int dx, int dy);
   public int getx();
   public int gety();
   public int getr();
   public int getdx();
   public int getdy();
   public void setx(int newx);
   public void sety(int newy);
   public void setdx(int newdx);
   public void setdy(int newdy);
}
