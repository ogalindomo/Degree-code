import java.util.*;
import java.io.*;
public class run
{
   public static hashTableStrings list;
   public static void main (String [] args) throws IOException
   {
     File here = new File ("fourth.txt");
     Scanner read = new Scanner(here);
     list = new hashTableStrings(1997);
     while(read.hasNextLine())
     {
       String line = read.nextLine();
       processInput(line);
     }
     read.close();
     long start = System.nanoTime();
     list.empty();
     System.out.println("Load Factor: "+list.loadFactor());
     System.out.println("Standard Deviation of Length: "+list.standardDev());
     long end   = System.nanoTime();
     long total = end - start;
     System.out.println("Time: "+total);
     
     
     File newHere = new File("words.txt");
     Scanner similarRead = new Scanner(newHere);
     while(similarRead.hasNextLine())
     {
       processSimilar(similarRead.nextLine());  
     }
   }
   
   public static void processSimilar(String line)
   {
     int indexRead = 0;
     String firstWord = "", secondWord = "";
     for(int i = 0; i < 2; i++)
     {
       for(;indexRead < line.length() && line.charAt(indexRead) != ','; indexRead++)
       {
         if(i == 0)
            firstWord += line.charAt(indexRead);
         else
            secondWord += line.charAt(indexRead);
       }
       indexRead +=1;
     }
     System.out.print("Similarity of "+firstWord +" & "+secondWord+" is: ");
     findSimilarities(firstWord,secondWord);
   }
   
   public static void findSimilarities(String firstWord, String secondWord)
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
     System.out.println(numerator/denominator);       
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
}
