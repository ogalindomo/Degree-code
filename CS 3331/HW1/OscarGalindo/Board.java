///////////////////////////////////////////
//Author: Oscar Galindo Molina           //
//ID: 80585887                           //
//CS 3331                                //
//Professor: Edgar Padilla             //
//HW 1                                   //
//////////////////////////////////////////
public class Board
{
  public static boolean board[][] = new boolean [15][15];
  public static boolean boardRed[][] = new boolean [15][15];
  public static boolean boardBlue[][] = new boolean [15][15];
  public static int numberOfDisks = 0;
  
  public static void addDisk (int coord_x, int coord_y)
  {
    if(coord_x < 0 || coord_y < 0)//If any of the coordinates is less than 0 then the game is over.
     {
        System.out.println("THE GAME IS OVER.");
        numberOfDisks = 256;
     }
     else if(!(coord_x > 0 && coord_x < 16) || !(coord_y > 0 && coord_y < 16)) //If the coordinates are outside of the range 1-15 then the program reports that the coordinate does not exist.
     {
        System.out.println("THAT COORDINATE DOES NOT EXIST.");
        System.out.println(" ");
     }
     else
     {
       if(board[coord_y - 1][coord_x - 1] == true)//If the coordinate is already used then the program reports it.
       {
          System.out.println("THAT COORDINATE IS ALREADY USED.");
          System.out.println(" ");
       }
       else
       {
          System.out.println(" ");
          if(numberOfDisks % 2 == 0)//This section of code sets, when it is the turn of player 1, the choosen space to be true(used) and then checks if the player has won based on the function win.
          {
             boardRed[coord_y - 1][coord_x - 1] = true;
             if(win(boardRed))//This function checks if player one won.
             {
               System.out.println("THE GAME IS OVER.");
               System.out.println("Congratulations Player 1.");
               numberOfDisks = 256; //The number of disks is set to be 256 so that the execution of the game is stopped. The execution is stopped because the number of disks is set above 225 which is the threshold of the loop in the loop of the class main
             }
          }
          else
          {
             boardBlue[coord_y - 1][coord_x - 1] = true;
             if(win(boardBlue))//This function checks if player two won.
             {
               System.out.println("THE GAME IS OVER.");
               System.out.println("Congratulations Player 2.");
               numberOfDisks = 256; //The number of disks is set to be 256 so that the execution of the game is stopped. The execution is stopped because the number of disks is set above 225 which is the threshold of the loop in the loop of the class main
             }
          }
          board[coord_y - 1][coord_x - 1] = true;//After the coordinate is added to the array of used coordinates of each player, the array that contains all used coordinates receives the coordinate choosen by the any of the two players.
          numberOfDisks++;
       }
    }    
  }
  
  public static boolean win (boolean playerArr[][])
  //This function traverses in every turn the array of the player that is interacting with the game and checks all the board for any possible connection of five disks. 
  {
    for(int coord_x = 1; coord_x < 16; coord_x++)//Loop that goes through each possible x coordinate 
    {
       for(int coord_y = 1; coord_y < 16; coord_y++)//Loop that goes through each possible y coordinate 
       {
         //Each of the following for loops represents a direction to traverse and check for a possible winning combination, these loops check the diagonal, horizontal, and vertical direction. 
         for(int x = coord_x - 1, y = coord_y - 1, continous = 0; x >= 0 && x < 15 && y >= 0 && y < 15 && playerArr[y][x] != false; x++)
         {
           if(playerArr[y][x] == true)
             continous += 1;
           if(continous == 5)
             return true;
         }  
    
         for(int x = coord_x - 1, y = coord_y - 1, continous = 0; x >= 0 && x < 15 && y >= 0 && y < 15 && playerArr[y][x] != false; x--)
         {
           if(playerArr[y][x] == true)
             continous += 1;
           if(continous == 5)
             return true;
         } 
    
         for(int x = coord_x - 1, y = coord_y - 1, continous = 0; x >= 0 && x < 15 && y >= 0 && y < 15 && playerArr[y][x] != false; y++)
         {
           if(playerArr[y][x] == true)
             continous += 1;
           if(continous == 5)
             return true;
         }
    
         for(int x = coord_x - 1, y = coord_y -1, continous = 0; x >= 0 && x < 15 && y >= 0 && y < 15 && playerArr[y][x] != false; y--)
         {
           if(playerArr[y][x] == true)
             continous += 1;
           if(continous == 5)
             return true;
         }
    
         for(int x = coord_x -1, y = coord_y -1, continous = 0; x >= 0 && x < 15 && y >= 0 && y < 15 && playerArr[y][x] != false; x++, y++)
         {
           if(playerArr[y][x] == true)
             continous += 1;
           if(continous == 5)
             return true;
         } 
     
         for(int x = coord_x -1, y = coord_y -1, continous = 0; x >= 0 && x < 15 && y >= 0 && y < 15 && playerArr[y][x] != false; x--, y++)
         {
           if(playerArr[y][x] == true)
             continous += 1;
           if(continous == 5)
             return true;
         } 
     
         for(int x = coord_x -1, y = coord_y - 1, continous = 0; x >= 0 && x < 15 && y >= 0 && y < 15 && playerArr[y][x] != false; x--, y--)
         {
           if(playerArr[y][x] == true)
             continous += 1;
           if(continous == 5)
             return true;
         } 
     
         for(int x = coord_x - 1, y = coord_y - 1, continous = 0; x >= 0 && x < 15 && y >= 0 && y < 15 && playerArr[y][x] != false; x++, y--)
         {
           if(playerArr[y][x] == true)
             continous += 1;
           if(continous == 5)
             return true;
         } 
      }
    }
    return false;//If all the board of a player is traversed and no winning combination is found then false is returned
  }
}
