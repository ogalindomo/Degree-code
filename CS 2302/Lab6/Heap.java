public class Heap
{
    public HeapNode[] H;
    public int size;
    public Heap(int capacity)
    {
      H = new HeapNode[capacity+1];
      this.size = 0;
    }
    
    public void insert(HeapNode node)
    {
      if(size >= H.length-1)
        System.out.println("Full");
      size++;
      int i = size;
      while(i > 1 && (node.similarity*-1) < (H[i/2].similarity*-1))
      {
        H[i] = H[i/2];
        i = i/2;
      }
      H[i] = node;
    }
    
    public HeapNode extractMin()
    {
      if(size <= 0)
        System.out.println("Not possible to extract.");
      HeapNode minVal = H[1];  
      H[1] = H[size];  
      size--;  
      int i = 1;
      int min = 1;
      HeapNode temp;
      while(true)
      {
        if(2*i <= size && (H[min].similarity*-1) > (H[2*i].similarity)*-1)
           min = 2*i;
        if((2*i)+1 <= size && (H[min].similarity*-1) > (H[(2*i)+1].similarity*-1))
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
