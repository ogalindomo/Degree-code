public class Backtracking
{
   public static void main (String [] args)
   {
     int num [] = {-1,25,1,27,23,24,120,25,1,2,24,5,7,8,9,10,11,12,13,14,15,16,17,18,19,31,32,39,60,61,62,63,64,65,66,
         -2,65,1023,270,213,224,1206,103,99};
     //Should partition indeces 0 and 1 together and 2 so that 4 = 4
     //Elements in partitions should not exist in the complement parititon.
     long start = System.nanoTime();
     System.out.println(possible(num,halfSum(num),0)); 
     long end   = System.nanoTime();
     long total = end - start;
     System.out.println("Time: "+total);
   }
   
   public static double halfSum(int num [])
   {
     double sum = 0;
     for(int i = 0; i < num.length; i++)
      sum += num[i];
     return sum/2;
   }
   
   public static boolean possible(int num [], double sum, int index)
   {
     System.out.println(sum);
     if(index >= num.length | sum < 0)
       return false;
     if(sum == 0 && num.length != 0 && num.length != 1)
       return true;
     if(possible(num, sum-num[index],index+1))
     {
       System.out.println("Take: "+num[index]);
       return true;
     }
     return possible(num,sum,index+1);
   }
}
