import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.Font;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.sound.sampled.*;
import java.io.*;
import javax.swing.*;

/**
 * Frame class for the graphical user interface of connect five.
 * Controller for handling events that affect the model and the view.
 *
 * @author Edgar Padilla
 * @Co-authors: Oscar Galindo Mario Delgado:
 */
@SuppressWarnings("serial")
public class ConnectFive extends JFrame
{
    /**
     * Board model
     */
    private Board board;
    /**
     * Label containing message to user
     */
    private JLabel message;
    /**
     * Panel for the <code>board<code> to be displayed on the GUI
     * frame.
     */
    private BoardPanel boardPanel;

    /**
     * Boolean that indicates if a game is currently being played
     */
    private boolean playing;

    /** Activates mute of sounds */
    private boolean mute;

    /**
     * Constructor that initializes and adds all the components of the frame
     * including anonymous classes for the handlers.
     */
    public ConnectFive()
    {
        setTitle("Connect Five");
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        getContentPane().setLayout(new BorderLayout());

        //adding buttons (top)
        JPanel  boardSizePanel = new JPanel(new GridLayout(2, 3, 5 , 5));
        JButton largeBoard = new JButton("Board Size (15x15)");
        JButton mediumBoard = new JButton("Board Size (12x12)");
        JButton smallBoard = new JButton("Board Size (9x9)");
        JButton playGame = new JButton("Play Game");
        JButton change = new JButton("Change Color");
        JButton muting = new JButton("Mute");
        for (JButton button: new JButton[] { largeBoard, mediumBoard, smallBoard, change, playGame, muting })
        {
            button.setFocusPainted(true);
            boardSizePanel.add(button);
        }
        getContentPane().add(boardSizePanel, BorderLayout.NORTH);
        board = new Board(15);
        playing = false;
        mute = false;

        //create Board GUI instance (center)
        boardPanel = new BoardPanel(board); //initializing the panel for the model
        boardPanel.setPreferredSize(new Dimension(670, 670));
        getContentPane().add(boardPanel, BorderLayout.CENTER);

        //creating message label (bottom)
        JPanel statusPanel = new JPanel();
        statusPanel.setBackground(Color.DARK_GRAY);
        statusPanel.setPreferredSize(new Dimension(670, 50));
        message = new JLabel("Welcome to Connect Five");
        message.setForeground(Color.WHITE);
        message.setFont(new Font(message.getName(), Font.BOLD, 28));
        statusPanel.add(message);
        getContentPane().add(statusPanel, BorderLayout.SOUTH);


        //Actions for the three different buttons.
        //Actions for (15x15) button
        largeBoard.addActionListener(e ->
        {
           buttonSound();
           gameButton(15);
        });

        //Actions for (12x12) button
        mediumBoard.addActionListener(e ->
        {
           buttonSound();
           gameButton(12);
        });

        //Actions for (9x9) button
        smallBoard.addActionListener(e ->
        {
           buttonSound();
           gameButton(9);
        });

        //Actions for play game button
         playGame.addActionListener(e ->
        {
           if(playing)
           {
              play();
           }
           else if(!playing)
           {
              playing = true;
              play();
              boardPanel.setPlaying(true);
           }
         });
         message.setText("Please choose your table mode.");

        //Actions for change color button
        change.addActionListener(e ->
        {
           boolean foundColor = true;
           String [] colors = {"Green","Blue","Yellow","Red","Black","Gray","Orange","Purple"};
           String[] possibilities = {"hey","no"};//Simple initialization
           String colorPlayer1 = BoardPanel.getPlayer1ColorName();
           String colorPlayer2 = BoardPanel.getPlayer2ColorName();
           if(playing)
           {
              String inputColor = "";
              int r = 0, g = 0, b = 0;
              possibilities = new String[6];
              for(int i = 0, j= 0; i < 6 && j < colors.length; j++)
              {
                  if(!(colorPlayer1.equals(colors[j])) && !(colorPlayer2.equals(colors[j])))//Adds the options to be displayed if they are not used.
                  {
                       possibilities[i] = colors[j];
                       i += 1;
                  }
              }
              if(board.getNumberOfDisks() % 2 == 0)
              {
                  inputColor = (String) JOptionPane.showInputDialog(null, "Color","Player 1 please choose a color.", JOptionPane.QUESTION_MESSAGE, null, possibilities,colorPlayer1); // Gets the color choosen by the user.
              }
              else if(board.getNumberOfDisks() % 2 == 1)
              {
                  inputColor = (String) JOptionPane.showInputDialog(null, "Color","Player 2 please choose a color.", JOptionPane.QUESTION_MESSAGE, null, possibilities,colorPlayer2); // Gets the color choosen by the user.
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
                  playcolorMod();
               }
            }
         });

        //Actions when the mute button is pressed
        muting.addActionListener(e ->
        {
           if(mute)
               mute = false;

           else if(!mute)
              mute = true;
        });

        //Actions when the mousd is clicked
        boardPanel.addMouseListener(new MouseAdapter()
        {
            public void mousePressed(MouseEvent e)
            {
                if(playing)
                {
                  board.addDisk(e.getX(), e.getY());
                  play();
                  boardPanel.drawBoard();
                  getContentPane().repaint();
                }
                else if(!playing)
                {
                  errorSound();
                  message.setFont(new Font(message.getName(), Font.BOLD, 22));
                  message.setText("Please choose a new game board and press 'play game'.");
                }
            }//end mouse pressed
        });
    }

