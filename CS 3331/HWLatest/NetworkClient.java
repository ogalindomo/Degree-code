import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.net.*;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.text.DefaultCaret;

/** A simple chat dialog. */
@SuppressWarnings("serial")
public class NetworkClient extends JDialog {
    
    /** Default dimension of chat dialogs. */
    private final static Dimension DIMENSION = new Dimension(400, 400);
    
    private JButton connectButton;
    private JButton sendButton;
    private JTextField serverEdit;
    private JTextField portEdit;
    private JTextArea msgDisplay;
    private JTextField msgEdit;
    private PrintWriter out;
    private BufferedReader in;
    private String host;
    private int hostport;
    private Socket s;
    private boolean connected;
    
    /** Create a main dialog. */
    public NetworkClient() {
        this(DIMENSION);
    }
    
    /** Create a main dialog of the given dimension. */
    public NetworkClient(Dimension dim) {
        super((JFrame) null, "JavaChat");
        configureGui();
        setSize(dim);
        //setResizable(false);
        connectButton.addActionListener(this::connectClicked);
        sendButton.addActionListener(this::sendClicked);
        setLocationRelativeTo(null);
    }
    
    /** Configure UI of this dialog. */
    private void configureGui() {
        JPanel connectPanel = new JPanel(new FlowLayout(FlowLayout.LEADING));
        connectButton = new JButton("Connect");
        connectButton.setFocusPainted(false);
        serverEdit = new JTextField("localhost", 18);
        portEdit = new JTextField("8000", 4);
        connectPanel.add(connectButton);
        connectPanel.add(serverEdit);
        connectPanel.add(portEdit);
        
        msgDisplay = new JTextArea(10, 30);
        msgDisplay.setEditable(false);
        DefaultCaret caret = (DefaultCaret)msgDisplay.getCaret();
        caret.setUpdatePolicy(DefaultCaret.ALWAYS_UPDATE); // autoscroll
        JScrollPane msgScrollPane = new JScrollPane(msgDisplay);

        JPanel sendPanel = new JPanel(new FlowLayout(FlowLayout.LEADING));
        msgEdit = new JTextField("Enter a message.", 27);
        sendButton = new JButton("Send");
        sendButton.setFocusPainted(false);
        sendPanel.add(msgEdit);
        sendPanel.add(sendButton);
        
        setLayout(new BorderLayout());
        add(connectPanel, BorderLayout.NORTH);
        add(msgScrollPane, BorderLayout.CENTER);
        add(sendPanel, BorderLayout.SOUTH);
    }
    
    /** Callback to be called when the connect button is clicked. */
    private void connectClicked(ActionEvent event) {
        try
        {
            if(!connected)
            {
              host = serverEdit.getText();
              connected = true;
              connectButton.setText("Disconnect");
              hostport = Integer.parseInt(portEdit.getText());
              s = new Socket(host,hostport);
              out = new PrintWriter(new OutputStreamWriter(s.getOutputStream()));
              in = new BufferedReader(new InputStreamReader(s.getInputStream()));
              new Thread(() -> 
              {
                  try{
                      String str = null;
                      while((str = in.readLine()) != null)
                          msgDisplay.append("\n"+str);}
                  catch(IOException e ){}
              }).start();
              //s.close();
           }
           else if(connected)
           {
                s.close();
                connectButton.setText("Connect");
                msgDisplay.append("\n"+"You disconnected");
                connected = false;
           }
        }
        catch(IOException e)
        {
           
            
        }
    }
    
    
    /** Callback to be called when the send button is clicked. */
    private void sendClicked(ActionEvent event) 
    {
        try
        {
            if(!connected)
            {
                msgDisplay.append("\n Please connect to a server before sending something.");
            }
            String message = msgEdit.getText();
            out.println(message);
            out.flush();
            if(message.equals("BYE"))
             {
                 s.close();
                 connectButton.setText("Connect");
                 msgDisplay.append("\n"+"You disconnected");
                 connected = false;
             }
        }
        catch(IOException e)
        {}
    }

    /** Show the given message in a dialog. */
    private void warn(String msg) {
        JOptionPane.showMessageDialog(this, msg, "JavaChat", 
                JOptionPane.PLAIN_MESSAGE);        
    }
    
    public static void main(String[] args) {
        NetworkClient dialog = new NetworkClient();
        dialog.setVisible(true);
        dialog.setDefaultCloseOperation(DISPOSE_ON_CLOSE);
    }
    
}