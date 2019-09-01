///////////////////////////////////////////
//Author: Oscar Galindo Molina           //
//ID: 80585887                           //
//CS 3331                                //
//Professor: Edgar Padilla               //
//HW 1                                   //
//////////////////////////////////////////
public class ConsoleUI
{
   public static void drawUI()
   {
      System.out.print("y/x   "); 
      for(int i = 0; i < 15; i++)
      {
        if(i < 10) //This gives format to the colums that are less than 10 
        {
          System.out.print("  ");  
          System.out.print(i+1);
          System.out.print(" ");  
        }
        else if(i >= 10) //This gives format to the column equal or more than 10
        {
          System.out.print(" ");  
          System.out.print(i+1); 
          System.out.print(" ");
        }
      }
      System.out.println("");
      for(int i = 0, rowNum = 1; i < 31; i++)
      {
        if(i % 2 == 0)//This line makes every two lines to be the delimiation lines of the matrix representing the box.
        {
          System.out.print("      ");
          for(int j = 0; j < 15; j++)
          {
            System.out.print("+---"); 
          }
          System.out.println("+");
        }
        else
        {
          if(rowNum < 10)
            System.out.print("   "+rowNum+"  "); //This lines gives formatting to the number of rows that are less than 10
          else if (rowNum >= 10)
            System.out.print("   "+rowNum+" "); //This lines gives formatting to the number of rows that are equal or more than 10 
          for(int j = 0; j < 15; j++)
          {
            System.out.print("|");  
            System.out.print(" ");
            if(Board.redUse(j, rowNum - 1))//This line checks if the space was already selected by a player and prints out, if selected, the sign of each player.
              System.out.print("•");
            else if(Board.blueUse(j, rowNum - 1))
              System.out.print("○");
            else//If the space is not used then a space is printed so graphically it does not show that it is used
              System.out.print(" ");
            System.out.print(" "); 
          }
          System.out.println("|");
          rowNum++;
        }
      }
      System.out.println("");//This line allows the console to move to the next line.
   }
}
