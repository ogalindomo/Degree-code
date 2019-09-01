import java.awt.event.*;
import javax.sound.sampled.*;
import java.io.*;
import javax.swing.*;
import java.awt.event.MouseAdapter;
/**
 * Frame class for the graphical user interface of connect five.
 * Controller for handling interactions between the view components and the model.
 *
 * @author Edgar Padilla, Oscar Galindo, Mario Delgado:
 *  
 */
public class Main  extends MouseAdapter
{
    /** Keeps the reference to the GUI used throughout execution */
    private static GUI screen;
   
    /** Keeps the reference to the AI used throughout execution */
    private static AI secondPlayer;
    
    /** Keeps the reference to the board used throughout execution */
    private static Board board;
    
    /** Keeps the reference to the board panel used throughout execution */
    private static BoardPanel boardPanel;
    
    /** Keeps track of the activation of the AI */
    private static boolean artificialActive;
    
    /** Stores the status of execution(true if the game is going).*/
    private static boolean playing;
    
    /** Keeps trace of the current gamemode being played */
    private static String gamemode;
    
    /** Initializes the listener of all JMenuItem & JButton elements of the GUI(view). */
    private static Listener ear;
    
    private static String player1Name = "", player2Name = "";
    
    /** 
     * Initializes the game.
     */
    public static void main(String[]args)
    {
        board = new Board(15);//Instantiates the board
        boardPanel = new BoardPanel(board);
        screen = new GUI(board,boardPanel);
        ear = new Listener();
        secondPlayer = new EasyAI(board);
        player1Name = "Player 1";
        player2Name = "Player 2";
        gamemode = "";
        screen.setVisible(true);
        screen.pack();
    }
    
    /**
     *  Listener class for the graphical user interface of connect five.
     *  Listener for connecting decision-making methods to action-making methods.
     */
    static class Listener implements ActionListener
    {
        /**
         *  Empty-argument initializer that connects the instance created of this class as the listener to the GUI class.
         */
        public Listener()
        {
            screen.addListener(this);//Adds the instance created of the listener as the hearing of the elements in the GUI class.
        }
        
        /**
         *  Initializes the actions if the action listener of an item of the menu is triggered.
         *  @param ActionEvent e (occurs when a button is graphically pressed).
         */
        public void actionPerformed(ActionEvent e)
        {
            AbstractButton prov = (AbstractButton) e.getSource();//What triggered the events is converted into an abstract button
            String input = prov.getText();//From the type AbstractButton the string the represents the text of the button is extracted
            String source_blue = getClass().getResource("blue_button_big.png").toString();//Reference to the graphical face(image) of all possible button.
            String source_yellow = getClass().getResource("yellow_button_big.png").toString();
            String source_oscar = getClass().getResource("oscar_button_big.png").toString();
            String easyButton = getClass().getResource("rabbit_button_big.png").toString();
            String mediumButton = getClass().getResource("medium_button_big.png").toString();
            String difficultButton = getClass().getResource("difficult_button_big.png").toString();
            String playButton = getClass().getResource("play_button.png").toString();
            String aiClass = null;
            String classButton = null;
            String source = null;
            if(prov.getIcon() != null)
            {
                source = prov.getIcon().toString();
                aiClass = secondPlayer.getClass().toString();
            }
            if(input.equals("15x15") || source_blue.equals(source)) 
                gameButton(15);
            else if(input.equals("12x12") || source_yellow.equals(source))
                gameButton(12);
            else if(input.equals("9x9") || source_oscar.equals(source))
                gameButton(9);
            else if(input.equals("Play Game") || playButton.equals(source))
                playPressed();
            else if(input.equals("MultiPlayer"))
                playMode(input);//The gamemode selected is passed as a literal string to the method.
            else if(input.equals("Singleplayer"))
                playMode(input);
            else if(input.equals("Change Name"))
                changeName();
            else if(input.equals("Easy") || easyButton.equals(source))
            {
                if(!(aiClass.equals("class EasyAI")) && playing && artificialActive)
                {
                    int answer = JOptionPane.showConfirmDialog(null, "Will you like to change AI difficulty to easy?");
                    if(answer == 0)
                        secondPlayer = new EasyAI(board);
                    screen.playEffect(5);
                }
                else
                {
                    secondPlayer = new EasyAI(board);
                    screen.setMessage("Difficulty selected for AI: Easy");
                    screen.playEffect(5);
                }
            }
            else if(input.equals("Medium") || mediumButton.equals(source))
            {
                if(!(aiClass.equals("class MediumAI")) && playing && artificialActive)
                {
                    int answer = JOptionPane.showConfirmDialog(null, "Will you like to change AI difficulty to medium?");
                    if(answer == 0)
                        secondPlayer = new MediumAI(board);
                    screen.playEffect(5);
                }
                else
                {
                    secondPlayer = new MediumAI(board);
                    screen.setMessage("Difficulty selected for AI: Medium");
                    screen.playEffect(5);
                }
            }
            else if(input.equals("Difficult") || difficultButton.equals(source))
            {
                if(!(aiClass.equals("class DifficultAI")) && playing && artificialActive)
                {
                    int answer = JOptionPane.showConfirmDialog(null, "Will you like to change AI difficulty to Difficult?");
                    if(answer == 0)
                        secondPlayer = new DifficultAI(board);
                    screen.playEffect(5);
                }
                else
                {
                    secondPlayer = new DifficultAI(board);
                    screen.setMessage("Difficulty selected for AI: Difficult");
                    screen.playEffect(5);
                }
            }
        }
    }
    
