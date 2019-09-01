public class heap
{
   public int[] H; 
   
   public heap (int n)
   {
     H = new int[n];  
     H[0] = 0;
   }
   
   public int insert (int k)
   {
     if(H[0] >= H.length-1)
        return -1;
     H[0]++;
     int i = H[0];
     while(i > 1 && k < H[i/2])
     {
       H[i] = H[i/2];
       i = i/2;
     }
     H[i] = k;
     return i;
   }
   
   public int extractMin()
   {
     if(H[0] <= 0)
        return -1;
     int minVal = H[1];  
     H[1] = H[H[0]];  
     H[0]--;  
     int i = 1;
     int min = 1;
     int temp;
     while(true)
     {
       if(2*i <= H[0] && H[min] > H[2*i])
          min = 2*i;
       if((2*i)+1 <= H[0] && H[min] > H[(2*i)+1])
          min = 2*i+1;
       if(i == min)
          break;
       temp = H[i];
       H[i] = H[min];
       H[min] = temp;
       i = min;
     }
     return minVal;
   }
}
