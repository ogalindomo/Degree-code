package tournament;
import games.*;
import java.lang.Math;
import java.util.Random;
/**
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class CombinedPayoff extends Player
{
    // instance variables - replace the example below with your own
    protected final String newName = "Combined-Payoff"; //Overwrite this variable in your player subclass
    int game_results[] = {0,0,0};
    int method_used = 0;
    double beta = 1;
    boolean firstGame =  true;
    public CombinedPayoff()
    {
        super();
        playerName = newName;
    }

    protected MixedStrategy solveGame(MatrixGame mg, int playerNumber){
        if(firstGame){
            firstGame = false;
        }
        else{
            if(playerNumber == 1){
                if(lastPayoffs[0] > lastPayoffs[1])
                    game_results[method_used]++;
                else
                    game_results[method_used]--;
            }
            else{
                if(lastPayoffs[1] > lastPayoffs[0])
                    game_results[method_used]++;
                else
                    game_results[method_used]--;
            }
        }
        double summation_exp = 0.0;
        double probability [] = new double[game_results.length];
        for(int i = 0;i < game_results.length; i++)
            summation_exp += (beta * Math.exp(game_results[i]));
        
        for(int i = 0; i < probability.length; i++)
            probability[i] = ((beta * Math.exp(game_results[i]))/summation_exp);
        
        Random r = new Random();
        double random_choice = r.nextDouble();
        int choice = 0;
        for(int i = 1; i < probability.length; i++)
            probability[i] += probability[i-1];
        
        for(int i = 0; i < probability.length; i++)
            if(probability[i] > random_choice){
                choice = i;
                break;
            }
                
        // for(int i = 0; i < probability.length; i++)
            // System.out.println("Probability: "+probability[i]+" random choice: "+random_choice);
        
        MixedStrategy ms;
        switch(choice){
            case 0:
                MaxMinPayoff a0 = new MaxMinPayoff();
                ms = a0.solveGame(mg, playerNumber);
                method_used = 0;
                break;
                
            case 1:
                MinMaxRegret a1 = new MinMaxRegret();
                ms = a1.solveGame(mg, playerNumber);
                method_used = 1;
                break;
            
            default:
                MaxAverage a2 = new MaxAverage();
                ms = a2.solveGame(mg, playerNumber);
                method_used = 2;
                break;
        }
        return ms;
    }
}
