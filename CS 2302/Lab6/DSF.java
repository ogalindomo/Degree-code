public class DSF
{
  private int[] S;
  private int mostElementsIndex;
  private int elementsAtIndex;
  private int min;
  private int[] S1;
  public DSF(int n)
  {
    S = new int[n];
    for(int i = 0;i < n;i++)
      S[i] = -1;
  }
  
  public int union_by_size(int i, int j)
  {
    int ri = find_c(i);
    int rj = find_c(j);
    if(ri == rj)
      return -1;
    if(S[ri]>S[rj])
    {
      S[rj] += S[ri];  
      S[ri] = rj;  
    }
    else
    {
      S[ri] += S[rj];  
      S[rj] = ri;
    }
    return 1;
  }
  
  public void print()
  {
    for(int i = 0;S.length > i;i++)
       System.out.print(S[i]+" ");
    System.out.println();
  }
  
  public int find_c(int i)
  {
    if(S[i] < 0)
      return i;
    int root = find_c(S[i]);
    S[i] = root;
    return root;
  }
  
  public void largestClusters(int m)
  {
    setMax();
    for(int i = 0; i < m;i++)
    {
      System.out.println("Maximum Cluster "+ (i+1));
      System.out.println("Root: "+run.words[mostElementsIndex]);
      System.out.print("Contains: ");
      elementsWithRoot(mostElementsIndex);
      System.out.println("");
      System.out.println(" ");
      newMax();
    }
  }
  
  public void setMax()
  {
    elementsAtIndex = 1;
    copyS();
    for(int i = 0; i < S1.length; i++)
    {
      if(elementsAtIndex < -1*S1[i])
      {
        mostElementsIndex = i;
        elementsAtIndex = -1*S1[i];
      }
    } 
  }
  
  public void copyS()
  {
    S1 = new int[S.length];
    for(int i = 0;i < S.length; i++)
    {
      S1[i] = S[i];  
    } 
  }
  
  public void erase()
  {
    S1[mostElementsIndex] = 0;
    for(int i = 0; i < S1.length; i++)
    {
      if(S1[i] == mostElementsIndex)
        S1[i] = 0;
    }  
  }
  
  public void newMax()
  {
    int newMaxIndex = 0;
    int newNumberElements = 0;
    int min = 1;
    for(int i = 0; i < S.length; i++)
    {
      if(i != mostElementsIndex && elementsAtIndex >= S1[i]*-1 && min <= S1[i]*-1)
      {
        newMaxIndex = i;
        newNumberElements = S[i]*-1;
        min = newNumberElements;
      }
    }
    mostElementsIndex = newMaxIndex;
    //System.out.println("New Index"+mostElementsIndex);.
    elementsAtIndex = newNumberElements;
  }
  
  public void elementsWithRoot(int root)
  {
    for(int i = 0; i < run.words.length;i++)
    {
      if(S1[i] == root)
       System.out.print(run.words[i]+", ");
    } 
    erase();
   }
  
  public void printdsf()
  {
    for(int i = 0; i < S.length; i++)
        System.out.println(i +" "+S[i]);
  }
}
