import java.awt.*;
public class GrowingBalloon implements Balloon{
/** Coordinates of this balloon. */ protected int x, y;
/** Current radius of this balloon. */ protected int radius = 0;
/** Growing rate of this balloon’s radius. The radius grows * delta pixels every time the draw method is called. */
protected int delta = 2;
/** Color of this balloon. */ protected Color color;
/** Create a new balloon at the given position and with the given color. */ public GrowingBalloon(int x, int y, Color color) {
this.x = x;
this.y = y; this.color = color;
}
/** Increases the balloon’s radius by delta pixels and draws it using * the given the graphics. */
public void draw(Graphics g, int width, int height)
{
    g.setColor(Color.BLACK);
    g.fillRect(0, 0, width, height);
    radius += delta;
    g.setColor(this.color);
    g.fillOval(x, y, radius, radius);
}
}