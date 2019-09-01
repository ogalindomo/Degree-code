public class bstNode extends bst_ops{	
   public int item;
   public bstNode left;
	public bstNode right;
   
   public bstNode(int i){
     item = i;
     left = null;
     right = null;
   }
	
   public bstNode(int i, bstNode l, bstNode r){
     item = i;
     left = l;
     right = r;
   }
}