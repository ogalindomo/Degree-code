import java.util.*;
import java.io.*;
import java.lang.Math;
public class run
{
  public static hashTableStrings list;
  public static String words[];
  public static Heap spaces;
  public static void main (String [] args) throws IOException
  {
     int x_max =100;
     int y_max =100;
     StdDraw.setXscale(0, x_max);
     StdDraw.setYscale(0, y_max);
     StdDraw.setPenColor(StdDraw.BLACK); 
     GraphNode list1 [] = new GraphNode[5];
     for(int i = 0; i < list1.length; i++)
     {
       for(int j = i + 1; j < list1.length; j++)
       {
         GraphNode prov = new GraphNode (i,j,list1[i]);
         list1[i] = prov;
       }
     }
     drawList(list1,50,50,40);
     
     
     File here = new File ("glove.6B.50d.txt");
     Scanner read = new Scanner(here);
     list = new hashTableStrings(1997);
     while(read.hasNextLine())
     {
       String line = read.nextLine();
       processInput(line);
     }
     
     read.close();
     toArray();
     processSimilarities();
     long start = System.nanoTime();
     GraphNode beginning = createStart();
     GraphNode MST = KruskalMST(beginning);
     long end   = System.nanoTime();
     long total = end - start;
     System.out.println("Time: "+total);
     
     printMST(MST);
  }
  
  public static void drawList(GraphNode [] list, double x, double y,double r) 
  {
     double change = 360/list.length;
     for(int i = 0; i < list.length; i++)
     {
       for(GraphNode holder = list[i]; holder != null ; holder = holder.next)
       {
          StdDraw.line(x+(r*Math.cos(Math.toRadians(change*holder.origin))), y+(r*Math.sin(Math.toRadians(change*holder.origin)))
               ,x+(r*Math.cos(Math.toRadians(change*holder.destination))),y+(r*Math.sin(Math.toRadians(change*holder.destination))));
       }
       StdDraw.setPenColor(StdDraw.BLUE);
       StdDraw.filledCircle((r*Math.cos(Math.toRadians(change*i)))+x,y+(r*Math.sin(Math.toRadians(change*i))),3);
       StdDraw.setPenColor(StdDraw.BLACK);
       StdDraw.circle(x+(r*Math.cos(Math.toRadians(change*i))),y+(r*Math.sin(Math.toRadians(change*i))), 3);
       StdDraw.text(x+(r*Math.cos(Math.toRadians(change*i))),y+(r*Math.sin(Math.toRadians(change*i))),Integer.toString(i));
     }
  }
  
  public static double processSimilar(String firstWord, String secondWord)
  {
    int indexRead = 0;
    return sim(firstWord,secondWord);
  }  
  
  public static void processInput(String line)
  {
     int firstLetter = line.charAt(0);
     if(!((65 <= firstLetter && firstLetter <= 90)||(97 <= firstLetter && firstLetter <= 122)))
        return;
     String word = "";
     int lineIndex = 0;
     for(; line.charAt(lineIndex) != ' '; lineIndex++)
     {
       word += line.charAt(lineIndex);
     }
     lineIndex += 1;
     String number = "";
     float embedding[] = new float[50];
     int embeddingIndex = 0;
     while(line.length() > lineIndex)
     {
       int reading = line.charAt(lineIndex); 
       if((48 <= reading && reading <= 57)||reading == 46||reading == 45||reading == 101||reading == 69)
          number += line.charAt(lineIndex);
        if(line.charAt(lineIndex) == ' ' || lineIndex == line.length()-1)
       {
         embedding[embeddingIndex] = Float.parseFloat(number);
         number = "";
         embeddingIndex++;
       }
       lineIndex++;
     }
     list.insert(new sNode(word,embedding,null)); 
   }
   
  public static double sim(String firstWord, String secondWord)
  {
     sNode first = list.search(firstWord);
     sNode second = list.search(secondWord);
     if(first == null||second == null)
     {
       System.out.println(" One word is not present.");  
     }     
     double numerator = 0;
     for(int i = 0; first.embedding.length > i;i++)
     {
       numerator += (first.embedding[i] * second.embedding[i]);  
     }     
     double sumA = 0, sumB = 0;
     for(int i = 0; first.embedding.length > i; i++)
     {
       sumA += Math.pow(first.embedding[i],2);  
     }     
     for(int i = 0; second.embedding.length > i; i++)
     {
       sumB += Math.pow(second.embedding[i],2);  
     }     
     double denominator = (Math.sqrt(sumA) * Math.sqrt(sumB));     
     return(numerator/denominator);       
   }
   
  public static void toArray () throws IOException
  {
     File newF = new File("fourth.txt");
     Scanner in = new Scanner(newF);
     int lineNum = 0;
     while(in.hasNextLine())
     {
       if(!(in.nextLine().equals("")))
       {
         lineNum++;  
       }
     }
     in.close();
     //System.out.println("Number of lines: "+lineNum);//Control Statement
     words = new String[lineNum];
     Scanner in2 = new Scanner(newF);
     for(int i = 0; in2.hasNextLine(); i++)
     {
       words[i] = in2.nextLine();
     }
     in2.close();
  }
  
  public static void processSimilarities()
  {
     spaces = new Heap(words.length*(words.length-1));
     for(int i = 0; i < words.length;i++)
     {
       for(int j = 0;j < words.length;j++)
       {
         if(i != j)
         {
           HeapNode holder = new HeapNode (words[i],words[j],sim(words[i],words[j]));
           spaces.insert(holder);
         }
       } 
     }
  }

  public static GraphNode createStart()
  {
    GraphNode Start = null;
    for(int i = 0; i < spaces.H.length; i++)
    {
      HeapNode temp = spaces.extractMin();
      Start = new GraphNode(temp.word0, temp.word1,Start);
    }
    return Start;
  }
  
  public static GraphNode KruskalMST(GraphNode start)
  {
    DSF S = new DSF(words.length);
    GraphNode MST = null;
    for(GraphNode m = start; m != null; m = m.next)
    {
      if(S.union(index(m.originS), index(m.destinationS)) == 1)
      {
        MST = new GraphNode(m.originS,m.destinationS,MST,sim(m.originS,m.destinationS));
      }
    }
    return MST;
  }
  
  public static int index(String word)
  {
     //System.out.println(word);
     for(int i = 0; i < words.length; i++)
     {
       if(word.equals(words[i]))
         return i;
     } 
     return -1;
  }
   
  public static void printMST(GraphNode MST)
  {
    for(GraphNode N = MST; N != null; N = N.next)
    {
      System.out.println("Connect: "+N.originS+" With: "+N.destinationS);
      System.out.println("Cost: "+N.cost); 
      System.out.println(" ");
    }
  }
}
