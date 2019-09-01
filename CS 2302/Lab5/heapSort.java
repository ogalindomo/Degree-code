public class heapSort
{
  public static void main(String [] args)
  {
    heap H = new heap(50);
    int x_max =100;
    int y_max =100;
    StdDraw.setXscale(0, 200);
    StdDraw.setYscale(-120, 200);
    StdDraw.setPenColor(StdDraw.BLACK);  
    
    int [] S = {12,25,5,29,20,1,4,15,28,100};
    int [] S1 ={8, 9, 11, 4, 7,12, 13, 17, 24, 15, 27, 28, 30, 33, 34,37, 40, 42, 50, 16,100,200,300,-10,20,19 };
    int [] S2 = {10, 15, 4, 8 ,9, 5, 2, 3, 7, 12, 18, 1,24, 60 ,6,78,115,31,76,148,23,-15,-20,-30,-64,-128,-32,1000,320,-10000};
    int [] S3 = {10, 15, 4, 8 ,9, 5, 2, 3, 7, 12, 18, 1,24, 60 ,6,78,115,31,76,148,23,-15,-20,-30,-64,-128,-32,1000,320,-10000, 34,56,61,64,90,83,85,45,67,34};
    
    long start = System.nanoTime();
    draw_heap(H,15,180,0);
    for(int i = 0, y = 155; i < S.length; i++,y -= 25)
    {
      H.insert(S[i]);
      draw_heap(H,15,y,0);
    }
    long end   = System.nanoTime();
    long total = end - start;
    System.out.println(total);
  }
   
  public static void draw_heap(heap newHeap, double x, double y, int index)
  {
    if(newHeap == null || index > newHeap.H[0])
       return;
    double xc = ((2*x)+15)/2;
    double yc = ((2*y)+15)/2;
    
    if(index <= newHeap.H[0])
    {
      StdDraw.line(x,y,x, y+15);
      StdDraw.line(x,y,x+15,y);
      StdDraw.line(x+15,y,x+15,y+15);
      StdDraw.line(x,y+15,x+15,y+15);
      StdDraw.text(xc,yc,Integer.toString(newHeap.H[index]));
    }
    draw_heap(newHeap,x+15,y, index+1);
  }
}
