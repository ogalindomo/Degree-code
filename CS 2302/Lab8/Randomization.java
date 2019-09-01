import java.util.*;
import java.lang.Math;
import java.util.Random;
public class Randomization
{
  public static void main(String [] args)
  {
    long start = System.nanoTime();
    System.out.println(compare(-1*Math.PI, Math.PI));
    long end   = System.nanoTime();
    long total = end - start;
    System.out.println("Time: "+total);
    System.out.println(compare2(-1*Math.PI, Math.PI));
    System.out.println(compare3(-1*Math.PI, Math.PI));
  }
  
  public static boolean compare(double left, double right)// tan is equal to sin/cos
  {
    Random rand = new Random();
    for(int i = 0; i < 10000000; i++)
    {
      double test = left + new Random().nextDouble()*(right-left);
      if(Math.abs(f(test) - g(test)) > 0.000001) 
      {
        return false;  
      }
    }  
    return true;  
  }
  
  public static boolean compare2(double left, double right)//cos and cos(-x) are equal
  {
    Random rand = new Random();
    for(int i = 0; i < 1000000; i++)
    {
      double test = left + new Random().nextDouble()*(right-left);
      if(Math.abs(d(test) - l(test)) > 0.000001) 
      {
        return false;  
      }
    }  
    return true;  
  }
  
  public static boolean compare3(double left, double right)//sin(2X) = 2sin(X)cos(X)
  {
    Random rand = new Random();
    for(int i = 0; i < 1000000; i++)
    {
      double test = left + new Random().nextDouble()*(right-left);
      if(Math.abs(t(test) - p(test)) > 0.000001) 
      {
        return false;  
      }
    }  
    return true;  
  }
  
  public static double f(double theta)
  {
    return Math.sin(theta)/Math.cos(theta);  
  }
  
  public static double g(double theta)
  {
    return Math.tan(theta);
  }
  
  public static double l(double theta)
  {
    return Math.cos(-1*theta); 
  }
  
  public static double d(double theta)
  {
    return Math.cos(theta); 
  }
  
  public static double p(double theta)
  {
    return 2*Math.sin(theta)*Math.cos(theta); 
  }
 
  public static double t(double theta)
  {
    return Math.sin(2*theta); 
  }
}