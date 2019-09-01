package HW4;
public interface AI
{
    /** Contract-method that forces the AI to implement a method to perform a choice of disk. */
    public void makeMove();
    /** Conctract-method that forces the AI to implement a method in which coordinates to be played are generated. */
    public void getCoordinates();
    /** Contract-method that forces the AI to implement a method to receive the board to which the execution changed to play. */
    public void setBoard(Board board);
}
