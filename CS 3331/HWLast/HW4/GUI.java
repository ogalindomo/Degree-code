package HW4;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.Font;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.*;
import javax.sound.sampled.*;
import java.io.*;
import javax.swing.*;
import java.nio.*;
/**
 * Frame class for the graphical user interface of connect five.
 * View for showing the state of the model.
 *
 * @author Edgar Padilla, Oscar Galindo, Mario Delgado: 
 *  
 */
@SuppressWarnings("serial")
public class GUI extends JFrame implements ActionListener
{
    /**
     * Board model
     */
    protected Board board;
    
    /**
     * Label containing message to user
     */
    protected JLabel message;
    
    /**
     * Panel for the <code>board<code> to be displayed on the GUI
     * frame.
     */
    protected BoardPanel boardPanel;
    
    /** Instance of the menu bar in the graphical interface */
    protected JMenuBar menuBar;
    
    /** Instances of all sub-menus in the menu bar of the GUI. */
    protected JMenu gamemode, options, settings, aiDifficulty;
    
    /** Instances of all menu items for each sub-menu of the menu bar in GUI class. */
    protected JMenuItem fifteen, twelve, nine, muted, color, aiEasy, aiMedium, aiDifficult, single, multi, changeName;
    
    /** Initialization variable of the tool bar of the GUI. */
    protected JToolBar bar;
    
    /** Elements of the tool bar in the graphical interface. */
    protected JButton play, start, board_color, board_fifteen, board_twelve, board_nine, easyButton, mediumButton, difficultButton;
    
    /** Boolean that indicates if the player wishes to listen sounds */
    protected boolean  mute;
   
