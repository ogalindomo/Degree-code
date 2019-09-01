/**
 * Contains the model for the Connect Five board. (No GUI elements should placed here.)
 * 
 * @author Edgar Padilla
 *
 */
public class Board
{
    /** Defines the size of the board */
    public final int size;
    private int numberOfDisks;
    public boolean player1 [][];
    public boolean player2 [][];
    private int status;
    
    /**
     *  Default constructor
     */
    public Board(int size)
    {
        this.size = size;
        player1 = new boolean[size][size];
        player2 = new boolean[size][size];
        status = 0;
        // Your Code Goes Here!
    }
    
    /**
     * Adds a disc to the game board.
     * 
     * @param x x coordinate of where the disk needs to be placed.
     * @param y y coordinate of where the disk needs to be placed.
     */
    public void addDisk(int x, int y)
    {
        if(isValidPosition(x,y))
        {
          //System.out.println("X "+x+" Y "+y);
          numberOfDisks += 1;
        }
    }
    
    /**
     * Checks if input positions is valid. Checks if valid x-y range. Also checks if position is empty.
     * 
     * @param x x input.
     * @param y y input.
     * 
     * @return Validity of placement of the disc.
     */
    public boolean isValidPosition(int x, int y)//Change to private once testing is done.
    {
        int coord_x = 0, coord_y = 0;
        if(size == 15)
        {
            if(!(x > 25 && x < 625)||!(y > 25 && y < 625))
            {
                status = 1;
                return false; 
            }
            coord_x = ((x-25)/40);
            coord_y = ((y-25)/40);
            if(player1[coord_x][coord_y]||player2[coord_x][coord_y])
            {
                status = 2;
                return false;
            }
        }
        else if(size == 9)
        {
            if(!(x > 25 && x < 628)||!(y > 25 && y < 628))
            {
                status = 1;
                return false;
            }

            coord_x = ((x-25)/67);
            coord_y = ((y-25)/67);
            if(player1[coord_x][coord_y]||player2[coord_x][coord_y])
            {
                status = 2;
                return false;
            }
        }
        if(numberOfDisks % 2 == 0)
        {
          player1[coord_x][coord_y] = true;  
          if(win(player1))
            status = 3;
          else if(!(win(player1)))
            status = 0;
        }
        else if(numberOfDisks % 2 ==1)
        {
          player2[coord_x][coord_y] = true;     
          if(win(player2))
            status = 4;
          else if(!(win(player2)))
            status = 0;
        }
        return true;
    }

    /** Returns the size of this board. */
    public int size() 
    {
        return size;
    }
    
    /** Returns the number of disks in the game board.*/
    public int getNumberOfDisks(){return numberOfDisks;}
    
    /** Reports the status after attempting to add a disc*/
    public int getStatus(){return status;}
    
    public boolean player1Use (int coord_x, int coord_y)
    {
        return  player1[coord_x][coord_y];
    }
    
    public boolean player2Use (int coord_x, int coord_y)
    {
        return  player2[coord_x][coord_y];
    }
    
    public boolean win(boolean playerArr[][])
    {
        for(int coord_x = 0; coord_x < this.size; coord_x++)//Loop that goes through each possible x coordinate 
        {
        for(int coord_y = 0; coord_y < this.size; coord_y++)//Loop that goes through each possible y coordinate 
        {
          //Each of the following for loops represents a direction to traverse and check for a possible winning combination, these loops check the diagonal, horizontal, and vertical direction. 
          for(int x = coord_x, y = coord_y, continous = 0; permitted(x,y) && playerArr[x][y] != false; x++)
          {
            if(playerArr[x][y] == true)
              continous += 1;
            if(continous == 5)
              return true;
          }  
     
          for(int x = coord_x, y = coord_y, continous = 0;permitted(x,y) && playerArr[x][y] != false; x--)
          {
            if(playerArr[x][y] == true)
              continous += 1;
            if(continous == 5)
              return true;
          } 
    
          for(int x = coord_x, y = coord_y, continous = 0;permitted(x,y) && playerArr[x][y] != false; y++)
          {
            if(playerArr[x][y] == true)
              continous += 1;
            if(continous == 5)
              return true;
          }
    
          for(int x = coord_x, y = coord_y, continous = 0; permitted(x,y) && playerArr[x][y] != false; y--)
          {
            if(playerArr[x][y] == true)
              continous += 1;
            if(continous == 5)
              return true;
          }
     
          for(int x = coord_x, y = coord_y, continous = 0; permitted(x,y) && playerArr[x][y] != false; x++, y++)
          {
            if(playerArr[x][y] == true)
              continous += 1;
            if(continous == 5)
              return true;
          } 
     
          for(int x = coord_x, y = coord_y, continous = 0; permitted(x,y) && playerArr[x][y] != false; x--, y++)
          {
            if(playerArr[x][y] == true)
              continous += 1;
            if(continous == 5)
              return true;
          } 
      
          for(int x = coord_x, y = coord_y, continous = 0; permitted(x,y) && playerArr[x][y] != false; x--, y--)
          {
            if(playerArr[x][y] == true)
              continous += 1;
            if(continous == 5)
              return true;
          } 
      
          for(int x = coord_x, y = coord_y, continous = 0; permitted(x,y) && playerArr[x][y] != false; x++, y--)
          {
            if(playerArr[x][y] == true)
              continous += 1;
            if(continous == 5)
              return true;
          } 
       }
       }
       return false;//If all the board of a player is traversed and no winning combination is found then false is returned 
    }
    
    private boolean permitted(int x, int y)
    {
      if(x >= 0 && x < this.size && y >= 0 && y < this.size)
        return true;
      return false;
    }
    
}