    /**
     *  Activates the conditions for the play game button.
     */
    public static void playPressed()
    {
        if(playing)
        {
            play();
        }
        else if(!playing)
        {
            screen.setPlaying(true);
            playing = true;
            play();
        }
        screen.playEffect(5);
    }
    
    private static void changeName()
    {
        if(playing)
        {
            int numDisks = board.getNumberOfDisks();
            String prov = "";
            if(numDisks % 2 == 0)
            {
                prov = (String)JOptionPane.showInputDialog(null,"Please enter a new name for player 1.");
                player1Name = prov;
                if(player1Name.equals("Oscar"))
                    screen.setSecretColor(true);
                else 
                    screen.setSecretColor(false);
                play();
            }
            else    
            {
                prov = (String)JOptionPane.showInputDialog(null,"Please enter a new name for player 2.");
                player2Name = prov;
                play();
            }
        }
        else
            screen.setMessage("To use this feature please start a game.");
        screen.playEffect(5);
    }
   
    /**
     *  Activates the condition for the mutiplayer/singleplayer game buttons.
     *  @param String gamemode (Indicates if the game mode selected was singleplayer).
     */
    private static void playMode(String mode)
    {
        if(!(mode.equals(gamemode)))// If the game mode button pressed is different than the current game mode then the execution begins, else, nothing happens.
        {
            if(playing)//If the game is active then a confirmation dialog is send to the user.
            {
                int input = JOptionPane.showConfirmDialog(null, "Will you like to change game mode?");//Asks the user if he/she wishes to change gamemode.
                if(input != 0) {return;}
            }
            playing = false;
            screen.setPlaying(false);
            board = new Board(board.size());
            screen.setBoard(board);
            if(mode.equalsIgnoreCase("Singleplayer"))
                artificialActive = true;
            else 
                artificialActive = false;
            gamemode = mode;
            screen.repaint();
            screen.setMessage("Please choose a board size and press 'play game'."); 
        }
        if(artificialActive)//If the AI is active then it receives the new board on which the game will be played.
              secondPlayer.setBoard(board);
        screen.playEffect(5);
    }
    
    /**
     *  Activates the change in board size graphically and logically.
     *  @param int size (size of the board selected).
     */
    private static void gameButton(int size)
    {
        if(!playing) //If the user changes the board size and the game is not executing the execution shows the new board in the GUI.
        {
            board = new Board(size);
            screen.setBoard(board);
            screen.repaint();
        }
        else if (playing) //If the user changes the board size while the game is executing this is ran.
        {
          int input = JOptionPane.showConfirmDialog(null, "Will you like to start a new game?");
          // 0=yes, 1=no, 2=cancel
          if(input == 0)
          {
             board = new Board(size);
             screen.setBoard(board);
             screen.repaint();
             playing = true;
             screen.setPlaying(true);
             play();
           }
        }  
        if(artificialActive)//If the AI is active then it receives the new board on which the game will be played.
              secondPlayer.setBoard(board);
        screen.playEffect(5);
    }
    
    /**
     *  Reports the status of each move and the status of the board,
     *  if a player wins then the game is stopped.
     */
    public static void play()
    {
        if(board.getNumberOfDisks() == (board.size()*board.size()))
        {
            screen.setPlaying(false);
            playing = false;
            screen.setMessage("It is a Tie!");
        }
        else
        {
            int status = board.getStatus();
            screen.playEffect(status);//This plays the sound effect based on the status of the board.
            if(status == 1)
            {
               screen.setMessage("Outside of boundaries location, try again.");
            }
            else if(status == 2)
               screen.setMessage("Coordinate already used, try again.");
            
            else if (status == 3)
            {
               screen.setMessage("Congratulations "+player1Name+", you won!");
               screen.setPlaying(false);
               playing = false;
            }
            else if(status == 4)
            {
               if(artificialActive) //Differentiated message in case the AI won.
                   screen.setMessage("AI beat you!");
               else
                   screen.setMessage("Congratulations "+player2Name+", you won!");
               playing = false;
               screen.setPlaying(false);
            }
            else if(status == 0)
            {
               if(board.getNumberOfDisks() % 2 == 0) 
               {
                   screen.setMessage(player1Name + " please choose a new position!");
               }
               else if(!artificialActive)
               {
                   screen.setMessage(player2Name + " please choose a new position!");
               }
            }
        }
    }
   
    /**
     *  Initializes the actions to take when the mouse is pressed.
     *  @param MouseEvent e (occurs when the mouse is pressed).
     */
    public void mousePressed(MouseEvent e)
    {
        if(playing)
        {
            board.addDisk(convert(e.getX()), convert(e.getY()));
            play();
            if(artificialActive && board.getStatus() == 0)
            {
                 secondPlayer.makeMove();
                 play();
            }
            screen.repaint();
        }
        else if(!playing)
        {
            screen.playEffect(1);
            screen.setMessage("Please choose a board size and press 'play game'.");
        }    
    }
    
    /** Converts the graphical coordinates from mousePressed
     *  into coordinates of the arrays.
     *  @param int coordinate (graphical coordinate detected by the mouse listener).
     *  @return int converted coordinate.
     */
    public int convert(int coordinate) 
    { 
        return (coordinate - boardPanel.getStartPoint())/boardPanel.getChange();
    }
}
