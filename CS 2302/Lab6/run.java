import java.util.*;
import java.io.*;
public class run
{
   public static hashTableStrings list;
   public static String words[];
   public static Heap spaces;
   public static DSF link;
   public static void main (String [] args) throws IOException
   {
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
     processes(10);
     link.largestClusters(6);
     //link.printdsf();
   }
   
   public static double processSimilar(String firstWord, String secondWord)
   {
     int indexRead = 0;
     return findSimilarities(firstWord,secondWord);
   }
   
   public static double findSimilarities(String firstWord, String secondWord)
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
     link = new DSF(lineNum);
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
      spaces = new Heap(words.length*words.length-1);
      for(int i = 0; i < words.length;i++)
      {
        for(int j = 0;j < words.length;j++)
        {
          if(i != j)
          {
            HeapNode holder = new HeapNode (words[i],words[j],processSimilar(words[i],words[j]));
            spaces.insert(holder);
          }
        } 
      }
   }
   
   public static void processes(int n)
   {
     for(int i = 0; i < n;i++)
     {
       HeapNode holder = spaces.extractMin();
       //System.out.println(holder.word0+" "+holder.word1+" "+holder.similarity);//Control Statement
       String firstWord = holder.word0;
       String secondWord = holder.word1;
       int firstPos = index(firstWord);
       int secondPos = index(secondWord);
       //System.out.println(firstPos+" "+secondPos);
       link.union_by_size(firstPos,secondPos);  
     }
   }
   
   public static int index(String word)
   {
     for(int i = 0; i < words.length; i++)
     {
       if(word.equals(words[i]))
         return i;
     } 
     return -1;
   }
}
