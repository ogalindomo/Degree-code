package tournament;
import games.*;

/**
 * Write a description of class MaxMinPayoff here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class MaxMinPayoff extends Player
{
    // instance variables - replace the example below with your own
    protected final String newName = "MaxMin";
    /**
     * Constructor for objects of class MaxMinPayoff
     */
    public MaxMinPayoff()
    {
        super();
        playerName = newName;
    }
    
    protected MixedStrategy solveGame(MatrixGame mg, int playerNumber){
        //mg.printMatrix();
        MixedStrategy ms = new MixedStrategy(mg.getNumActions(playerNumber));
        double min = 0.0;
        int[] outcome = {0,0};
        //double[] values = mg.getPayoffs(outcome);
        int actions = mg.getNumActions(playerNumber);
        //System.out.println(actions);
        double[][][] board = new double[actions][actions][2];
        int coord = 0;
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
        double minimum[] = new double [actions];
        if(playerNumber == 0){ //Row Player
            for(int i = 0;  i < actions; ++i){
                min = Double.POSITIVE_INFINITY;
                for(int j = 0; j < actions; ++j){
                   if(board[i][j][0] < min){
                        min = board[i][j][0];
                        minimum[i] = min;
                   }
                }
            } 
        }
        
        if(playerNumber == 1){ //Column Player
            for(int j = 0;  j < actions; ++j){
                min = Double.POSITIVE_INFINITY;
                for(int i = 0; i < actions; ++i){
                   if(board[i][j][1] < min) {
                       min = board[i][j][1];
                       minimum[j] = min;
                   }
                }
            }
        }
        
        double selection = Double.NEGATIVE_INFINITY;
        for(int i = 0; i < minimum.length; i++){
            if(minimum[i] > selection){
                selection = minimum[i];
                coord = i+1;
            }
        }
        
        ms.setZeros(); //All probabilities are zero. 
        ms.setProb(coord, 1.0);
        //mg.printMatrix();
        return ms;//default uniform random strategy        
    }                   
}
