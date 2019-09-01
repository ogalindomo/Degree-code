import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;

import javax.swing.JPanel;

/**
 * Class that acts as the Panel to display the model (board) as a grid of 15 by 15.
 *
 * @author Edgar Padilla
 * @Co-authors: Oscar Galindo Mario Delgado
 */
@SuppressWarnings("serial")
public class BoardPanel extends JPanel
{

    /** Board model. */
    private Board board;
    
    /** Playing indicator */
    private boolean playing;
    
    /** Coordinates where the lines of the program end and start */
    private int startPoint, endPoint;
    
    /** Change in number of pixels of each line in the board */
    private int boardChange;
    
    /** Graphical size of disks */
    private int diskSize;
    /**
     * Creates an instance of this panel for the discs board.
     */
    public BoardPanel(Board board)
    {
        super(true);
        this.board = board;
        setOpaque(true);
        setBackground(new Color(238,238,238));
        if(board.size() == 15)
        {
           startPoint = 25;
           endPoint = 625;
           boardChange = 40;
           diskSize = 30;
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
     *
     * @param discs Current board to be painted.
     */
    public void drawBoard()
    {
        repaint();
    }

    /**
     * Paints the discs board to the panel.
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
            
            if(playing && i != board.size())
            {
               for(int j = 0; j < board.size() ; j++)
               {
                 if(board.player1Use(j,i))
                 {
                   g.setColor(Color.RED);
                   g.fillOval((startPoint+5) + boardChange*j, (startPoint+5) + boardChange*i, diskSize, diskSize);
                 }
                 else if(board.player2Use(j,i) && i != 15)
                 {
                   g.setColor(Color.BLUE);
                   g.fillOval((startPoint+5) + boardChange*j, (startPoint+5) + boardChange*i, diskSize, diskSize);
                 }
               }
             }         
        }
    }
    
    /** The function indicates to the execution if a game is being played */
    public void setPlaying(boolean answer){playing = answer;}
}
