import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.util.Calendar;
import javax.swing.Timer;

public class DigitalClock implements TimeDisplay
{
    private Font font = new Font("Monospaced", Font.BOLD, 41);
    private Color color = new Color(254,254,254);
    public void paint(Graphics g, Color f) {
        Calendar calendar = Calendar.getInstance();
        int hours = calendar.get(Calendar.HOUR_OF_DAY);
        int minutes = calendar.get(Calendar.MINUTE);
        int seconds = calendar.get(Calendar.SECOND);
        g.setFont(font);
        g.setColor(f);
        g.drawString(String.format("%d:%02d:%02d", hours%12, minutes, seconds), 10, 60);
    }
}
