package HW5;
import HW4.*;
import java.awt.event.*;
import javax.swing.*;
import java.net.*;
import java.io.*;
import java.awt.*;
import javax.swing.*;
import javax.swing.text.DefaultCaret;
import javax.swing.JFrame;
/**
 * Control structure of the ConnectFive Game.
 *
 * @author Oscar Galindo, Mario Delgado
 */
public class Control extends HW4.Main 
{
    //Instances for the internet functionality.
    /** Listener of the console(view) */
    private Observer ear2;
    
    /** Booleans used for determining the state of connection */
    private boolean network, joined, hosting, connected;
    
    /** Integer to store the size of the game proposed to another player. */
    private int proposedSize;
    
    /** Extended class instance of the GUI */
    private View console;
    
    /** Instance of the communication port of the game. */
    private NetworkAdapter communication;
    
    /** Observer of the status of the screen. */
    private WindowObserver eye;
    
    /** Instance of the server. */
    private ServerSocket serv;
    
    /** Instances of the sockets used respectively in execution. */
    private  Socket client, server;
    
    /** Strings used to store the names of the players. */
    private  String myName, otherPlayerName;
    
    public static void main(String[]args)
    {
        new Control(true);
    }
    
    private Control(boolean visibility)
    {
        super();
        board = new Board(15);//Instantiates the board
        boardPanel = new BoardPanel(board);
        console = new View(board,boardPanel);
        screen = (GUI) console;
        secondPlayer = new EasyAI(board);
        player1Name = "Player 1";
        player2Name = "Player 2";
        gamemode = "";
        myName = "";
        proposedSize = 0;
        gamemode = "";
        ear2 = new Observer();
        eye = new WindowObserver();
        console.addWindowListener(eye);
        screen.addWindowListener(eye);
        console.setListener(ear2);
        console.setboardListener(ear2);
        console.setVisible(visibility);
        console.pack();  
    }
    
