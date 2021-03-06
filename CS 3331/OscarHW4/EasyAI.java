import java.util.Random;

/**
 * Class for the implementation of an easy AI
 *
 * @author Oscar Galindo, Mario Delgado
 */
public class EasyAI implements AI
{
    /** X component of the coordinate generated by the execution. */
    private int x;
    
    /** Y component of the coordinate generated by the execution. */
    private int y;
    
    /** Instance of the board model that the game is currently using. */
    private Board board;
    
    /** 
     *  Constructor for the AI
     *  @param Board board (instance of the board used for the game)/
     */
    public EasyAI (Board board)
    {
        this.board = board;
        getCoordinates();
    }
    
    /**
     *  Performs a move if the coordinates selected by the execution are not used.
     */
    public void makeMove()
    {
        getCoordinates();
        board.addDisk(x,y);
        while(board.getStatus() == 2) //While the board reports that the coordinate was not set by the AI a new coordinate is generated
        {
           getCoordinates();
           board.addDisk(x,y);
        }
    }
    
    /**
     *  Obtains the x and y components of the coordinate that AI will use to put a disk.
     */
    public void getCoordinates()
    {
       Random rand = new Random(); 
       int sizeLimit = board.size();
       this.x = rand.nextInt(sizeLimit - 1);
       this.y = rand.nextInt(sizeLimit - 1);
    }
    
    /**
     *  Setter of the instance board
     *  @param Board board (represents the instance of the board that is currently used in execution).
     */
    public void setBoard(Board board)
    {
       this.board = board; 
    }
}
