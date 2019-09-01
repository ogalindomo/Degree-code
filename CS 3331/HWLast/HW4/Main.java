package HW4;
import java.awt.event.*;
import javax.sound.sampled.*;
import java.io.*;
import javax.swing.*;
import java.awt.event.MouseAdapter;
import java.awt.Color;
/**
 * Frame class for the graphical user interface of connect five.
 * Controller for handling interactions between the view components and the model.
 *
 * @author Edgar Padilla, Oscar Galindo, Mario Delgado:
 *  
 */
public class Main 
{
    /** Keeps the reference to the GUI used throughout execution */
    protected GUI screen;
   
    /** Keeps the reference to the AI used throughout execution */
    protected AI secondPlayer;
    
    /** Keeps the reference to the board used throughout execution */
    protected Board board;
    
    /** Keeps the reference to the board panel used throughout execution */
    protected BoardPanel boardPanel;
    
    /** Keeps track of the activation of the AI */
    protected boolean artificialActive;
    
    /** Stores the status of execution(true if the game is going).*/
    protected boolean playing;
    
    /** Boolean that indicates if the secret color should appear as option or not */
    protected boolean secretColor;
    
    /** Keeps trace of the current gamemode being played */
    protected String gamemode;
    
    /** Initializes the listener of all JMenuItem & JButton elements of the GUI(view). */
    protected Listener ear;
    
    /** Initializations of the names of the two possible players. */
    protected String player1Name = "", player2Name = "";
    
    public static void main(String[]args)
    {
        new Main();
    }
    
    /** Initialization of the Class with just the required methods for an extension. */
    protected Main()
    {
       board = new Board(15);//Instantiates the board
       boardPanel = new BoardPanel(board); 
       secondPlayer = new EasyAI(board); 
       player1Name = "Player 1";
       player2Name = "Player 2"; 
    }
    
    /** Initialization of the Class with the needed parameters to play with this level of implementation. */
    protected Main(boolean visbility)
    {
        board = new Board(15);//Instantiates the board
        boardPanel = new BoardPanel(board);
        screen = new GUI(board,boardPanel);
        ear = new Listener();
        screen.addListener(ear);
        screen.setBoardListener(ear);
        secondPlayer = new EasyAI(board);
        player1Name = "Player 1";
        player2Name = "Player 2";
        gamemode = "";
        screen.setVisible(visbility);
        screen.pack();
    }
    
    /**
     *  Listener class for the graphical user interface of connect five.
     *  Listener for connecting decision-making methods to action-making methods.
     */
    protected class Listener extends MouseAdapter implements ActionListener
    {
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
            String colorButton = getClass().getResource("color_button_big.png").toString();
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
            else if(input.equals("Multiplayer"))
                playMode(input);//The gamemode selected is passed as a literal string to the method.
            else if(input.equals("Singleplayer"))
                playMode(input);
            else if(input.equals("Change Name"))
                changeName();
            else if(input.equals("Change Color") || colorButton.equals(source))
                changeColor();
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
    }
    
    /**
     *  Activates the conditions for the play game button.
     */
    protected void playPressed()
    {
        if(playing)
        {
            play();
        }
        else if(!playing)
        {
            playing = true;
            play();
        }
        screen.playEffect(5);
    }
    
