public class hashTableStrings
{
  public sNode [] H;
  public int numberOfElements;
  public hashTableStrings(int n)// Initialize all lists to null
  { 
    H = new sNode[n];
    numberOfElements = 0;
    for(int i = 0;i < n;i++)
      H[i] = null;
  }
  
  private int h(String S)
  {
    int h = 0;
    for(int i = 0;i < S.length();i++)
      h = (h*27+S.charAt(i))%H.length;
    return h; 
  }
  
  public void insert(sNode newWord)
  {
    int pos = h(newWord.word); 
    newWord.next = H[pos];
    H[pos] = newWord;
    numberOfElements++;
    if(numberOfElements > H.length*3)
    {
      newSize();  
    }
  }
  
  public void newSize()
  {
    hashTableStrings newH = new hashTableStrings((H.length*2)+1);
    for(int i = 0; i < H.length; i++)
    {
      for(sNode holder = H[i]; holder != null; holder = holder.next)
      {
         newH.insert(new sNode(holder.word,holder.embedding,null));
      }
    }
    substitute(newH);
  }
  
  public void substitute(hashTableStrings newH)
  {
    this.H = newH.H;
    this.numberOfElements = newH.numberOfElements;
  }
  
  public void empty()
  {
    int numberEmpty = 0;
    for(int i = 0; i < H.length; i++)
      if(H[i] == null)
        numberEmpty++;
    double emnum = (double) numberEmpty;
    double percentage = (emnum*100)/H.length;
    System.out.println("Length: "+H.length);
    System.out.println("Empty: "+numberEmpty);
    System.out.println(percentage);
  }
  
  public void nonEmpty()
  {
    int nonEmpty = 0;
    for(int i = 0; i < H.length; i++)
       if(H[i] != null)
         nonEmpty++;
    System.out.println("Non empty = "+nonEmpty);
  }
  
  public double loadFactor()
  {
    return (double)numberOfElements / H.length;
  }
  
  public double standardDev()
  {
    double addition = 0;  
    for(int i = 0; i < H.length; i++)
      addition += calculation(H[i]);
    return (double)Math.sqrt(addition/(numberOfElements-1));
  }
  
  public double calculation(sNode origin)
  {
    int nodeNum = 0;
    for(;origin != null; origin = origin.next)
    {
      nodeNum ++;  
    }
    return Math.pow(((double)nodeNum - loadFactor()), 2);  
  }
  
  public sNode search(String word)
  {
     int pos = h(word); 
     for(sNode holder = H[pos]; holder != null; holder = holder.next)
       if(holder.word.equals(word))
          return holder;
     return null;
  }
}
