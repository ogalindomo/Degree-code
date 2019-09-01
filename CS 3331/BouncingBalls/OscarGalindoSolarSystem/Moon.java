import java.awt.Color;
import java.awt.Graphics;
public class Moon implements CelestialObject
{
    int r, d, centerX, centerY, angle, change, distancePlanet;
    Color color;
    public Moon(int r, int d, int centerX, int centerY, int angle, Color c, int change)
    {
        this.r = r;
        this.angle = angle;
        distancePlanet = d;
        color = c;
        this.centerX = centerX;
        this.centerY = centerY;
        this.change = change;
    }
    public int getX()
    {
        return centerX;
    }
    public int getY()
    {
        return centerX;
    }
    public void updateAngle()
    {
        angle += change;
        if(angle > 360)
            angle = angle % 360;
    }
    public void setPosition(int x, int y)
    {
        this.centerX = x; 
        this.centerY = y;
    }
    public void appear(Graphics g)
    {
        g.setColor(color);
        g.fillOval(calcX() - r, calcY() - r, r * 2, r * 2); 
    }
    private int calcX()
    {
        return (int) (centerX + distancePlanet * Math.cos(Math.toRadians(angle)));
    }
    private int calcY()
    {
        return (int) (centerY + distancePlanet * Math.sin(Math.toRadians(angle)));
    }
}