    /**
     *  Activates the change name mechanism.
     */
    protected void changeName()
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
                    secretColor = true;
                else 
                    secretColor = false;
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
    protected void playMode(String mode)
    {
        if(!(mode.equals(gamemode)))// If the game mode button pressed is different than the current game mode then the execution begins, else, nothing happens.
        {
            if(playing)//If the game is active then a confirmation dialog is send to the user.
            {
                int input = JOptionPane.showConfirmDialog(null, "Will you like to change game mode?");//Asks the user if he/she wishes to change gamemode.
                if(input != 0) {return;}
            }
            playing = false;
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
    protected void gameButton(int size)
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
    protected void play()
    {
        if(board.getNumberOfDisks() == (board.size()*board.size()))
        {
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
               playing = false;
            }
            else if(status == 4)
            {
               if(artificialActive) //Differentiated message in case the AI won.
                   screen.setMessage("AI beat you!");
               else
                   screen.setMessage("Congratulations "+player2Name+", you won!");
               playing = false;
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
      * Implements all the necessary dialogs to change color 
      */
    protected void changeColor()
    {
        String [] colors = {"Green","Blue","Yellow","Red","Black","Gray","Orange","Purple","Oscar"};
        String[] possibilities = {"hey","no"};//Simple initialization
        String colorPlayer1 = BoardPanel.getPlayer1ColorName();
        String colorPlayer2 = BoardPanel.getPlayer2ColorName();
        if(playing)
        {
            String inputColor = "";
            int r = 0, g = 0, b = 0;
            if(secretColor && board.getNumberOfDisks() % 2 == 0)
               possibilities = new String[7];
            else
               possibilities = new String[6];
            for(int i = 0, j= 0; i < possibilities.length && j < colors.length; j++)
            {
                if(!(colorPlayer1.equals(colors[j])) && !(colorPlayer2.equals(colors[j])))//Adds the options to be displayed if they are not used.
                {
                     possibilities[i] = colors[j];
                     i += 1;
                }
            }
            if(board.getNumberOfDisks() % 2 == 0)
            {
                inputColor = (String) JOptionPane.showInputDialog(null, "Color",player1Name+" please choose a color.", JOptionPane.QUESTION_MESSAGE, null, possibilities,colorPlayer1); // Gets the color choosen by the user.
            }
            else if(board.getNumberOfDisks() % 2 == 1)
            {
                inputColor = (String) JOptionPane.showInputDialog(null, "Color",player2Name+" please choose a color.", JOptionPane.QUESTION_MESSAGE, null, possibilities,colorPlayer2); // Gets the color choosen by the user.
            }
            if(inputColor != null)
            {
                switch(inputColor)
                {
                    case "Green":
                    r = 140; 
                    g = 197;
                    b = 141;                   
                    break;
               
                    case "Blue":
                    r = 0;
                    g = 0;
                    b = 255;
                    break;   
               
                    case "Yellow":
                    r = 240;
                    g = 226;
                    b = 84;
                    break;  
                 
                    case "Red":
                    r = 237;
                    g = 90;
                    b = 76;
                    break; 
               
                    case "Black":
                    r = 0;
                    g = 0;
                    b = 0;
                    break;
                    
                    case "Gray":
                    r = 128;
                    g = 128;
                    b = 128;
                    break;
                    
                    case "Orange":
                    r = 237;
                    g = 166;
                    b = 79;
                    break;
                  
                    case "Purple":
                    r = 125;
                    g = 110;
                    b = 246;
                    break;
                    
                    case "Oscar":
                    r = 55;
                    g = 120;
                    b = 117;
                    break;
                }
                Color provisional = new Color(r,g,b);
                if(board.getNumberOfDisks() % 2 == 0 && !inputColor.equals("") && boardPanel.getPlayer2Color().getRGB() != provisional.getRGB())
                {
                    boardPanel.setPlayer1Color(r,g,b);
                    boardPanel.setPlayer1ColorName(inputColor);
                }
                else if(board.getNumberOfDisks() % 2 == 1 && !inputColor.equals("") && boardPanel.getPlayer1Color().getRGB() != provisional.getRGB())
                { 
                    boardPanel.setPlayer2Color(r,g,b);
                    boardPanel.setPlayer2ColorName(inputColor);
                }
                screen.playEffect(6);      
             }
        }
        else
            screen.setMessage("To use this feature please start a game.");
    }
    
    /** Converts the graphical coordinates from mousePressed
     *  into coordinates of the arrays.
     *  @param int coordinate (graphical coordinate detected by the mouse listener).
     *  @return int converted coordinate.
     */
    protected int convert(int coordinate) 
    { 
        return (coordinate - boardPanel.getStartPoint())/boardPanel.getChange();
    }
}
