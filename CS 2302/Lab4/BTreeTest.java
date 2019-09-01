///////////////////////////////////////////
//Author: Oscar Galindo Molina           //
//ID: 80585887                           //
//CS 2302                                //
//Professor: Dr.Olac Fuentes             //
//TA: Zakia Al Kadri                     //
//Lab 4                                  //
///////////////////////////////////////////
import java.util.Random; 
public class BTreeTest
{
  public static int num[];
  public static int index = 0;
  public static BTreeNode start;
  public static void printAscending(BTreeNode T)
  {
     //Prints all items in the tree in ascending order
    if (T.isLeaf)
    {
      for(int i =0; i<T.n;i++)
        System.out.print(T.item[i]+" ");
    }
    else
    {
      for(int i =0; i<T.n;i++)
      {
        printAscending(T.c[i]);
        System.out.print(T.item[i]+" ");
      }
       printAscending(T.c[T.n]);
    }
  }

   public static int m1(BTreeNode T)
  { 
    if (T.isLeaf)
      return T.n;
      
    return T.n + m1(T.c[T.n]);
  }

  public static int m2(BTreeNode T)
  { 
    int sum =0;
    for(int i =0; i<T.n;i++)
       if (T.item[i]%2 ==0)
            sum++;
    if (!T.isLeaf)
      for(int i =0; i<=T.n;i++)
    sum += m2(T.c[i]);
    return sum;
   }

  public static int m3(BTreeNode T, int k)
  {
     int i=0;
     while ((i<T.n )&&(k>T.item[i])) //Sequentially search for k
        i++;
     if (T.isLeaf)
       return i;
     else
        return i + m3(T.c[i], k);
   }

   public static void main(String[] args)   
   {
      //int [] S ={ 21, 2, 20, 12, 11, 18,  9, 17, 25, 30, 7, 13,  5, 14, 10,  6,  3, 19, 15, 16,  26, 8,  4, 24, 31,1};
      //int [] S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};
      int [] S ={8, 9, 11, 4, 7,  12, 13, 17, 24, 15, 27, 28, 30, 33, 34, 37, 40, 42, 50, 16 };
      int [] S1 ={8, 9, 11, 4, 7,  12, 13, 17, 24, 15, 27, 28, 30, 33, 34, 37, 40, 42, 50, 16,100,200,300,-10,20,19 };
      int [] D = {10, 15, 4, 8 ,9, 5, 2, 3, 7, 12, 18, 1,24, 60 ,6,78,115,31,76,148,23,-15,-20,-30,-64,-128,-32,1000,320,-10000};
      int [] F = {10, 15, 4, 8 ,9, 5, 2, 3, 7, 12, 18, 1,24, 60 ,6,78,115,31,76,148,23,-15,-20,-30,-64,-128,-32,1000,320,-10000, 34,56,61,64,90,83,85,45,67,34};
       int x_max =100;
      int y_max =100;
      StdDraw.setXscale(-10, 110);
      StdDraw.setYscale(-10, 110);
      StdDraw.setPenColor(StdDraw.BLACK);  
      BTree B = new BTree(3);
      //Build B-tree from array
      for (int i=0;i<S.length;i++){
         System.out.println("New element: "+S[i]);          
         B.insert(S[i]);

         System.out.println("Tree (pre-order traversal)");
           B.printNodes();
         System.out.println("*********************");
      }
      BTreeNode T = B.root;
      num = new int[countItems(T)];
      System.out.println(countItems(T));
      draw_tree(T, 0, x_max, y_max-5, (y_max-10.0)/(B.height+1),0);
      start = T;
      //toArray(T, num.length/2);
      
      System.out.println(searchLevel(T,100));
      // toArray(T);
      // printSmallest(T,2);
      // printLargest(T,2);
      
  }
 
  
  public static void draw_tree(BTreeNode T, double x0, double x1, double y, double y_inc, int level) 
  {
    if(T ==null)
       return;
    double xm = (x0+x1)/2;
    double yn = y-y_inc;//correct
    for(int i = 0; i < T.n+1; i++)
    {
       printLinear(T,y,x1,level+1);
    }
     if(T.isLeaf)//correct
     {
       for(int i = 0; i < T.n; i++,xm+= 6)
       {
         StdDraw.setPenColor(StdDraw.WHITE);
         StdDraw.filledCircle(xm,y, 3);
         StdDraw.setPenColor(StdDraw.BLACK);
         StdDraw.circle(xm,y,3);
         StdDraw.text(xm,y,Integer.toString(T.item[i]));
       }   
      }
    else //T!isLeaf
    {
      double k = x1/(T.n);
      double j = 0;
      for(int i = 0; i < T.n+1; i++,j = j + k)
      {
        StdDraw.line(xm,y,j,yn);
        draw_tree(T.c[i],x0,j,yn,y_inc,level+1);
      }
      
      for(int i = 0; i < T.n; i++, xm+= 6)
      {
        StdDraw.setPenColor(StdDraw.WHITE);
        StdDraw.filledCircle(xm,y, 3);
        StdDraw.setPenColor(StdDraw.BLACK);
        StdDraw.circle(xm,y, 3);
        StdDraw.text(xm,y,Integer.toString(T.item[i]));
       }
   }
}
  