    /**
     *  Observer class for the graphical user interface of connect five.
     *  Listener for connecting decision-making methods to action-making methods.
     */
    private class Observer extends HW4.Main.Listener implements NetworkAdapter.MessageListener
    {
        /** 
         *  Method that implements the actions according to the button pressed in the GUI.
         *  @param ActionEvent e (An event that originates from the GUI.)
         *  @Override the actionPerformed method from HW4.Main.Listener
         *  @see HW4.Main.Listener
         */
        @Override
        public void actionPerformed(ActionEvent e)
        {
            AbstractButton prov = (AbstractButton) e.getSource();//What triggered the events is converted into an abstract button
            String input = prov.getText();//From the type AbstractButton the string the represents the text of the button is extracted
            String source_blue = getClass().getResource("blue_button_big.png").toString();//Reference to the graphical face(image) of all possible button.
            String source_yellow = getClass().getResource("yellow_button_big.png").toString();
            String source_oscar = getClass().getResource("oscar_button_big.png").toString();
            String source_console = getClass().getResource("console_button.png").toString();
            String source = null;
            if(prov.getIcon() != null)
            {
                source = prov.getIcon().toString();
            }
            if(input.equals("Multiplayer Wi-Fi") || input.equals("Console"))
            {
               if(!network)
                {
                    if(playing)
                    {
                        console.playEffect(5);
                        int answer = JOptionPane.showConfirmDialog(null, "Will you like to change game mode?");//Asks the user if he/she wishes to change gamemode.
                        if(answer != 0) {return;}
                        playing = false;
                        board = new Board(board.size());
                        console.setBoard(board);
                        console.repaint();
                    }
                    console.playEffect(5);
                    boardPanel.setPlayer1Color(237,90,76);
                    boardPanel.setPlayer1ColorName("Red");
                    boardPanel.setPlayer2Color(0,0,255);
                    boardPanel.setPlayer2ColorName("Blue");
                    console.repaint();
                    console.clearWritten();
                    console.writeNetworkConsole("Welcome "+myName+" to the internet version of this game.");
                    console.writeNetworkConsole("To change your name please go to settings.");
                    console.writeNetworkConsole("For hosting the game just indicate the port you wish to open.");
                    console.writeNetworkConsole("To connect as a client indicate the IP you wish to connect.");
                    console.blockSend();
                    console.networkGUIVisibility(true);
                    artificialActive = false;
                }
                else
                {
                    console.playEffect(5);
                    console.networkGUIVisibility(true);
                }
            }
            else if(input.equals("Host Game"))
            {
                 console.playEffect(5);
                 if(!network)
                 {
                     network = true;
                     if(myName.equals(""))
                     {
                         console.setMessage("Please enter your name");
                         String name = (String)JOptionPane.showInputDialog(null, "Please write your name or else your name will be Steve.\nTo change your name again please go to settings.",
                                                                    "Set Name",JOptionPane.QUESTION_MESSAGE);
                          if(name == null || name.equals("")||name.equals("null"))
                            myName = "Steve";
                          else 
                            myName = name;
                     }
                     console.setMessage("Waiting for other connections");
                     int port = Integer.parseInt(console.getPort());
                     console.blocknetworkEdit();
                     console.hostDisconnect(); //Sets the button of Host Game to read Disconnect
                     console.setModeConsole(); //Sets the multiplayer wifi as a console option to show the console
                     new Thread(() -> 
                     { 
                         try {
                               serv = new ServerSocket(port);
                               hosting = true;
                               server = serv.accept();
                               connectionProtocol(server);
                         } catch(Exception err) {
                               console.setMessage("Port already in use.");
                               console.liberateNetworkEdit();
                               console.setConnectedStatus(false);
                               try{serv.close(); server.close();} catch(Exception error) {}
                               hosting = false;
                               network = false;
                         }
                     }).start();
                 }
            }
            else if(input.equals("Connect as Client"))
            {
                 console.playEffect(5);
                 if(!network)
                 {
                     network = true;
                     if(myName.equals(""))
                     {
                          console.setMessage("Please enter your name");
                          String name = (String)JOptionPane.showInputDialog(null, "Please write your name or else your name will be Steve.\nTo change your name again please go to settings.",
                                                                    "Set Name", JOptionPane.QUESTION_MESSAGE);
                          if(name == null || name.equals("")||name.equals("null"))
                            myName = "Steve";
                          else 
                            myName = name;
                     }
                     int port = Integer.parseInt(console.getPort());
                     String ip = console.getipInput();
                     console.blocknetworkEdit();
                     new Thread(() -> 
                     { 
                         try {
                             client = new Socket(ip,port);
                             joined = true;
                             connectionProtocol(client);
                             communication.writeName(myName);
                             communication.writeJoin();
                             console.writeNetworkConsole("");
                         } catch(Exception err) {
                             console.setMessage("Please check the ip and port provided.");
                             console.liberateNetworkEdit();
                             network = false;
                             joined = false;
                         }
                     }).start();
                 }
            }
            else if(input.equals("Disconnect"))
            {
                console.playEffect(5);
                if(connected)
                    console.setMessage("You disconnected.");
                else
                    console.setMessage("You stopped hosting.");
                disconnectionProtocol();
                console.networkGUIVisibility(false);
            }
            else if(input.equals("Send"))
            {
                console.playEffect(5);
                if(network)
                {
                    String str = console.getWritten();
                    console.writeNetworkConsole("You: "+str);
                    communication.writeMessage(str);
                }
            }
            else if ((input.equals("Multiplayer") || input.equals("Singleplayer")) && network)
            {
                 int answer = JOptionPane.showConfirmDialog(null, "Will you like to abandon network mode?");
                 if(answer == 0)
                 {
                     disconnectionProtocol();
                     console.setMessage("You disconnected.");
                     super.actionPerformed(e);
                 }
            }
            else if(network && (input.equals("15x15") || source_blue.equals(source)))
            {
                newGame(15);
                console.playEffect(5);
            }
            else if(network && (input.equals("12x12") || source_yellow.equals(source)))
            {
                console.playEffect(5);
                newGame(12);
            }
            else if(network && (input.equals("9x9") || source_oscar.equals(source)))
            {
                console.playEffect(5);
                newGame(9);
            }
            else if(input.equals("Change Name"))
            {
                if(network && connected)
                {
                    console.playEffect(5);
                    String name = JOptionPane.showInputDialog("Please input your nametag.");
                    if(name.equals(""))
                        myName = "Steve";
                    else 
                        myName = name;
                    communication.writeName(myName);
                    setNames(otherPlayerName);
                }
                else 
                    super.actionPerformed(e);
            }
            else if(input.equals("Change Color") && network)
            {
                if(playing)
                    colorChange();
                else if(!playing)
                    console.setMessage("Start a game to change color.");
            }
            else if(source_console.equals(source))
            {
                console.playEffect(5);
                if(network)
                    console.networkGUIVisibility(true);
                else
                    console.setMessage("To use this feature please start a Wi-Fi game.");
            }
            else 
                super.actionPerformed(e);
        }
        
