package tournament;
import games.*;
import java.lang.Math;
/**
 * Write a description of class MaxAverage here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class MaxAverage extends Player
{
    protected final String newName = "MaxAverage"; //Overwrite this variable in your player subclass

    /**
     * Constructor for objects of class StdDevPayoff
     */
    public MaxAverage()
    {
        super();
        playerName = newName;
    }

    protected MixedStrategy solveGame(MatrixGame mg, int playerNumber){
        MixedStrategy ms = new MixedStrategy(mg.getNumActions(playerNumber));
        int[] outcome = {0,0};
        int actions = mg.getNumActions(playerNumber);
        double[][][] board = new double[actions][actions][2];
        int max_payoff = 0;
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
        
        //Board is already in the system.
        double summation=0.0;
        int elements = 0, action = 0;
        double[]values_payoff = new double[actions];
        if(playerNumber == 0)
        {
            for(int i = 0; i < board.length; i++)
            {
                summation = 0.0;
                for(int j = 0; j < board[i].length; j++)
                {
                    summation += board[i][j][0];
                }
                //System.out.println("");
                //elements -= 1;
                values_payoff[i] = summation;
                //System.out.println(values_variance[i][0]);
            }
        }
        
        if(playerNumber == 1)
        {
            for(int j = 0; j < board[0].length; j++)
            {
                summation = 0.0;
                for(int i = 0; i < board.length; i++)
                {
                    summation += board[i][j][1];
                }
                //System.out.println("");
                //elements -= 1;
                values_payoff[j] = summation;
                //System.out.println(values_variance[j][0]);
            }
        }

        double max = Double.NEGATIVE_INFINITY;
        for(int i = 0; i < values_payoff.length; i++)
        {
            if(values_payoff[i] > max){
                max = values_payoff[i];
                realCoord = i + 1;
            }
        }
        
        //System.out.println("---------" + playerNumber);
        ms.setZeros();
        for(int a = 1; a <= mg.getNumActions(playerNumber);a++) {
            if (a == realCoord) {
               ms.setProb(a, 1.0);
               //System.out.println("How do probabilities look: "+ms.toString());
            }
            else ms.setProb(a, 0);//set the rest of the strategy to 0
        }
        ms.setProb(realCoord, 1);
        //System.out.println("Coord: "+realCoord+" probabilities: "+ms.toString());
        //mg.printMatrix();
        return ms;//default uniform random strategy        
    }
}
