package tournament;
import games.*;
import java.lang.Math;
/**
 * Write a description of class VariancePayoff here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class VariancePayoff extends Player
{
    protected final String newName = "Variance"; //Overwrite this variable in your player subclass

    /**
     * Constructor for objects of class StdDevPayoff
     */
    public VariancePayoff()
    {
        super();
        playerName = newName;
    }

    protected MixedStrategy solveGame(MatrixGame mg, int playerNumber){
        MixedStrategy ms = new MixedStrategy(mg.getNumActions(playerNumber));
        double min = Double.POSITIVE_INFINITY, average_min = Double.POSITIVE_INFINITY;
        int[] outcome = {0,0};
        int actions = mg.getNumActions(playerNumber);
        double[][][] board = new double[actions][actions][2];
        int realCoord = Integer.MAX_VALUE;
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
        double average = 0.0, summation=0.0, variance = 0.0;
        int elements = 0, action = 0;
        double[][]values_variance = new double[actions][2];
        double [] values_read = new double[actions];
        if(playerNumber == 0)
        {
            for(int i = 0; i < board.length; i++)
            {
                elements = 0;
                summation = 0.0;
                for(int j = 0; j < board[i].length; j++)
                {
                    summation += board[i][j][0];
                    values_read[j] = board[i][j][0];
                    //System.out.print(values_read[j]+" ");
                    elements += 1;
                }
                //System.out.println("");
                average = summation / elements;//Average
                for(int e = 0; e < values_read.length; e++){
                    summation += Math.pow((values_read[e] - average),2);
                }
                    
                //elements -= 1;
                variance = summation / elements;
                values_variance[i][0] = variance;
                values_variance[i][1] = average;
                //System.out.println(values_variance[i][0]);
            }
        }
        
        if(playerNumber == 1)
        {
            for(int j = 0; j < board[0].length; j++)
            {
                elements = 0;
                summation = 0.0;
                for(int i = 0; i < board.length; i++)
                {
                    summation += board[i][j][1];
                    values_read[i] = board[i][j][1];
                    //System.out.print(values_read[i]+" ");
                    elements += 1;
                }
                //System.out.println("");
                average = summation / elements;//Average
                for(int e = 0; e < values_read.length; e++){
                    summation += Math.pow((values_read[e] - average),2);
                }
                //elements -= 1;
                variance = summation / elements;
                values_variance[j][0] = variance;
                values_variance[j][1] = average;
                //System.out.println(values_variance[j][0]);
            }
        }

        for(int index = 0; index < values_variance.length; index++){
            if(values_variance[index][1] < 0){
                realCoord = (realCoord == Integer.MAX_VALUE)? index+1: realCoord;
                continue;
            }
            if(min > values_variance[index][0])
            {
                min = values_variance[index][0];
                average_min = values_variance[index][1];
                realCoord = index+1;
            }
            else if(min == values_variance[index][0]){
                if(average < values_variance[index][1]){
                    min = values_variance[index][0];
                    average_min = values_variance[index][1];
                    realCoord = index+1;
                }
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
