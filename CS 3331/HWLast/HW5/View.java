package HW5;
import HW4.*;
import java.awt.*;
import java.awt.Dimension;
import java.awt.event.*;
import javax.sound.sampled.*;
import java.io.*;
import javax.swing.*;
import javax.swing.text.DefaultCaret;
import java.net.*;
/**
 * View(GUI) structure of the ConnectFive Game.
 *
 * @author Oscar Galindo, Mario Delgado
 */
public class View extends HW4.GUI 
{
    /** Items added to the network GUI and the main GUI. */
    private JMenuItem multiplayerConnection, disconnect_option;
    
    /** Button that adds the Multiplayer wi-fi option as gamemode. */
    private JButton wifi, consoleButton;
    
    /** Instance of the game chat. */
    private NetworkDialog networkGui;
    
    /** Area where the messages written and displayed are shown. */
    private JTextArea msgDisplay;
    
    /** Final dimension for the network GUI. */
    private final Dimension DIMENSION = new Dimension(575, 400);
    
    /** Buttons of network roles for the network GUI. */
    private JButton connectButton, hostButton;
    
    /** Button that represents the option of sending messages. */
    private JButton sendButton;
    
    /** Field for writing the desired IP to which a player wishes to connect. */
    private JTextField serverEdit;
    
    /** Field for writing to which port the player wishes to connect. */
    private JTextField portEdit;
    
    /** Field for writing messages. */
    private JTextField msgEdit;
   
    /** Panel to which the options of how to connect are added in the network GUI. */
    private JPanel connectPanel;
    
    /**
     *  Initializator of the class View that implements the option for Wi-Fi mode.
     */
    public View(Board board, BoardPanel boardPanel)
    {
        super(board,boardPanel);
        networkGui = new NetworkDialog();
        multiplayerConnection = new JMenuItem("Multiplayer Wi-Fi");
        wifi = new JButton(new ImageIcon(getClass().getResource("button_wifi_red.png")));
        wifi.setPreferredSize(new Dimension(35,35));
        wifi.setToolTipText("WiFi connection is off.");
        consoleButton = new JButton(new ImageIcon(getClass().getResource("console_button.png")));
        consoleButton.setPreferredSize(new Dimension(35,35));
        consoleButton.setToolTipText("Show chat console");
        disconnect_option = new JMenuItem("Disconnect");
        bar.add(wifi);
        bar.add(consoleButton);
        gamemode.add(multiplayerConnection);
        board_color.addActionListener(this);
        color.addActionListener(this);
    }
    
    /** 
      * Method that sets listener of all elements in the main and network GUIs. 
      */
    public void setListener(ActionListener received)
    {
        super.addListener(received);
        multiplayerConnection.addActionListener(received);
        wifi.addActionListener(received);
        connectButton.addActionListener(received);
        hostButton.addActionListener(received);
        sendButton.addActionListener(received);
        disconnect_option.addActionListener(received);
        consoleButton.addActionListener(received);
    }     
    
    /** 
     *  Sets the listener for the network GUI.
     *  @param WindowListener received (the instance/listener that will listes to the network GUI).
     */
    void setNetworkGUIListener(WindowListener received)
    {
       networkGui.setWindowListener(received); 
    }
    
    /**
     *  Sets the listener for the boardPanel
     *  @param MouseListener received (instance/listener of the boardPanel).
     */
    void setboardListener(MouseListener received)
    {
        super.setBoardListener(received);
    }
    
    /**
     *  Method that changes the apperance of the connection status button.
     *  @param boolean connected (indicates if connected to someone else).
     */
    public void setConnectedStatus(boolean connected)
    {
        if(connected)
        {
            hostDisconnect();
            gamemode.add(disconnect_option);
            wifi.setIcon(new ImageIcon(getClass().getResource("button_wifi_green.png")));
            wifi.setToolTipText("WiFi conection stablished, press to disconnect"); 
        }
        else
        {
            setMultiplayer();
            hostButton.setText("Host Game");
            gamemode.remove(disconnect_option);
            wifi.setIcon(new ImageIcon(getClass().getResource("button_wifi_red.png")));
            wifi.setToolTipText("WiFi connection is off.");
        }
    }
    
    /**
     *  This method sets the menu option of Multiplayer Wi-Fi as Console.
     */
    public void setModeConsole(){multiplayerConnection.setText("Console");}
    
    /**
     *  This method restores the menu option of Multiplayer Wi-Fi to its original state.
     */
    private void setMultiplayer() {multiplayerConnection.setText("Multiplayer Wi-Fi");}
    
    /**
     *  Sets the text of the host button to be disconnect.
     */
    public void hostDisconnect() {hostButton.setText("Disconnect");}
    
    /**
     *  Method that changes the visibility of the network GUI.
     *  @param boolean input (indicates the status of the connection).
     */
    public void networkGUIVisibility(boolean input)
    {
        networkGui.setVisible(input);
    }
    
    /**
     *  Method that writes to the console of the network GUI.
     *  @param String input (represents what is to be added to the console of the network GUI).
     */
    public void writeNetworkConsole(String input)
    {
        msgDisplay.append(input+"\n");
    }
    
