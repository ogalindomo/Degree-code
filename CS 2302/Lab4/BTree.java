public class BTree
{
  public BTreeNode root;
  private int t; //2t is the maximum number of childen a node can have
  public int height;
    
  public BTree(int t)
  {
    root = new BTreeNode(t);
    this.t = t;
    height = 0;
  }
    
  public void printHeight()
  {
    System.out.println("Tree height is "+height);
  }
    
  public void insert(int newKey)
  {
    if (root.isFull())
    {//Split root;
      split();
      height++;
    }
    root.insert(newKey);
  }
    
  public void print()
  {
    // Wrapper for node print method
    root.print();
  }
    
  public void printNodes()
  {
    // Wrapper for node print method
    root.printNodes();
  }

   public void split()
   {
     // Splits the root into three nodes.
     // The median element becomes the only element in the root
     // The left subtree contains the elements that are less than the median
     // The right subtree contains the elements that are larger than the median
     // The height of the tree is increased by one

     // System.out.println("Before splitting root");
     // root.printNodes(); // Code used for debugging
     BTreeNode leftChild = new BTreeNode(t);
     BTreeNode rightChild = new BTreeNode(t);
     leftChild.isLeaf = root.isLeaf;
     rightChild.isLeaf = root.isLeaf;
     leftChild.n = t-1;
     rightChild.n = t-1;
     int median = t-1;
     for (int i = 0;i<t-1;i++)
     {
       leftChild.c[i] = root.c[i];
       leftChild.item[i] = root.item[i];
     }
     leftChild.c[median]= root.c[median];
     for (int i = median+1;i<root.n;i++)
     {
       rightChild.c[i-median-1] = root.c[i];
       rightChild.item[i-median-1] = root.item[i];
     }
     rightChild.c[median]=root.c[root.n];
     root.item[0]=root.item[median];
     root.n = 1;
     root.c[0]=leftChild;
     root.c[1]=rightChild;
     root.isLeaf = false;
        // System.out.println("After splitting root");
        // root.printNodes();
  }
}