/**
 * Contains the model for the Connect Five board.
 * 
 * @author Edgar Padilla, Oscar Galindo, Mario Delgado
 */
public class Board
{
    /** Defines the size of the board */
    private final int size;
    
    /** Keeps record of the number of disks present in the board */
    private int numberOfDisks;
    
    /** Keeps record of where player 1 has located his or her disks */
    private boolean player1 [][];
    
    /** Keeps record of where player 1 has located his or her disks */
    private boolean player2 [][];
    
    /** Keeps record on what status is the 
     * board (i.e. a player won, invalid position, already used position, etc.) */
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
    private boolean isValidPosition(int x, int y)//Change to private once testing is done.
    {
        if(!permitted(x,y))
        {
            status = 1;
            return false; 
        }
        else if(player1[x][y]||player2[x][y])
        {
             status = 2;
             return false;
        }
        else if(numberOfDisks % 2 == 0)
        {
          player1[x][y] = true;  
          if(win(player1))
            status = 3;
          else if(!(win(player1)))
            status = 0;
        }
        else if(numberOfDisks % 2 ==1)
        {
          player2[x][y] = true;     
          if(win(player2))
            status = 4;
          else if(!(win(player2)))
            status = 0;
        }
        return true;
    }
    
    /** Returns the number of disks in the game board.
      * @return number of disks
      */
    public int getNumberOfDisks(){return numberOfDisks;}
    
    /** 
      * Reports the status after attempting to add a disc.
      * @return int status (status of the board).
      */
    public int getStatus(){return status;}
    
    /** Reports if a positions that is being checked was already used by player 1 
      * @param coord_x x input
      * @param coord_y y input
      * @return boolean indicating if a specific x,y coordinate has been used by player 1.
      */
    public boolean player1Use (int coord_x, int coord_y)
    {
        return  player1[coord_x][coord_y];
    }
    
    /** Reports if a positions that is being checked was already used by player 2 
      * @param coord_x x input
      * @param coord_y y input
      * @return boolean indicating if a specific x,y coordinate has been used by player 2.
      */
    public boolean player2Use (int coord_x, int coord_y)
    {
        return  player2[coord_x][coord_y];
    }
    
    /** Reports out if the player that is playing won or not. 
      * @param boolean playerArr (reference of the array of the player whose turn it is).
      * @return boolean win (indicating if the player won).
      */
    private boolean win(boolean playerArr[][])
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
    
    /** Returns the size of this board. 
      * @return an integer indicating the size of the board.
      */
    public int size() 
    {
        return size;
    }
    
    /** Reports if the position being checked by the win method actually 
     *  exists within the array of the player whose turn it is.
     *  @param x x input
     *  @param y y input
     *  @return boolean that indiciates if the coordinate that will be accessed by the win method actually exists.
     */
    private boolean permitted(int x, int y)
    {
       if(x >= 0 && x < this.size && y >= 0 && y < this.size)
         return true;
       return false;
    }
    
    /** Provides a copy to the solicitor of the array that represents player1's board
     *  @return boolean[][] player1Copy that represents player1's board.
     */
    public boolean[][] aiAnalysisArray()
    {
       boolean player1Copy[][] = new boolean[this.size][this.size];
       for(int i = 0; i < player1Copy.length; i++)
       {
          for(int j = 0; j < player1Copy[i].length; j++)
          {
             player1Copy[i][j] = player1[i][j];
          }  
       }
       return player1Copy;
    }
    
    /** Provides a copy to the solicitor of the array that represents AI's board
     *  @return boolean[][] player2Copy that represents AI's board.
     */
    public boolean[][] aiArray()
    {
       boolean player2Copy[][] = new boolean[this.size][this.size];
       for(int i = 0; i < player2Copy.length; i++)
       {
          for(int j = 0; j < player2Copy[i].length; j++)
          {
             player2Copy[i][j] = player2[i][j];
          }  
       }
       return player2Copy;
    }
}
