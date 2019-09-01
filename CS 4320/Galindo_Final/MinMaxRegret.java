package tournament;
import games.*;

/**
 * Write a description of class MinMaxRegret here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class MinMaxRegret extends Player
{
    // instance variables - replace the example below with your own    
    protected final String newName = "MinMax";

    /**
     * Constructor for objects of class MinMaxRegret
     */
    public MinMaxRegret()
    {
        // initialise instance variables
        super();
        playerName = newName;
    }

   protected MixedStrategy solveGame(MatrixGame mg, int playerNumber){
        //mg.printMatrix();
        MixedStrategy ms = new MixedStrategy(mg.getNumActions(playerNumber));
        double max;
        int[] outcome = {0,0};
        //double[] values = mg.getPayoffs(outcome);
        int actions = mg.getNumActions(playerNumber);
        //System.out.println(actions);
        double[][][] board = new double[actions][actions][2];
        int realCoord = 0;
        for(int i = 1; i <= actions; i++)
        {
            for(int j = 1; j <= actions; j++)
            {
                outcome[0] = i;
                outcome[1] = j;
                board[i-1][j-1] = mg.getPayoffs(outcome);
            }
        }
        //System.out.println("---------" + playerNumber);
        double maximum[] = new double[actions];
        if(playerNumber == 0){ //Row Player
            for(int i = 0;  i < actions; ++i){
                max = Double.NEGATIVE_INFINITY;
                for(int j = 0; j < actions; ++j){
                   if(board[i][j][1] > max){
                        max = board[i][j][1];
                        maximum[i] = board[i][j][1];
                   }
                }
            } 
        }
        
        if(playerNumber == 1){ //Column Player
            for(int j = 0;  j < actions; ++j){
                max = Double.NEGATIVE_INFINITY;
                for(int i = 0; i < actions; ++i){
                   if(board[i][j][0] > max) {
                       max = board[i][j][0];
                       maximum[i] = board[i][j][0];
                   }
                }
            }
        }
        
        double selection = Double.POSITIVE_INFINITY;
        for(int i = 0; i < maximum.length; i++){
            if(maximum[i] < selection){
                selection = maximum[i];
                realCoord = i+1;
            }
        }
        
        ms.setZeros();
        for(int a = 1; a <= mg.getNumActions(playerNumber);a++) {
            if (a == realCoord) {
               ms.setProb(a, 1.0);
               //System.out.println("How do probabilities look: "+ms.toString());
            }
            else ms.setProb(a, 0);//set the rest of the strategy to 0
        }
        //mg.printMatrix();
    	return ms;//default uniform random strategy        
    }          
}