        /** 
          * Method that implements a generic connection protocol. 
          */
        private void connectionProtocol(Socket s)
        {
            communication = new NetworkAdapter(s);
            communication.setMessageListener(this);
            communication.receiveMessagesAsync();
        }
        
        /**
         *  Method that implements the code for communicating the desire to start a new game.
         *  @param int size (desired size of the board of the new game).
         */
        private void newGame(int size)
        {
            if(network)
            {
                String [] options = {"Yes","No"};
                int answer = JOptionPane.showOptionDialog(null, "Will you like to propose a new "+size+"x"+size+" game?", "Propose Game",  
                                                          JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, options, options[0]);
                if(answer == 0)
                {
                    proposedSize = size;
                    communication.writeNew(size);
                }
            }
        }
        
        /**
         *  Method that implements the measures necessary when the player presses the board panel.
         *  @Override the mousePressed from HW4.Main.Listener.
         *  @see HW4.Main.Listener.
         *  @param MouseEvent e (event that originates when a click is made in the graphical area of the board).
         */
        @Override
        public void mousePressed(MouseEvent e)
        {
            if(network)
            {
               if(playing && hosting && board.getNumberOfDisks() % 2 == 0)
               {
                   board.addDisk(convert(e.getX()), convert(e.getY()));
                   console.repaint();
                   play();
                   if(board.getStatus() == 0 || board.getStatus() == 3 || board.getStatus() == 4)
                   {
                       communication.writeFill(convert(e.getX()), convert(e.getY()), 0);
                       play();
                   }
               }
               else if(playing && joined && board.getNumberOfDisks() % 2 == 1)
               {
                   board.addDisk(convert(e.getX()), convert(e.getY()));
                   console.repaint();
                   play();
                   if(board.getStatus() == 0 || board.getStatus() == 3 || board.getStatus() == 4)
                   {
                       communication.writeFill(convert(e.getX()), convert(e.getY()), 0);
                       play();
                   }
               }
               else if(!playing && (joined || hosting))
                  console.setMessage("Press a circle in the toolbar to star a game.");                
               else
               {
                   console.setMessage("Please wait for your turn");
                   console.playEffect(1);
               }
            }
            else {super.mousePressed(e);}
        }
        