    /**
     * Initializes the frame for the GUI and starts the application.
     */
    public static void main(String[] args)
    {
        ConnectFive cf = new ConnectFive();
        cf.setVisible(true);
        cf.pack();
    }

    /**
     * General Implementation for all buttons that are related to board
     * @param size: int
     */
    public void gameButton(int size)
    {
        if(!playing)
        {
            board = new Board(size);
            boardPanel.setBoard(board);
            message.setText(size+"x"+size); //initializing the panel for the model
            getContentPane().add(boardPanel, BorderLayout.CENTER);
            boardPanel.drawBoard();
            getContentPane().repaint();
        }
        else if (playing)
        {
          int input = JOptionPane.showConfirmDialog(null, "Will you like to start a new game?");
          // 0=yes, 1=no, 2=cancel
          if(input == 0)
          {
             board = new Board(size);
             boardPanel.setBoard(board);
             getContentPane().add(boardPanel, BorderLayout.CENTER);
             boardPanel.drawBoard();
             getContentPane().repaint();
             playing = true;
             play();
           }
        }
    }

    /**
     * Initializes the game sequence and checks the status after selection of discs.
     */
    public void play()
    {
        if(board.getNumberOfDisks() == (board.size()*board.size()))
        {
            playing = false;
            message.setText("It is a Tie!");
        }
        else
        {
            message.setFont(new Font(message.getName(), Font.BOLD, 28));
            int status = board.getStatus();
            if(status == 1)
            {
               errorSound();
               message.setText("Outside of boundaries location, try again.");
            }
            else if(status == 2)
            {
               errorSound();
               message.setText("Coordinate already used, try again.");
            }
            else if (status == 3)
            {
               message.setText("Congratulations Player 1, you won!");
               playWinSound();
               playing = false;
            }
            else if(status == 4)
            {
               message.setText("Congratulations Player 2, you won!");
               playWinSound();
               playing = false;
            }
            else if(status == 0)
            {
               diskAddedsound();
               if(board.getNumberOfDisks() % 2 == 0) {message.setText("Player 1 please choose a new position!");}
               else if (board.getNumberOfDisks() % 2 == 1) {message.setText("Player 2 please choose a new position!");}
            }
        }
    }

    /**
     * Initializes the sound that indicates a player has won.
     */
    public void playWinSound()
    {
        InputStream pathSoundFile = getClass().getResourceAsStream("bellringing.wav");
        playSound(pathSoundFile);
    }

    /**
     * Initializes the sound that indicates a button has been pressed.
     */
    public void buttonSound()
    {
         InputStream pathSoundFile = getClass().getResourceAsStream("Button.wav");
         playSound(pathSoundFile);
    }

    /**
     * Initializes the sound that indicates a disk has been set in the table.
     */
    public void diskAddedsound()
    {
         InputStream pathSoundFile = getClass().getResourceAsStream("diskplacement.wav");
         playSound(pathSoundFile);
    }

    /**
     * Initializes the sound that indicates an error was made.
     */
    public void errorSound()
    {
         InputStream pathSoundFile = getClass().getResourceAsStream("Error.wav");
         playSound(pathSoundFile);
    }

    /**
     * Initializes the sound that indicates a sound change was successful.
     */
    public void playcolorMod()
    {
        InputStream pathSoundFile = getClass().getResourceAsStream("colorChange.wav");
        playSound(pathSoundFile);
    }

    /**
     * Implements/plays the desired sound.
     */
    public void playSound(InputStream access)
    {
        if(!mute)
        {
          try{
              InputStream bufferedIn = new BufferedInputStream(access);
              AudioInputStream audioIn = AudioSystem.getAudioInputStream(bufferedIn);
              Clip clip = AudioSystem.getClip();
              clip.open(audioIn);
              clip.start();
            }
          catch(UnsupportedAudioFileException | IOException | LineUnavailableException e1){
              System.out.println("Selected Audio File is not compatible/available.");};
        }
    }
}
