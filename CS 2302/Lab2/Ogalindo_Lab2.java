
///////////////////////////////////////////
//Author: Oscar Galindo Molina           //
//ID: 80585887                           //
//CS 2302                                //
//Professor: Dr.Olac Fuentes             //
//TA: Daniel Gomez                       //
//Lab 2                                  //
///////////////////////////////////////////
import java.util.Random;

public class Ogalindo_Lab2
{
  public static void main(String[] args)
  {
    int num[] = randomArray(10000, 1000);
    
    //for(int i = 0; i < num.length; i++)
        //System.out.println(num[i]);
    
    // long startTime = System.nanoTime();
    // System.out.println(hasDuplicates(num));
    // long endTime   = System.nanoTime();
    // long totalTime = endTime - startTime;
    // System.out.println(totalTime);
    
    long start = System.nanoTime();
    System.out.println(selectionSort(num));
    long end   = System.nanoTime();
    long total = end - start;
    System.out.println(total);
    
    // long startTime = System.nanoTime();
    // System.out.println(quickSort(num, 0, num.length-1));
    // long endTime   = System.nanoTime();
    // long totalTime = endTime - startTime;
    // System.out.println(totalTime);
    
    // long start = System.nanoTime();
    // System.out.println(duplicateEfficient(num));
    // long end   = System.nanoTime();
    // long total = end - start;
    // System.out.println(total);
  }
    
  public static int[] randomArray(int n, int m)
  {
    int number [] = new int [n];
    for(int i =0; i < number.length; i++)
    {
      Random randomNum = new Random();
      number[i] = randomNum.nextInt(m);
    }
    return number;
  }
  
  public static boolean hasDuplicates(int []A)
  {
    boolean duplicates = false;
    for (int i=0;i<A.length;i++)
         for (int j=0;j<A.length;j++)
              if (A[i]==A[j] && i!=j)
                 duplicates = true;
    return duplicates;
  }
  
  public static boolean duplicateEfficient(int array[])
  {
    for(int i = 0; i < array.length; i++)
    {
      int number = array[i];
      for(int j = i + 1; j < array.length; j++)
      {
        if(number == array[j])
            return true;
      }  
    }
    return false;
  }
  
  public static boolean selectionSort(int number[])
  {
    for (int i = 0; i < number.length - 1; i++)
    {
      int index = i;
      for (int j = i + 1; j < number.length; j++)
      {
           if (number[j] < number[index]) 
                    index = j;
      }
      int smallerNumber = number[index];  
      number[index] = number[i];
      number[i] = smallerNumber;
     }
    
    for(int i = 0; i+1 < number.length; i++)
    {
      if(number[i] == number[i+1])
        return true;
    }
    return false;
  }
  
  public static int partition(int arr[], int low, int high)
  {
     int pivot = arr[high]; 
     int i = (low-1); 
     for (int j=low; j<high; j++)
     {
       if (arr[j] <= pivot)
       {
         i++;
         int temp = arr[i];
         arr[i] = arr[j];
         arr[j] = temp;
       }
     }
     int temp = arr[i+1];
     arr[i+1] = arr[high];
     arr[high] = temp;
     return i+1;
  }
   
  public static boolean quickSort(int number[], int low, int high)
  {
    if (low < high)
    {
      int pi = partition(number, low, high);
      quickSort(number, low, pi-1);
      quickSort(number, pi+1, high);
    }
    
    for(int i = 0; i+1 < number.length; i++)
    {
      if(number[i] == number[i+1])
        return true;
    }
    return false;
  }
  
  public static boolean sorted (int number[])
  {
    boolean place [] = new boolean [number.length];
    for(int i = 0; i < number.length; i++)
    {
      int num = number[i];
      if(place[num] == false)
        place[i] = true;
      else if(place[num] == true)
        return true;
    }
    return false;
  } 
}
