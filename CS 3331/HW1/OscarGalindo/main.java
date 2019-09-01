///////////////////////////////////////////
//Author: Oscar Galindo Molina           //
//ID: 80585887                           //
//CS 3331                                //
//Professor: Edgar Padilla               //
//HW 1                                   //
//////////////////////////////////////////
import java.util.*;
public class main
{
  public static void main (String [] args)
  {
    Scanner in = new Scanner(System.in);
    ConsoleUI.drawUI();//Initial Print of the Board
    while(Board.numberOfDisks <= 225)//Main control structure of the game, the game executes until the number of Disks is less or equal to 225
    {
      if(Board.numberOfDisks == 225)
      {
         System.out.println("It is a DRAW.");
         Board.numberOfDisks++;//This line stops the execution of the loop after the game has detected that nobody won the game and the board is full.
      }
      else
      {
        if(Board.numberOfDisks % 2 == 0)//This makes the game start with player one
           System.out.println("Player 1");
         else//This makes the game to continue with player 2 and the loop repeats
           System.out.println("Player 2");
        System.out.println("Please input x and y coordinates, or input -1 to end the game.");
        int coord_x = in.nextInt();//The scanner reads the first coordinate as the X
        int coord_y = in.nextInt();//The scanner reads the second coordinate as the Y
        System.out.println("Coordinates selected: x="+coord_x+" y="+coord_y);
        Board.addDisk(coord_x,coord_y);//The selected coordinate is used and is added to the already used disks
        ConsoleUI.drawUI();//The board is the printed with the new disk included.
      }
    }
    in.close();
  }
}
