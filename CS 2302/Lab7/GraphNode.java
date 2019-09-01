
public class GraphNode
{
   public int origin;
   public int destination;
   public GraphNode next;
   public String originS;
   public String destinationS;
   public double cost;
   
   public GraphNode()
   {
     
   }
   public GraphNode(int or, int dest, GraphNode n)
   {
     this.origin = or;
     this.destination = dest;
     next = n;
   }
   public GraphNode(String or, String dest, GraphNode n)
   {
     this.originS = or;
     this.destinationS = dest;
     next = n;  
   }
   public GraphNode(String or, String dest, GraphNode n, double price)
   {
     this.originS = or;
     this.destinationS = dest;
     next = n;
     cost = price;
   }
}
