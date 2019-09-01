import java.awt.Graphics;
import java.awt.Color;
import java.lang.Math;
import java.awt.Graphics2D;
import java.awt.geom.Ellipse2D;
import java.util.Random;
public class Planet implements CelestialObject
{
    private int x, y, r, distanceSun, angle, change;
    private int centerX, centerY;
    private Color color;
    private Moon moon[];
    public Planet(int r, int d, int centerX, int centerY, int angle, Color c, int change, int numberOfMoons)
    {
       this.r = r;
       this.angle = angle;
       distanceSun = d;
       color = c;
       this.centerX = centerX;
       this.centerY = centerY;
       this.change = change;
       setMoons(numberOfMoons);
    }
    public void appear(Graphics g)
    {
        g.setColor(color);
        g.fillOval(calcX() - r, calcY() - r, r * 2, r * 2); 
        g.setColor(Color.WHITE);
        g.drawOval(centerX - distanceSun, centerY - distanceSun, distanceSun * 2, distanceSun * 2); 
        for(int i = 0; i < moon.length; i++)
        {
           moon[i].updateAngle();
           moon[i].setPosition(calcX(), calcY());
           moon[i].appear(g); 
        }
    }
    public void setPosition(int x, int y)
    {
        this.x = x;
        this.y = y;
    }
    public void updateAngle()
    {
        angle += change;
        if(angle > 360)
            angle = angle % 360;
    }
    public void setMoons(int numberOfMoons)
    {
        moon = new Moon[numberOfMoons];
        Random rand = new Random();
        for(int i = 0; i < moon.length; i++)
        {
            int d = rand.nextInt(this.r + 6) + (this.r +2);
            int r = rand.nextInt(5) + 2;
            int angle = rand.nextInt(360) + 1;
            int change = rand.nextInt(6) + 3;
            moon[i] = new Moon(r, d, calcX(), calcY(), angle, Color.WHITE, change);
        }
    }
    private int calcX()
    {
        return (int) (centerX + distanceSun * Math.cos(Math.toRadians(angle)));
    }
    private int calcY()
    {
        return (int) (centerY + distanceSun * Math.sin(Math.toRadians(angle)));
    }
    public int getX(){return x;}
    public int getY(){return y;}
}
