///////////////////////////////////////////
//Author: Oscar Galindo Molina           //
//ID: 80585887                           //
//CS 2302                                //
//Professor: Dr.Olac Fuentes             //
//TA: Daniel Gomez                       //
//Lab 1                                  //
///////////////////////////////////////////
import java.util.*;

public class four_squares 
{
   public static void draw_squares(int n, double x, double y, double rad) 
   {
     if (n>0)
     {
       StdDraw.line(x-rad, y-rad, x-rad, y+rad);
       StdDraw.line(x-rad, y+rad, x+rad, y+rad);
       StdDraw.line(x+rad, y+rad, x+rad, y-rad);
       StdDraw.line(x+rad, y-rad, x-rad, y-rad);

       draw_squares(n-1, x-rad, y-rad, rad/2);
       draw_squares(n-1, x-rad, y+rad, rad/2);
       draw_squares(n-1, x+rad, y-rad, rad/2);
       draw_squares(n-1, x+rad, y+rad, rad/2);

     }            
   }     
   
   public static void main(String[] args) {
      StdDraw.setXscale(0, 2000);
      StdDraw.setYscale(0, 2000);
      StdDraw.setPenColor(StdDraw.BGREEN);
      double coordinate[][] ={{550,1450},{1450,1450},{550,550},{1450,550}};
      //draw_squares(4, 1000, 1000, 500);
      
      //circle(1000,1000,500,1.9,120);//First Assignment Method Calls
      //circle(1000,1000,500,1.125,5);
      //circle(1000,1000,500,1.065,1);
      
      //circleMove(1,1000,1,1.7);//Second Assignment Method Calls
      //circleMove(1,1000,1,1.15);
      //circleMove(1,1000,1,1.05);
      
      //squares(10,0.75,coordinate);//Third Assignment Method Calls
      //squares(10,0.9,coordinate);
      squares(85,0.95,coordinate);
      
      //branches(3,1000,1950,600,1850/3);//Fourth Assignment Method Calls
      //branches(4,1000,1950,600,1850/4);//Each call contains the division of the entire resolution of the screen by the number of levels so that all can be seen in the screen.
      //branches(7,1000,1950,600,1900/7);
      
      //circles(3,1000,1000,500);//Fifth Assignment Method Calls
      //circles(4,1000,1000,500);
      //circles(5,1000,1000,500);
   }
   
   public static void circle (double x, double y, double rad, double ratio, double limit)
   {
     if(rad > limit)//The user provides the minimum radius that is needed for the method to run.
     {
      StdDraw.circle(x, y, rad);  
      circle(x, y, rad/ratio, ratio,limit);
     }
   }
   
   public static void circleMove(double x, double y, double rad, double ratio)
   {
     if(rad < 1000)//This maximum radius is assigned due to the size of the graphical interface.
     {
       StdDraw.circle(x + rad, y, rad);  
       circleMove(x,y,rad*ratio,ratio);
     }
   }
  
   public static void squares(int n, double correction, double[][] coordinates)
   {
     if(n > 0)
     {
       StdDraw.line(coordinates[0][0], coordinates[0][1], coordinates[2][0], coordinates[2][1]);
       StdDraw.line(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1]);
       StdDraw.line(coordinates[3][0], coordinates[3][1], coordinates[2][0], coordinates[2][1]);
       StdDraw.line(coordinates[3][0], coordinates[3][1], coordinates[1][0], coordinates[1][1]);
       double coordinate[][] = {{coordinates[2][0]-((coordinates[2][0]-coordinates[0][0])*correction),coordinates[2][1]+((coordinates[0][1]-coordinates[2][1])*correction)},
                                {coordinates[0][0]+((coordinates[1][0]-coordinates[0][0])*correction),coordinates[0][1]+((coordinates[1][1]-coordinates[0][1])*correction)},
                                {coordinates[3][0]-((coordinates[3][0]-coordinates[2][0])*correction),coordinates[3][1]-((coordinates[3][1]-coordinates[2][1])*correction)},
                                {coordinates[1][0]+((coordinates[3][0]-coordinates[1][0])*correction),coordinates[1][1]-((coordinates[1][1]-coordinates[3][1])*correction)}};
                                //This array is used to generate the coordinates for the next square and then these are used by the recursive call as the new points for the lines to be printed.
                                //The amount of correction in each iteration is determined by the user.
       squares(n-1,correction,coordinate);                 
     }
   }
   
   public static void branches(int n, double x, double y, double correctionX, double correctionY) 
   {
     if(n>0)//Correction among X and Y is used to close the angles and the space that each branch uses.
     {
       StdDraw.line(x,y,x-(0.5*correctionX),y-correctionY);
       branches(n-1,x-(0.5*correctionX),y-correctionY,correctionX*0.5,correctionY);
       StdDraw.line(x,y,x+(correctionX*0.5),y-correctionY);
       branches(n-1,x+(0.5*correctionX),y-correctionY,correctionX*0.5,correctionY);
     }
   }
   
   public static void circles(int n, double x, double y, double rad)
   {
     if(n>0)//Each of the recursive call makes one of the circles in each different position.
     {
       StdDraw.circle(x,y,rad);
       circles(n-1,x,y,rad/3);
       circles(n-1,x-(rad/3)*2,y,rad/3);
       circles(n-1,x+(rad/3)*2,y,rad/3);
       circles(n-1,x,y+(rad/3)*2,rad/3);
       circles(n-1,x,y-(rad/3)*2,rad/3); 
     }
   }
}