import java.awt.*;
public class GrowingShrinkingBalloon extends GrowingBalloon {
/**
* Create a new balloon at the given position and with the given * color. The initial size of the balloon is 0.
*/
public GrowingShrinkingBalloon(int x, int y, Color color) { super(x, y, color);
}
/** Adjusts this balloon’s radius by delta pixels and draws it. */ 

public void draw(Graphics g, int width, int height)
{
   if(radius == 0 || radius < 0 )
      delta = Math.abs(delta);
   if(Math.min(y + radius, height) == height || Math.min(y - radius, 0) == (y-radius) || Math.min(x - radius, 0) == (x-radius) || Math.min((x+radius),width) == width)
      delta = -delta;
   super.draw(g,width,height);
    }
}