        /** 
         *  Implements the necessary interface to listen to the messages from NetworkAdapter class.
         *  @see NetworkAdapter
         *  @param NetworkAdapter.MessageType type (type of message received from NetworAdapter).
         *  @param int x, y, z (meaning different things depending on the MessageType).
         *  @param int[] others (meaning different things depending on the MessageType).
         *  @param String message (message written by the other player and received in string form).
         */
        public void messageReceived(NetworkAdapter.MessageType type, int x, int y, int z, int[] others, String message)
        {
            if(type == NetworkAdapter.MessageType.MESSAGE)
            {
                 console.writeNetworkConsole(otherPlayerName+": "+message);
                 console.setMessage("Message Received from "+otherPlayerName);
                 console.messageReceived();
            }
            else if(type == NetworkAdapter.MessageType.JOIN)
            {
                console.setMessage("Join request received from "+otherPlayerName);
                String [] options = {"Yes, accept connection","No, refuse connection"};
                int answer = JOptionPane.showOptionDialog(null, "Will you like to accept the incoming connection from "+player2Name+" ?", "Incoming Connection",
                                                          JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, options, options[0]);
                if(answer == 0)
                {
                    connected = true;
                    console.unblockSend();
                    console.setConnectedStatus(true);
                    communication.writeName(myName);
                    communication.writeJoinAck(board.size());
                    console.setMessage("Connected to "+otherPlayerName);
                }
                else 
                {
                    console.setMessage("Join request from "+otherPlayerName+" denied.");
                    console.liberateNetworkEdit();
                    communication.writeName(myName);
                    communication.writeJoinAck();
                    disconnectionProtocol();
                }
            }
            else if (type == NetworkAdapter.MessageType.JOIN_ACK)
            {
                if(x == 1)
                {
                    connected = true;
                    console.setMessage(otherPlayerName+" accepted the connection.");
                    console.setConnectedStatus(true);
                    console.repaint();
                    console.unblockSend();
                }
                else 
                {
                    connected = false;
                    console.setMessage(otherPlayerName+" refused the connection.");
                    disconnectionProtocol();
                }
            }
            else if(type == NetworkAdapter.MessageType.FILL)
            {
                board.addDisk(x,y);
                console.repaint();
                play();
            }
            else if(type == NetworkAdapter.MessageType.NEW)
            {
                String [] options = {"Yes, accept new game","No, refuse new game"};
                int answer = JOptionPane.showOptionDialog(null, "Will you like to start a new game of size "+x+" ?", "Incoming Connection",
                                                          JOptionPane.DEFAULT_OPTION, JOptionPane.PLAIN_MESSAGE, null, options, options[0]);
                if(answer == 0)
                {
                    playing = false;//The change between playing false and then true occurs because if the board size is change when playing
                    gameButton(x);// the game prompts for a conformation.
                    playing = true;
                    communication.writeNewAck(true);
                }
                else
                    communication.writeNewAck(false);
            }
            else if(type == NetworkAdapter.MessageType.NEW_ACK)
            {
                if(x == 1)
                {
                    playing = false;
                    gameButton(proposedSize);
                    playing = true;
                }
                else
                    console.setMessage("New game proposal refused by "+otherPlayerName+" player.");
            }
            else if(type == NetworkAdapter.MessageType.QUIT)
            {
                console.setMessage(otherPlayerName + " disconnected.");
                disconnectionProtocol();
            }
            else if(type == NetworkAdapter.MessageType.NAME)
            {
                if(hosting)
                    setNames(message);
                else if (joined)
                    setNames(message);
            }
            else if(type == NetworkAdapter.MessageType.COLOR)
            {
                setColor(message);
            }
        }
    }
    
    /**
     *  WindowObserver class that observes windows' status.
     */
    private class WindowObserver extends WindowAdapter
    {   
        public void windowClosing(WindowEvent e) 
        {
            if(connected)
                console.setMessage("You disconnected.");
            disconnectionProtocol();
        }
        
        public void windowClosed(WindowEvent e)
        {
            if(connected)
                console.setMessage("You disconnected.");
            disconnectionProtocol();
        }
    }
    