  public static double printLinear(BTreeNode T, double y, double totalXchange, int level)
  {
     double change = totalXchange/printNodeDepth(T,level);
     double xm = 0;
     for(int i =0;i < T.n+1;i++,xm+=6)
     {
       StdDraw.setPenColor(StdDraw.WHITE);
       StdDraw.filledCircle(xm,y, 3);
       StdDraw.setPenColor(StdDraw.BLACK);
       StdDraw.circle(xm,y, 3);
       StdDraw.text(xm,y,Integer.toString(T.item[i]));
    }
    return xm;
  }
  
   public static void printAscendingtoArray(BTreeNode T)//Problem A
  {
     //Prints all items in the tree in ascending order
    if (T.isLeaf)
        toArray(T);
    else
    {
      for(int i =0; i<T.n;i++)
      {
        printAscendingtoArray(T.c[i]);
        toArray(T.item[i]);
      }
       printAscendingtoArray(T.c[T.n]);
    }
  }
  
  public static void toArray(BTreeNode T)//Problem A
  {
     for(int additionIndex = 0; additionIndex < T.n; additionIndex++)
     {
       System.out.println(index);
       num[index] = T.item[additionIndex];
       index = index +1;
     } 
  }
  
  public static void toArray(int number)//Addition to Problem A
  {
    System.out.println(index);
    num[index] = number;
    index = index +1;
  }
  
  public static int countItems(BTreeNode root)//Addition to Problem A
  {
    if(root.isLeaf)
        return root.n;
    else // root not leaf
    {
      int sum = root.n;
      for(int i = 0; i < root.n+1; i++)
        sum += countItems(root.c[i]);
      return sum;
    }
  }
  
  public static void printSmallest(BTreeNode root, int level)//Problem B
  {
    if(level == 0)
        System.out.println(root.item[0]);
    else if(root.isLeaf && level != 0)
        return;
    else
    {   //System.out.println(level);
        printSmallest(root.c[0],level-1);
    }
  }
 
  public static void printLargest(BTreeNode root, int level) //Problem C
  {
    if(level == 0 && root != null)
        System.out.println(root.item[root.n-1]);
    else if (root.isLeaf && level != 0)
        return;
    else //root is not a leaf and level != 0
        printLargest(root.c[root.n], level-1);
  }
  
  public static int printNodeDepth(BTreeNode root, int level)//Problem D
  {
     if(level == 0 && root != null)
    {
      return 1;
    }
    
    else if(root != null && root.isLeaf && level !=0)
    {
      return 0; 
    }
    else //root is not a leaf and level is not 0
    {
      int sum = 0;
      for(int i = 0; i < root.n+1; i++)
        sum += printNodeDepth(root.c[i], level-1);
      return sum;
    } 
  }
  
  public static void printDepth(BTreeNode root, int level)//Problem E
  {
    if(level == 0 && root != null)
    {
      for(int i = 0; i < root.n; i++)
        System.out.print(root.item[i] +" ");
    }
    
    else if(root.isLeaf && level !=0)
    {
      return; 
    }
    else //root is not a leaf and level is not 0
    {
      for(int i = 0; i < root.n+1; i++)
        printDepth(root.c[i], level-1);
    }
  }
  
  public static int nodesFull(BTreeNode root)//Problem F
  {
    if(root.n == 5 && root != null && !(root.isLeaf))
    {
      int sum = 1;
      for(int i = 0; i < root.n+1; i++)
        sum += nodesFull(root.c[i]);
      return sum;
    }
    else if(root.n != 5 && root != null && !(root.isLeaf))
    {
      int sum = 0;
      for(int i = 0; i < root.n+1; i++)
        sum += nodesFull(root.c[i]);
      return sum;
    }
    else if(root.isLeaf && root.n == 5)
      return 1;
    else //if(root.isLeaf && root.n != 5)
      return 0; 
  }
  
  public static int leavesFull(BTreeNode root)//Problem G
  {
    if(root != null && root.isLeaf && root.n == 5)
    {
      return 1;
    }
    
    else if(root != null && root.isLeaf && root.n != 5)
    {
      return 0; 
    }
    else //root is not a leaf and level is not 0
    {
      int sum = 0;
      for(int i = 0; i < root.n+1; i++)
        sum += leavesFull(root.c[i]);
      return sum;
    }
  }
  
  public static int searchLevel(BTreeNode root, int k) //Problem H
  {
    int i = 0;
    while(i < root.n && k > root.item[i])
        i++;
    if(i == root.n || k < root.item[i])
        if(root.isLeaf)
            return -1;
        else
        {
            int sum = searchLevel(root.c[i], k);
            if(sum != -1)
             return 1 + sum;
            else    
             return -1;
        }
            
    else
        return 0;
  }
  
  public static void SearchBTree(BTreeNode root, int k) //Problem I
  {
    int i = 0;
    while(i < root.n && k > root.item[i])
        i++;
    if(i == root.n || k < root.item[i])
        if(root.isLeaf)
            return;
        else
             SearchBTree(root.c[i], k);
    else
        for(int j = 0; j < root.n; j++)
            System.out.print(root.item[j]+" ");
  } 
}