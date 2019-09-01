package tournament;
import games.*;

/**
 * Write a description of class MaxMinPayoff here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class MaxPayoff extends Player
{
    // instance variables - replace the example below with your own
    protected final String newName = "Max";
    /**
     * Constructor for objects of class MaxMinPayoff
     */
    public MaxPayoff()
    {
        super();
        playerName = newName;
    }

    protected MixedStrategy solveGame(MatrixGame mg, int playerNumber){
        // System.out.println("start of solveGame-------------------------------------------------------------------------");

        MixedStrategy ms = new MixedStrategy(mg.getNumActions(playerNumber));
        double max = Double.NEGATIVE_INFINITY;

        int[] outcome = {0,0};

        int actions = mg.getNumActions(playerNumber);
        double[][][] board = new double[actions][actions][2];

        //create our own board
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

        // if row Player
        if(playerNumber == 0){
            for(int i = 0;  i < actions; ++i){
                for(int j = 0; j < actions; ++j){
                    if (board[i][j][0] > max){ max = board[i][j][0]; realCoord = i+1;}
                }
            }
            outcome[0] = realCoord; outcome[1] = 1;
        }

        // if column Player
        if(playerNumber == 1){
            for(int i = 0;  i < actions; ++i){
                for(int j = 0; j < actions; ++j){
                    if (board[i][j][1] > max){ max = board[i][j][1]; realCoord = j+1;}
                }
            }
            outcome[0] = 1; outcome[1] = realCoord;
        }

        ms.setZeros();
        for(int a = 1; a <= mg.getNumActions(playerNumber);a++) {
            if (a == realCoord) {
               ms.setProb(a, 1.0);
               //System.out.println("How do probabilities look: "+ms.toString());
            }
            else ms.setProb(a, 0);//set the rest of the strategy to 0
        }

        double[] res = mg.getPayoffs(outcome);
        //System.out.println("Max Player " + playerNumber + " picked " + realCoord + "  ---  res 0: " + res[0] + " res 1: " + res[1] + " our max: " + max +" actions: "+mg.getNumActions(playerNumber));
        //mg.printMatrix();
        return ms;//default uniform random strategy
    }
}
