import java.awt.Graphics;
public interface CelestialObject
{
    public void appear(Graphics g);
    public void setPosition(int x, int y);
    public int getX();
    public int getY();
}
