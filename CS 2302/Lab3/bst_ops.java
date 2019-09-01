import java.util.Scanner;
import java.util.Stack;
public class bst_ops{   
    
   public static bstNode insert(bstNode T, int i){
      if (T==null)
         T = new bstNode(i);
      else
         if (i<T.item)
            T.left = insert(T.left,i);
         else 
            T.right = insert(T.right,i);
      return T;
   }
    
   public static bstNode search(bstNode T, int i){
      if (T==null || T.item== i)
         return T;
      if (i<T.item)
         return search(T.left,i);
      else
         return search (T.right,i);
   }
   
   public static bstNode min(bstNode T){
      if (T.left ==null)
         return T;
      return min(T.left);
   }
   
   public static int height (bstNode T){
      if (T==null)
         return -1;
      int hl = height(T.left);
      int hr = height(T.right);
      if(hl>hr)
         return 1+hl;
      return 1+hr;
   }
   
   public static bstNode delete(bstNode T, int i){
      if (T == null)
         return null;
      if (i<T.item)
         T.left=delete(T.left,i);
      else
         if (i>T.item)
            T.right=delete(T.right,i);
         else
          // i == T.item
            if (T.left == null && T.right == null)
               T =  null;
            else
               if (T.left == null && T.right != null)
                  T = T.right;
               else
                  if (T.left != null && T.right == null)
                     T = T.left;
                  else{
                     bstNode succ = min(T.right);
                     T.item = succ.item;
                     T.right = delete(T.right, succ.item);
                  }
      return T;
   }
 
   public static void inOrder(bstNode T){
      if (T!=null){
         inOrder(T.left);
         System.out.print(T.item+" ");
         inOrder(T.right);
      }
   }
   
    public static void draw_tree(bstNode T, double x0, double x1, double y, double y_inc) {
      if(T ==null)
         return;
      double xm = (x0+x1)/2;
      double yn = y-y_inc;
      if(T.left!=null){
         StdDraw.line(xm,y,(x0+xm)/2,yn);
         draw_tree(T.left,x0,xm,yn, y_inc);
      }
      if (T.right!=null){
         StdDraw.line(xm,y,(x1+xm)/2,yn);
         draw_tree(T.right,xm,x1,yn, y_inc);
      }   
      StdDraw.setPenColor(StdDraw.WHITE);
      StdDraw.filledCircle(xm,y, 3);
      StdDraw.setPenColor(StdDraw.BLACK);
      StdDraw.circle(xm,y, 3);
      StdDraw.text(xm,y,Integer.toString(T.item));
   }
  
   public static void pause(){
      Scanner s=new Scanner(System.in);
      System.out.println("Press enter to continue.....");
      s.nextLine();   
      StdDraw.clear();
   }
    
   public static void main(String[] args)   {
      int x_max =100;
      int y_max =100;
      StdDraw.setXscale(0, x_max);
      StdDraw.setYscale(0, y_max);
      StdDraw.setPenColor(StdDraw.BLACK);   
      int [] A = {10, 15, 4, 8 ,9, 5, 2, 3, 7, 12, 18, 1};
      //int [] C = {10, 15, 4, 8 ,9, 5, 2, 3, 7, 12, 18, 1,24, 60 ,6, 78,115,31,76,148,23,-15};
      //int [] D = {10, 15, 4, 8 ,9, 5, 2, 3, 7, 12, 18, 1,24, 60 ,6, 78,115,31,76,148,23,-15,-20,-30,-64,-128,-32
                  //,1000,320,-10000};
      //int [] F = {10, 15, 4, 8 ,9, 5, 2, 3, 7, 12, 18, 1,24, 60 ,6, 78,115,31,76,148,23,-15,-20,-30,-64,-128,-32
                  //,1000,320,-10000, 34,56,61,64,90,83,85,45,67,34};

      bstNode B=null;
      bstNode initial = balanced(B,A);
      long start = System.nanoTime();
      System.out.println(searchIterative(initial,88));
      long end   = System.nanoTime();
      long total = end - start;
      System.out.println(total);
      
      int read [] = toArray(initial);
   }  
   
   /////////////////////////Code Added////////////////////////////////////
   public static void inOrderStacks(bstNode root)//Problem 1
   {
     Stack container = new Stack();
     bstNode holder = root;
     if(root == null)
        return; 
        
     while(holder != null)
     {
       container.push(holder);
       holder = holder.left;
     }
     
     while(!(container.isEmpty()))
     {
       holder = (bstNode)container.pop();
       
       if(holder.right != null)
       {
         holder = holder.right;
         while(holder != null)
         {
           container.push(holder);
           holder = holder.left;   
         }
       }
     }
   }
   
   public static bstNode searchIterative(bstNode root, int i)//Problem 2
   {
     bstNode reading = root;
     if(reading != null)
     {
       while(reading != null && reading.item != i)
       {
         if(reading.item < i)
           reading = reading.right;
         else if(reading.item > i)
           reading = reading.left; 
       }
       if(reading != null && reading.item == i)
        return reading;
     }
     return null;  
   }
   
   public static bstNode balanced (bstNode root, int [] num)//Problem 3
   {
      int index = 0;
      if(root == null)
      {
        root = new bstNode(num[0]);
        index++;
      }
      
      bstNode pointer = root;
      while(index != num.length)//To end the iteration index reaches the end of the array.
      {
        if(pointer.item < num[index] && pointer.right != null)
          pointer = pointer.right;
        else if(pointer.item > num[index] && pointer.left != null)
          pointer = pointer.left;
        else if(pointer.item < num[index] && pointer.right == null)
        {
          pointer.right = new bstNode(num[index]);
          pointer = root;
          index ++;
        }
        else
        {
          pointer.left = new bstNode(num[index]);
          pointer = root;
          index++;
        }
      }
      return root; 
   }
   
   public static int[] toArray(bstNode holder)//Problem 4
   {
     int[] orderedSet = new int[countNodes(holder)];//Knowing how many elements are used allows the array to be created
     int i = 0;//Index used for accessing the positions of the array
     Stack container = new Stack();//Stacks are used to facilitate the addition of terms to the array
     if(holder == null)
        return orderedSet; 
        
     while(holder != null)
     {
       container.push(holder);
       holder = holder.left;
     }
     
     while(!(container.isEmpty()))
     {
       holder = (bstNode)container.pop();
       orderedSet[i] = holder.item;//Here the array receives the value of whatever is being pop.
       if(holder.right != null)
       {
         holder = holder.right;
         while(holder != null)
         {
           container.push(holder);
           holder = holder.left;   
         }
       }
       i++;
     }
     return orderedSet;
   }
   
   public static void printNodesDepth(bstNode root)//Problem 5
   {
     int heightNum = height(root);
     for(int i = 0; i <= heightNum ; i++)
     {
       System.out.print("Nodes at level "+(i+1)+" are: ");
       printAtDepth(root, i);
       System.out.println(" ");
     }
   }
    
   public static int countNodes(bstNode root)//Addition to problem 4
   {
     if(root == null)
        return 0;
     else 
        return countNodes(root.left)+1+countNodes(root.right); 
   }
   
   public static void printAtDepth(bstNode root, int i)//Addition to problem 5
   {
     if(root == null)
        return;
     else if(i == 0)
        System.out.print(root.item+" ");
     else
     {
        printAtDepth(root.left,i-1);
        printAtDepth(root.right,i-1);
     }
   }
}