    /**
     * Constructor that initializes and adds all the components of the frame
     * including anonymous classes for the handlers.
     * @param Board board (receives the model representation of the game).
     * @param BoardPanel panel (receives the instance of the panel that will draw the board).
     */
    public GUI(Board board, BoardPanel panel)
    {
        setTitle("Connect Five");
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        getContentPane().setLayout(new BorderLayout());
        this.board = board;
        this.boardPanel = panel;
        
        menuBar = new JMenuBar();
        gamemode = new JMenu("Game Mode");
        options = new JMenu("Board Size");
        settings = new JMenu("Settings");
        aiDifficulty = new JMenu("AI Difficulty");
        bar = new JToolBar("Connect Five",JToolBar.VERTICAL);
        
        bar.setFloatable(true);//Allows the bar to be moved around on the screen.
        
        //Accelerators, graphics and Mnemonics for the menu items are set here.
        fifteen = new JMenuItem("15x15", new ImageIcon(getClass().getResource("blue_button.png")));
        fifteen.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_1, ActionEvent.ALT_MASK));
        fifteen.setMnemonic(KeyEvent.VK_A);
        
        twelve = new JMenuItem("12x12", new ImageIcon(getClass().getResource("yellow_button.png")));
        twelve.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_2, ActionEvent.ALT_MASK));
        twelve.setMnemonic(KeyEvent.VK_B);
        
        nine = new JMenuItem("9x9", new ImageIcon(getClass().getResource("oscar_button.png")));
        nine.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_3, ActionEvent.ALT_MASK));
        nine.setMnemonic(KeyEvent.VK_C);
        
        muted = new JMenuItem("Mute", new ImageIcon(getClass().getResource("mute_button.png")));
        muted.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, ActionEvent.SHIFT_MASK));
        muted.setMnemonic(KeyEvent.VK_M);
        
        color = new JMenuItem("Change Color", new ImageIcon(getClass().getResource("color_button.png")));
        color.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_C, ActionEvent.SHIFT_MASK));
        color.setMnemonic(KeyEvent.VK_C);
        
        aiEasy = new JMenuItem("Easy", new ImageIcon(getClass().getResource("rabbit_button.png")));
        aiEasy.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_E, ActionEvent.SHIFT_MASK));
        aiEasy.setMnemonic(KeyEvent.VK_E);
        
        aiMedium = new JMenuItem("Medium", new ImageIcon(getClass().getResource("medium_button.png")));
        aiMedium.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_M, ActionEvent.SHIFT_MASK));
        aiMedium.setMnemonic(KeyEvent.VK_M);
        
        aiDifficult = new JMenuItem("Difficult", new ImageIcon(getClass().getResource("difficult_button.png")));
        aiDifficult.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_H, ActionEvent.SHIFT_MASK));
        aiDifficult.setMnemonic(KeyEvent.VK_H);

        single = new JMenuItem("Singleplayer");
        single.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_S, ActionEvent.ALT_MASK));
        single.setMnemonic(KeyEvent.VK_S);
        
        multi = new JMenuItem("Multiplayer");
        multi.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_M, ActionEvent.ALT_MASK));
        multi.setMnemonic(KeyEvent.VK_M);
        
        changeName = new JMenuItem("Change Name");
        changeName.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_N, ActionEvent.ALT_MASK));
        changeName.setMnemonic(KeyEvent.VK_N);
        
        play = new JButton("Play Game");
        
        //Menu items added to their respective positions in the menu.
        menuBar.add(play);
        menuBar.add(gamemode);
        menuBar.add(options);
        menuBar.add(settings);
        gamemode.add(single);
        gamemode.add(multi);
        options.add(fifteen);
        options.add(twelve);
        options.add(nine);
        settings.add(color);
        settings.add(muted);
        settings.add(changeName);
        settings.add(aiDifficulty);
        aiDifficulty.add(aiEasy);
        aiDifficulty.add(aiMedium);
        aiDifficulty.add(aiDifficult);
        
        //Buttons for the toolbar are initialized.
        start = new JButton(new ImageIcon(getClass().getResource("play_button.png")));
        start.setPreferredSize(new Dimension(35,35));
        start.setToolTipText("Play Game");
        
        board_fifteen = new JButton(new ImageIcon(getClass().getResource("blue_button_big.png")));
        board_fifteen.setPreferredSize(new Dimension(35,35));
        board_fifteen.setToolTipText("New 15x15 board");
        
        board_twelve = new JButton(new ImageIcon(getClass().getResource("yellow_button_big.png")));
        board_twelve.setPreferredSize(new Dimension(35,35));
        board_twelve.setToolTipText("New 12x12 board");
        
        board_nine = new JButton(new ImageIcon(getClass().getResource("oscar_button_big.png")));
        board_nine.setPreferredSize(new Dimension(35,35));
        board_nine.setToolTipText("New 9x9 board");
        
        easyButton = new JButton(new ImageIcon(getClass().getResource("rabbit_button_big.png")));
        easyButton.setPreferredSize(new Dimension(35,35));
        easyButton.setToolTipText("Easy AI");
        
        mediumButton = new JButton(new ImageIcon(getClass().getResource("medium_button_big.png"))); 
        mediumButton.setPreferredSize(new Dimension(35,35));
        mediumButton.setToolTipText("Medium AI");
        
        difficultButton = new JButton(new ImageIcon(getClass().getResource("difficult_button_big.png")));
        difficultButton.setPreferredSize(new Dimension(45,45));
        difficultButton.setToolTipText("Difficult AI");
        
        board_color = new JButton(new ImageIcon(getClass().getResource("color_button_big.png")));
        board_color.setPreferredSize(new Dimension(45,45));
        board_color.setToolTipText("Change Color");
        
        //Buttons are added to the tool bar.
        bar.add(start);
        bar.add(board_fifteen);
        bar.add(board_twelve);
        bar.add(board_nine);
        bar.add(easyButton);
        bar.add(mediumButton);
        bar.add(difficultButton);
        bar.add(board_color);

        //Action listeners for the elements heard in GUI class are initialized here.
        muted.addActionListener(this);
        
        //The tool bar is set to be located in the west of the panel and the boardpanel in the center.
        getContentPane().add(menuBar, BorderLayout.NORTH);
        getContentPane().add(bar, BorderLayout.WEST);
        
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
    }
    
    /**
     *  Initializes the actions if the action listener of an item of the menu is triggered.
     *  @param ActionEvent e (occurs when a button is graphically pressed).
     */
    public void actionPerformed(ActionEvent e)
    {
        Object obj = e.getSource();
        if(obj == muted)
           mute = !mute;
        buttonSound();   
    }
    
    
    /** 
     * Implements the logic to repaint all the containers in the game
     */
    public void repaint()
    {
        boardPanel.drawBoard();
        getContentPane().repaint();
    }
    
    /**
     *  Plays the sound effect appropiate for the state of the board.
     *  @param int state (the board state that exists at the moment of calling this method).
     */
    public void playEffect(int state)
    {
        switch(state)
        {
            case 0:
            diskAddedsound();
            break;
            
            case 1: case 2:
            errorSound();
            break;
            
            case 3: case 4:
            playWinSound();
            break;
            
            case 5:
            buttonSound();
            break;
            
            case 6:
            playcolorMod();
            break;
        }
    }
    
    /**
     * Initializes the sound that indicates a player has won.
     */
    private void playWinSound()
    {
        InputStream pathSoundFile = getClass().getResourceAsStream("bellringing.wav");
        playSound(pathSoundFile);
    }
    
    /**
     * Initializes the sound that indicates a button has been pressed.
     */
    private void buttonSound()
    {
         InputStream pathSoundFile = getClass().getResourceAsStream("Button.wav");
         playSound(pathSoundFile);
    }
    
    /**
     * Initializes the sound that indicates a disk has been set in the table.
     */
    private void diskAddedsound()
    {
         InputStream pathSoundFile = getClass().getResourceAsStream("diskplacement.wav");
         playSound(pathSoundFile);    
    }
    
    /**
     * Initializes the sound that indicates an error was made.
     */
    private void errorSound()
    {
         InputStream pathSoundFile = getClass().getResourceAsStream("Error.wav");
         playSound(pathSoundFile);
    }
    
    /** 
     * Initializes the sound that indicates a sound change was successful.
     */
    protected void playcolorMod()
    {
        InputStream pathSoundFile = getClass().getResourceAsStream("colorChange.wav");
        playSound(pathSoundFile);
    }
    
    /**
     * Implements/plays the desired sound.
     * @param InputStream access (path to access the file that should be played).
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
    
    /**
     *  Sets the status panel to what the desires status message is.
     *  @param String input (represents the message that is to be displayed).
     */
    public void setMessage (String input) 
    { 
        message.setFont(new Font(message.getName(), Font.BOLD, 24));
        message.setText(input);
    }
    
    /**
     *  Sets the board that will be used as a model throught the view components of the MVC architecture,
     *  displays the size of the board in the status panel,
     *  @param Board newBoard (represents the new board that selected by the user).
     */
    public void setBoard(Board newBoard)
    {   
        board = newBoard; 
        boardPanel.setBoard(board);
        message.setText(board.size()+"x"+board.size());
    }
    
    /** 
     *  This method initializes the common ActionListener on all elements(buttons/JMenuItems) of the GUI.
     *  @param ActionListener e the action listener to be impleted on each option of the Menu and Toolbar.
     */
    public void addListener(ActionListener e) // adds the actionListener indicated from class Main(controller) to all "J" Items
    {
        fifteen.addActionListener(e);
        twelve.addActionListener(e);
        nine.addActionListener(e);
        play.addActionListener(e);
        start.addActionListener(e);
        single.addActionListener(e);
        multi.addActionListener(e);
        aiEasy.addActionListener(e);
        aiMedium.addActionListener(e);
        changeName.addActionListener(e);
        board_fifteen.addActionListener(e);
        board_twelve.addActionListener(e);
        board_nine.addActionListener(e);
        mediumButton.addActionListener(e);
        easyButton.addActionListener(e);
        difficultButton.addActionListener(e);
        color.addActionListener(e);
        board_color.addActionListener(e);
    }
    
    /** 
      *  Sets the listener of the board and allows felixibilty in execution.
      *  @param MouseListener e (instance that will listen the mouse in the board).
      */
    public void setBoardListener(MouseListener e)
    {
        boardPanel.addMouseListener(e);
    }
}
