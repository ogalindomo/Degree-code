import static org.junit.Assert.*;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class BoardTest {
    
    private Board board;
    
    @Before
    public void setUp() {
        board = new Board(9);
    }

    @Test
    public void testBoard() {
        assertEquals(9, board.size()); // default size
    }
    
    @Test
    public void testBoard2() {
        board = new Board(4);
        assertEquals(4, board.size());
    }
    
    @Test
    public void testOutsideCoord(){//Tests to see that the execution identifies coordinates that are not of the board
        board = new Board(9);
        assertEquals(false, board.isValidPosition(10,250));
    }
    
    
    public void winningPlayer1(){//Tests that player 1 wins
        board = new Board(15);
        for(int i  = 0; i < 5; i++)
            board.player1[0][i] = true;
        assertEquals(true, board.win(board.player1));
    }
    
    @Test
    public void winningPlayer2(){//Tests that player 1 can win.
        board = new Board(15);
        for(int i  = 0; i < 5; i++)
            board.player2[0][i] = true;
        assertEquals(true, board.win(board.player2));
    }
    
    @Test
    public void correct_status(){
        //Checks that board reports the correct status when there is a conflicting scenario
        //Like that of repeating coordinates and coordinates outside of the graphic construction of the board
        board = new Board(15);
        board.addDisk(10,250);
        assertEquals(1, board.getStatus());
        board.addDisk(300,300);
        board.addDisk(300,300);
        assertEquals(2, board.getStatus());
    }
    
    @Test
    public void correctly_placed_disk_player1()
    {
      //Checks that in the turn of player 1 his selection for disc is assigned the correct spot in the array for player 1.
    
      board = new Board(15);
      board.addDisk(45,45);
      assertEquals(true, board.player1Use(0,0));
    }
    
    @Test
    public void correctly_placed_disk_player2()
    {
      //Checks that in the turn of player 2 his selection for disc is assigned the correct spot in the array for player 2.
      board = new Board(15);
      board.addDisk(300,300);
      board.addDisk(45,45);
      assertEquals(true, board.player2Use(0,0));
    }
  }
