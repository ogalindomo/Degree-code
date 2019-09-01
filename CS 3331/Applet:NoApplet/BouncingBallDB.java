import java.awt.Color;
import java.awt.Graphics;
import java.io.*;
import java.applet.*;
import java.util.Random;
public class BouncingBallDB extends DBAnimationApplet {
    private Color color = Color.GREEN;
    private int circles, rectangles;
    private Bounceable ball [];
    private Bounceable rect [];
    private Bounceable first = new Rectangle();
    public void init() {
        delay=10;
        super.init();
        circles = Integer.parseInt(getParameter("circles"));
        rectangles = Integer.parseInt(getParameter("rectangles"));
        ball = new CircleBall[circles]; 
        rect = new Rectangle[rectangles];
        Random rand = new Random();
        for(int i = 0; i < ball.length; i++) 
        {
            ball[i] = new CircleBall();
            int  x = rand.nextInt(dim.width *3/4) + dim.width/4; //500 is the maximum and the 1 is our minimum 
            int  y = rand.nextInt(dim.height *3/4) + dim.height/4;
            int  radius = rand.nextInt(30) + 15;
            int  r = rand.nextInt(255);
            int  g = rand.nextInt(255);
            int  b = rand.nextInt(255);
            int dx = -1*(rand.nextInt(10) +3);
            int dy = -1*(rand.nextInt(10) +3);
            ball[i].set(x, y, new Color(r,g,b), radius, dx, dy);
        }
        for(int i = 0; i < rect.length; i++) 
        {
            rect[i] = new Rectangle();
            int  x = rand.nextInt(dim.width - 150) + dim.width/4; //500 is the maximum and the 1 is our minimum 
            int  y = rand.nextInt(dim.height - 150) + dim.height/4;
            int  radius = rand.nextInt(30) + 15;
            int  r = rand.nextInt(255);
            int  g = rand.nextInt(255);
            int  b = rand.nextInt(255);
            int dx = -1*rand.nextInt(10) +3;
            int dy = -1*rand.nextInt(10) +3;
            rect[i].set(x, y, new Color(r,g,b), radius, dx, dy);
        }
    }
  
    protected void paintFrame(Graphics g) {
        g.setColor(Color.BLACK);
        g.fillRect(0, 0, dim.width, dim.height);
        for(int i = 0; i < ball.length; i++)
        {
            ball[i].appear(g,ball[i].getx(),ball[i].gety());
        }
        for(int i = 0; i < rect.length; i++)
        {
            rect[i].appear(g,rect[i].getx(),rect[i].gety());
        }
        for(int i = 0; i < ball.length; i++)
        {
            ball[i].setx(ball[i].getx() + ball[i].getdx()); 
            ball[i].sety(ball[i].gety() + ball[i].getdy());
        }
        for(int i = 0; i < rect.length; i++)
        {
            rect[i].setx(rect[i].getx() + rect[i].getdx()); 
            rect[i].sety(rect[i].gety() + rect[i].getdy());
        }
        for(int i = 0; i < ball.length; i++)
        {
           if(ball[i].getx() < ball[i].getr() || ball[i].getx() > (dim.width - ball[i].getr()))
           {
               ball[i].setdx(-1*ball[i].getdx());
           }
           if(ball[i].gety() < ball[i].getr() || ball[i].gety() > (dim.height - ball[i].getr()))
           {
               ball[i].setdy(-1*ball[i].getdy());
           }
        }
        for(int i = 0; i < rect.length; i++)
        {
           if(rect[i].getx() < rect[i].getr() || rect[i].getx() > (dim.width - rect[i].getr()))
           {
               rect[i].setdx(-1*rect[i].getdx());
           }
           if(rect[i].gety() < rect[i].getr() || rect[i].gety() > (dim.height - rect[i].getr()))
           {
               rect[i].setdy(-1*rect[i].getdy());
           }
        }
        for(int i = 0; i < ball.length; i++)
        {
          for(int j = i + 1; j < ball.length; j++)
          {
            double distance_between_balls = Math.sqrt(Math.pow(ball[i].getx()-ball[j].getx(),2)+Math.pow(ball[i].gety()-ball[j].gety(),2));
            int radius_added = ball[i].getr() + ball[j].getr();
            if(distance_between_balls <= radius_added)
            {
              ball[i].setdx(-1*ball[i].getdx());
              ball[j].setdx(-1*ball[j].getdx());
              ball[i].setdy(-1*ball[i].getdy());
              ball[j].setdy(-1*ball[j].getdy());
            }
          }
        }
        for(int i = 0; i < rect.length; i++)
        {
          for(int j = i + 1; j < rect.length; j++)
          {
            double distance_between_rect = Math.sqrt(Math.pow(rect[i].getx()-rect[j].getx(),2)+Math.pow(rect[i].gety()-rect[j].gety(),2));
            int radius_added = rect[i].getr() + rect[j].getr();
            if(distance_between_rect <= radius_added)
            {
              rect[i].setdx(-1*rect[i].getdx());
              rect[j].setdx(-1*rect[j].getdx());
              rect[i].setdy(-1*rect[i].getdy());
              rect[j].setdy(-1*rect[j].getdy());
            }
          }
        }
        for(int i = 0; i < ball.length; i++)
        {
          for(int j = 0; j < rect.length; j++)
          {
            double distance_between_balls = Math.sqrt(Math.pow(ball[i].getx()-rect[j].getx(),2)+Math.pow(ball[i].gety()-rect[j].gety(),2));
            int radius_added = ball[i].getr() + rect[j].getr();
            if(distance_between_balls <= radius_added)
            {
              ball[i].setdx(-1*ball[i].getdx());
              rect[j].setdx(-1*rect[j].getdx());
              ball[i].setdy(-1*ball[i].getdy());
              rect[j].setdy(-1*rect[j].getdy());
            }
          }
        }
        delay=10;
    }
}