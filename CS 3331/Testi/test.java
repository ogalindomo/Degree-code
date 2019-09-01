
public class test extends Thread
{
    private int count, inc, delay;
    public test(int init, int inc, int delay)
    {
        this.count = init; this.inc = inc; this.delay = delay;
    }
    
    public void run()
    {
        try{
                for(;;)
                {
                    System.out.println(count+" ");
                    count+= inc;
                    Thread.sleep(delay);
                    
                }
        
        
            }
        catch(InterruptedException e) {}
        
    }
    
    public static void main(String[]args)
    {
        new test(0,1,33).start();
        new test(0,-1,100).start();
        
    }
}