    /**
     *  Method that blocks the editable status of the serverEdit & portEdit fields.
     */
    public void blocknetworkEdit()
    {
        serverEdit.setEditable(false);
        serverEdit.setBackground(Color.LIGHT_GRAY);
        portEdit.setEditable(false);
        portEdit.setBackground(Color.LIGHT_GRAY);
    }
    
    /**
     *  Method that unblocks the editable status of the serverEdit & portEdit fields.
     */
    public void liberateNetworkEdit()
    {
        serverEdit.setEditable(true);
        serverEdit.setBackground(Color.WHITE);
        portEdit.setEditable(true);
        portEdit.setBackground(Color.WHITE); 
    }
    
    /** Blocks the button to send messages when activated. */
    public void blockSend() {sendButton.setEnabled(false);}
    
    /** Unblocks the button to send messages when activated. */
    public void unblockSend() {sendButton.setEnabled(true);}
    
    /** 
     *  Reports what the port indicated in the network GUI was to the control.
     *  @return String portEdit.getText() (represents the port).
     */ 
    public String getPort() {return portEdit.getText();}
    
    /**
     *  Reports the IP written in the network GUI and to which the user will like to connect.
     *  @param serverEdit.getText() (represents the IP written in the network GUI).
     */
    public String getipInput() {return serverEdit.getText();}
    
    /**
     *  Reports the message written in the console where messages are written to be sent.
     *  @return String msgEdit.getText() (represents message written).
     */
    public String getWritten() 
    {
        String str = msgEdit.getText();
        msgEdit.setText("");//Erases the console of the message after a message is sent.
        return str;
    }
    
    /**
     *  Clears the console when the game starts or the gamemode is changed back to Multiplayer Wi-Fi.
     */
    public void clearWritten() {msgDisplay.setText("");}
    
    /**
      *  This method plays a sound when a message is received.
      */
    public void messageReceived()
    {
        InputStream pathSoundFile = getClass().getResourceAsStream("messageReceived.wav");
        playSound(pathSoundFile);
    }
    
    /** 
     *  Class that implements the necessary dialog elements to have a chat.
     */
    public class NetworkDialog extends JDialog
    {
        /**
         *  Intializes the network chat.
         */
        public NetworkDialog() {
            super((JFrame) null, "Game Chat");
            configureGui();
            setSize(DIMENSION);
            hostButton.addActionListener(this::hostClicked);
            setLocationRelativeTo(null);
        }
        
        /**
         *  The elements of the network chat get assigned and constructed here.
         */
        private void configureGui()
        {
            connectPanel = new JPanel(new FlowLayout(FlowLayout.LEADING));
            connectButton = new JButton("Connect as Client");
            connectButton.setFocusPainted(false);
            hostButton = new JButton("Host Game");
            hostButton.setFocusPainted(false);
            serverEdit = new JTextField("localhost", 15);
            portEdit = new JTextField("25565", 4);
            connectPanel.add(hostButton);
            connectPanel.add(connectButton);
            connectPanel.add(serverEdit);
            connectPanel.add(portEdit);
            
            msgDisplay = new JTextArea(10, 30);
            msgDisplay.setEditable(false);
            DefaultCaret caret = (DefaultCaret)msgDisplay.getCaret();
            caret.setUpdatePolicy(DefaultCaret.ALWAYS_UPDATE); // autoscroll
            JScrollPane msgScrollPane = new JScrollPane(msgDisplay);
    
            JPanel sendPanel = new JPanel(new FlowLayout(FlowLayout.LEADING));
            msgEdit = new JTextField("Hello!", 38);
            sendButton = new JButton("Send");
            sendButton.setMnemonic('s');
            sendButton.setFocusPainted(false);
            sendPanel.add(sendButton);
            sendPanel.add(msgEdit);
            
            setLayout(new BorderLayout());
            add(connectPanel, BorderLayout.NORTH);
            add(msgScrollPane, BorderLayout.CENTER);
            add(sendPanel, BorderLayout.SOUTH);
        }
        
        /** 
         *  Method that implements a listener for the host button.
         *  Call getIP to print the IP addresses (local/network) to the network console when activated.
         *  @param ActionEvent event (Event generated when host is clicked).
         */
        private void hostClicked(ActionEvent event)
        {
            getIP();
        }
         
        /**
         *  This method reports the IP of the network setup found in the system.
         */
        private void getIP() 
        {
            String systemipaddress = "";
            try
            {
                InetAddress localhost = InetAddress.getLocalHost();
                msgDisplay.append("With-in Network System Address: " + (localhost.getHostAddress()).trim()+"\n");
                URL url_name = new URL("http://bot.whatismyipaddress.com");
                BufferedReader sc =
                new BufferedReader(new InputStreamReader(url_name.openStream()));
                // reads system IPAddress
                systemipaddress = sc.readLine().trim();
            }
            catch (Exception e)
            {
                systemipaddress = "Not possible to reach the web.";
            }
            writeNetworkConsole("Network Public IP Address: " + systemipaddress);
        }
        
        /**
         *  This method sets the WindowListener to the main GUI structure so it reports when the screen is closed.
         *  @param WindowListener e (the instance/listener that will listen for changes from the main GUI).
         */
        void setWindowListener(WindowListener e)
        {
            this.addWindowListener(e);
        }
    }
}
