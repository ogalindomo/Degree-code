import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JPanel;

/**
 * Class that acts as the Panel to display the model (board).
 *
 * @author Edgar Padilla, Oscar Galindo, Mario Delgado
 */
@SuppressWarnings("serial")
public class BoardPanel extends JPanel
{

    /** Board model. */
    private static Board board;
    
    /** Coordinates where the lines of the program end and start */
    private static int startPoint, endPoint;
    
    /** Change in number of pixels of each line in the board */
    private static int boardChange;
    
    /** Graphical size of disks */
    private static int diskSize;
    
    /** Color for player 1 */
    private static Color player1Color;
    
    /** Color for player 2 */
    private static Color player2Color;
    
    /** Stores the name of the color assigned to player 1 */
    private static String player1ColorName;
    
    /** Stores the name of the color assigned to player 2 */
    private static String player2ColorName;
    
    
    /**
     * Creates an instance of this panel for the discs board.
     * @param Board board (once the board panel is instatiated it must receive a reference to a board).
     */
    public BoardPanel(Board board)
    {
        super(true);
        this.board = board;
        setOpaque(true);
        setBackground(new Color(238,238,238));
        setGraphics();
        player1Color = new Color(237,90,76);
        setPlayer1ColorName("Red");
        player2Color = new Color(0,0,255);
        setPlayer2ColorName("Blue");
    }
    
    /** Allows the modification of the board dynamically, as the execution flows
     *  @param Board b (new board to model).
     */
    public void setBoard(Board b)
    {
       this.board = b;  
       setGraphics();
    }
    
    /** 
      *  Sets the graphic description of the board based on size 
      */
    public void setGraphics()
    {
        if(board.size() == 15)
        {
           startPoint = 25;//Each number represents a coordinate in the x/y graphical plane.
           endPoint = 625;
           boardChange = 40;
           diskSize = 30;
        }
        else if(board.size() == 12)
        {
           startPoint = 25;
           endPoint = 625;
           boardChange = 50;
           diskSize = 40; 
        }
        else if(board.size() == 9)
        {
           startPoint = 25;
           endPoint = 628; 
           boardChange = 67;
           diskSize = 59;
        } 
    }

    /**
     * Draws the discs board by calling the paint method.
     */
    public void drawBoard()
    {
        repaint();
    }

    /**
     * Paints the discs board to the panel.
     * @param Graphics g (graphics that represent the graphical space of the board panel).
     */
    public void paint(Graphics g)
    {
        g.setColor(Color.BLACK);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setStroke(new BasicStroke(2));
        for(int i = 0; i <= board.size(); i++)
        {
            //vertical lines
            g.setColor(Color.BLACK);
            g.drawLine(startPoint + i * boardChange, startPoint, startPoint + i * boardChange, endPoint);
            
            //horizontal
            g.drawLine(startPoint, startPoint + i * boardChange , endPoint, startPoint + i * boardChange);
            
            if(i != board.size())
            {
               for(int j = 0; j < board.size() ; j++)
               {
                 if(board.player1Use(j,i))
                 {
                   g.setColor(player1Color);
                   g.fillOval((startPoint+5) + boardChange*j, (startPoint+5) + boardChange*i, diskSize, diskSize);
                 }
                 else if(board.player2Use(j,i) && i != 15)
                 {
                   g.setColor(player2Color);
                   g.fillOval((startPoint+5) + boardChange*j, (startPoint+5) + boardChange*i, diskSize, diskSize);
                 }
               }
             }         
        }
    }
    
    public int getStartPoint() {return startPoint;}
    
    public int getChange() {return boardChange;}
    
    /** 
     * The function sets to a different color the color to draw Disks of player 1. 
     * @param int r sets the red degree of the desired color.
     * @param int g sets the green degree of the desired color.
     * @param int b sets the blue degree of the desired color.
     */
    public void setPlayer1Color(int r, int g, int b)
    {
        player1Color = new Color(r,g,b);
    }
    
    /** 
     * The function sets to a different color the color to draw Disks of player 2. 
     * @param int r sets the red degree of the desired color.
     * @param int g sets the green degree of the desired color.
     * @param int b sets the blue degree of the desired color.
     */
    public void setPlayer2Color(int r, int g, int b)
    {
        player2Color = new Color(r,g,b);
    }
    
    /** 
      * This setter reports the color assigned to player 1. 
      * @return Color player1Color (Color for player 1).
      */
    public Color getPlayer1Color(){return player1Color;}
    
    /** 
      * This setter reports the color assigned to player 2. 
      * @return Color player1Color (Color for player 2).
      */
    public Color getPlayer2Color(){return player2Color;}
    
    /** 
      * This setter replaces the name of the color assigned to player 1.
      * @param String colorName (represents the name of the selected color).
      */
    public void setPlayer1ColorName(String colorName){ player1ColorName = colorName;}
    
    /** 
      * This setter replaces the name of the color assigned to player 2.
      * @param String colorName (represents the name of the selected color).
      */
    public void setPlayer2ColorName(String colorName){ player2ColorName = colorName;}
    
    /**
      * This getter reports the name of the color assigned to player 1. 
      * @return String player1ColorName (word name of the color for player 1).
      */
    public static String  getPlayer1ColorName(){ return player1ColorName ;}
    
    /**
      * This getter reports the name of the color assigned to player 2. 
      * @return String player1ColorName (word name of the color for player 2).
      */
    public static String getPlayer2ColorName(){ return player2ColorName ;}
}