    /**
     *  Implements the color change algorithm for everyplayer.
     */
    protected void colorChange()
    {
        String [] colors = {"Green","Blue","Yellow","Red","Black","Gray","Orange","Purple","Oscar","Rebeca"};
        String[] possibilities = {"hey","no"};//Simple initialization
        String colorPlayer1 = BoardPanel.getPlayer1ColorName();
        String colorPlayer2 = BoardPanel.getPlayer2ColorName();
        if(playing)
        {
            String inputColor = "";
            int r = 0, g = 0, b = 0;
            if(myName.equalsIgnoreCase("Oscar") || myName.equals("oscargalindom") || myName.equalsIgnoreCase("Rebeca") || myName.equals("rebecamolinar"))
               possibilities = new String[8];
            else
               possibilities = new String[6];
            for(int i = 0, j= 0; i < possibilities.length && j < colors.length; j++)
            {
                if(!(colorPlayer1.equals(colors[j])) && !(colorPlayer2.equals(colors[j])))//Adds the options to be displayed if they are not used.
                {
                     if(colors[i].equals("Oscar") && myName.equalsIgnoreCase("Oscar"))
                     {
                         possibilities[i] = colors[j];
                         i += 1;
                     }
                     else if(colors[i].equals("Rebeca") && myName.equalsIgnoreCase("Rebeca"))
                     {
                         possibilities[i] = colors[j];
                         i += 1;
                     }
                     else 
                     {
                         possibilities[i] = colors[j];
                         i += 1;
                     }
                }
            }
            inputColor = (String) JOptionPane.showInputDialog(null, "Color","Player 1 please choose a color.", JOptionPane.QUESTION_MESSAGE, null, possibilities,colorPlayer1); // Gets the color choosen by the user.
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
                    
                    case"Rebeca":
                    r = 106;
                    g = 51;
                    b = 57;
                    break;
                }
                Color provisional = new Color(r,g,b);
                if(hosting)
                {
                    boardPanel.setPlayer1Color(r,g,b);
                    boardPanel.setPlayer1ColorName(inputColor);
                    communication.writeColor(inputColor);
                }
                else if(joined)
                { 
                    boardPanel.setPlayer2Color(r,g,b);
                    boardPanel.setPlayer2ColorName(inputColor);
                    communication.writeColor(inputColor);
                }
                console.playEffect(6);      
             }
        }
        console.repaint();
    }
    
    /**
     *  Method that sets the colors of the player that is non-local to this system.
     *  @param String colorReceived (String name of the color choose by the other player).
     */
    private void setColor(String colorReceived)
    {
        int r = 0, g = 0, b = 0;
        switch(colorReceived)
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
            
            case"Rebeca":
            r = 106;
            g = 51;
            b = 57;
            break;
        }    
        if(hosting)
        {
            boardPanel.setPlayer2Color(r,g,b);
            boardPanel.setPlayer2ColorName(colorReceived);
        }
        else if(joined)
        {
            boardPanel.setPlayer1Color(r,g,b);
            boardPanel.setPlayer1ColorName(colorReceived);
        }
        console.repaint();
    }
    
    /**
     *  Method that sets the appropiate order of names depending on your joined or host status.
     *  @param String answer (name received as that of other player).
     */
    private void setNames(String answer)
    {
        if(myName.equals("Oscar") || myName.equals("oscargalindom"))
            secretColor = true;
        if(hosting)
        {
            player1Name = myName;
            player2Name = answer;
            otherPlayerName = answer;
        }
        else if(joined)
        {
            player1Name = answer;
            player2Name = myName;
            otherPlayerName = answer;
        }
    }
    
    /**
     *  Generic disconnection protocol for the TCP connection.
     */
    private void disconnectionProtocol()
    {
        console.setConnectedStatus(false); 
        if(connected)//If the player is connected to someone else a quit message is written.
        {
            communication.writeQuit(); 
            communication.close(); 
        } 
        if(joined)
        {
            try{client.close();} 
            catch (Exception error) {}
            joined = false;
        }
        else if(hosting)
        {
            try
            { server.close(); serv.close();} 
            catch (Exception error){}
            hosting = false;
        }
        console.liberateNetworkEdit();
        console.blockSend();
        connected = false;
        network = false; 
        playing = false;
    }
}
