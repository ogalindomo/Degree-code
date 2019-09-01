import java.applet.*;
import java.awt.*;
import java.awt.BorderLayout;
public class ClassRoom extends Applet
{
    public void init()
    {
        setLayout(new BorderLayout());
        Panel window = new Panel(new BorderLayout());
        window.add(new Button("Window Aisle"), BorderLayout.NORTH);
        window.add(new Button("Wall Aisle"), BorderLayout.SOUTH);
        window.add(new Button("Chairs"), BorderLayout.CENTER);
        window.add(new Button("Desk"), BorderLayout.EAST);
        add(window);
        add(new Button("Board"), BorderLayout.LINE_END);
        //windowd.add(new Button("Chairs
    }
}
