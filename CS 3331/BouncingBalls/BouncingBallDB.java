import java.awt.Color;
import java.awt.Graphics;
import java.applet.*;
import java.util.Random;
public class BouncingBallDB extends DBAnimationApplet {
    private int circles, rectangles;
    private Bounceable elements [];
    public void init() {
        delay = 10;
        super.init();
        circles = Integer.parseInt(getParameter("circles"));
        rectangles = Integer.parseInt(getParameter("rectangles"));
        elements = new Bounceable [circles + rectangles];
        Random rand = new Random();
        for(int i = 0; i < circles + rectangles; i++) 
        {
            if(i < circles)
                elements[i] = new CircleBall();
            else
                elements[i] = new Rectangle();
            int  x = rand.nextInt(dim.width *3/4) + 250; //500 is the maximum and the 1 is our minimum 
            int  y = rand.nextInt(dim.height *3/4) + 250;
            int  radius = rand.nextInt(30) + 5;
            int  r = rand.nextInt(255);
            int  g = rand.nextInt(255);
            int  b = rand.nextInt(255);
            int dx = (rand.nextInt(10) +3);
            int dy = (rand.nextInt(10) +3);
            elements[i].set(x, y, new Color(r,g,b), radius, dx, dy);
        }
    
    }
  
    protected void paintFrame(Graphics g) {
        g.setColor(Color.BLACK);
        g.fillRect(0, 0, dim.width, dim.height);
        for(int i = 0; i < elements.length; i++)
        {
            elements[i].appear(g,elements[i].getx(),elements[i].gety());
        }
        for(int i = 0; i < elements.length; i++)
        {
            elements[i].setx(); 
            elements[i].sety();
        }
        for(int i = 0; i < elements.length; i++)
        {
           if(elements[i].getx() < elements[i].getr() || elements[i].getx() > (dim.width - elements[i].getr()))
           {
               elements[i].setdx(-1*elements[i].getdx());
           }
           if(elements[i].gety() < elements[i].getr() || elements[i].gety() > (dim.height - elements[i].getr()))
           {
               elements[i].setdy(-1*elements[i].getdy());
           }
        }
        delay=10;
        for(int i = 0; i < elements.length; i++)
        {
          for(int j = i + 1; j < elements.length; j++)
          {
            double distance_between_balls = Math.sqrt(Math.pow(elements[i].getx()-elements[j].getx(),2)+Math.pow(elements[i].gety()-elements[j].gety(),2));
            int radius_added = elements[i].getr() + elements[j].getr();
            if(distance_between_balls <= radius_added)
            {
              elements[i].setdx(-elements[i].getdx());
              elements[j].setdx(-elements[j].getdx());
              elements[i].setdy(-elements[i].getdy());
              elements[j].setdy(-elements[j].getdy());
            }
          }
        }
    }
}