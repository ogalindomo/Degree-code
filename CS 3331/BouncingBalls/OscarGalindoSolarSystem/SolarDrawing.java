import java.awt.*;
import javax.swing.*;
import java.awt.Graphics;
import java.util.Random;
/**
 * Class SolarSystem - write a description of the class here
 * 
 * @author (your name) 
 * @version (a version number)
 */
public class SolarDrawing extends DBAnimationApplet
{
    // instance variables - replace the example below with your own
    private int planets;
    private CelestialObject spheres [];
    public void init(){
        delay = 10;
        super.init();
        planets = Integer.parseInt(getParameter("planets"));
        spheres = new CelestialObject[planets + 1];
        spheres[0] = Sun.getInstance();
        spheres[0].setPosition(dim.width/2, dim.height/2);
        Random rand = new Random();
        for(int i = 1; i < spheres.length; i++)
        {
            int radius = rand.nextInt(20) +9;
            int d = rand.nextInt(dim.height / 2 - 20) + 50;
            int r = rand.nextInt(255);
            int g = rand.nextInt(255);
            int b = rand.nextInt(255);
            int angle = rand.nextInt(360) + 1;
            int change = rand.nextInt(2) + 1;
            int moonNumber = rand.nextInt(5) + 0;
            spheres[i] = new Planet(radius,d, dim.width/2, dim.height/2, angle, new Color(r,g,b), change, moonNumber);
        }
    }

    protected void paintFrame(Graphics g)
    {
        g.setColor(Color.BLACK);
        g.fillRect(0, 0, dim.width, dim.height);
        spheres[0].appear(g);
        for(int i = 1; i < spheres.length; i++)
        {
            Planet prov = (Planet)spheres[i];
            prov.updateAngle();
            spheres[i].appear(g);
        }
    }
}
