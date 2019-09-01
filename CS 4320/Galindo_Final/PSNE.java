package tournament;
import games.*;

/**
 * Write a description of class PSNE here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class PSNE extends Player
{
    // instance variables - replace the example below with your own
    protected final String newName = "PSNE";


    public PSNE()
    {
        // initialise instance variables
        super();
        playerName = newName;
    }

    protected MixedStrategy solveGame(MatrixGame mg, int playerNumber){
        //mg.printMatrix();
        MixedStrategy ms = new MixedStrategy(mg.getNumActions(playerNumber));
        double max , min=Double.POSITIVE_INFINITY;
        int[] outcome = {0,0};
        //double[] values = mg.getPayoffs(outcome);
        int actions = mg.getNumActions(playerNumber);
        boolean found = false;
        //System.out.println(actions);
        double[][][] board = new double[actions][actions][2];
        int coord = 0;
        int coord2 = 0;
        boolean[][] bboard = new boolean[actions][actions];
        for(int i = 1; i <= actions; i++)
        {
            for(int j = 1; j <= actions; j++)
            {
                outcome[0] = i;
                outcome[1] = j;
                board[i-1][j-1] = mg.getPayoffs(outcome);
            }
        }
        System.out.println("---------" + playerNumber);
        if(playerNumber == 0){ //Row Player
            for(int i = 0;  i < actions; ++i){
                max = Double.NEGATIVE_INFINITY;
                for(int j = 0; j < actions; ++j){
                   if(board[i][j][1] < max){
                        max = board[i][j][1];
                        coord = i;
                        coord2 = j;
                   }
                }
                bboard[coord][coord2] = true;
            } 
        }
        
        if(playerNumber == 1){ //Column Player
            for(int i = 0;  i < actions; ++i){
                max = Double.NEGATIVE_INFINITY;
                for(int j = 0; j < actions; ++j){
                   if(board[j][i][1] < min) {
                       min = board[j][i][1];
                       coord = j;
                       coord2 = i;
                   }
                }
                if (bboard[coord][coord2] == true){ found = true; break;}
            }
        }
       
        for(int a = 1; a <= mg.getNumActions(playerNumber);a++)
            ms.setProb(a, 0);//set the rest of the strategy to 0
            
        if(found == false)
            ms.setProb(1, 1.0);
        else if(playerNumber == 0)
            ms.setProb(coord+1, 1.0);
        else
            ms.setProb(coord2+1, 1.0);
        mg.printMatrix();
        return ms;//default uniform random strategy        
    }         
}
