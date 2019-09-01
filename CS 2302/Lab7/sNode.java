public class sNode
{
  public String word;
  public float[] embedding;
  public sNode next;
   public sNode(String S, float[] E, sNode N)
   {
      word = S;
      embedding = new float[50];
      for (int i = 0;i < 50;i++)
         embedding[i] = E[i];
      next = N;
  } 
}
