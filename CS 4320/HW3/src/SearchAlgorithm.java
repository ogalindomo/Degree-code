 
import java.util.*;
import java.lang.Math;
public class SearchAlgorithm {
   public void mutate(Schedule s, int x, int y, int range){
       Random rand = new Random();
       int mutation_cutoff = 10;
       boolean[] courses = new boolean[range];

       for(int r = 0; r < s.schedule.length; ++r)
          for(int c = 0 ; c < s.schedule[r].length; ++c)
               courses[s.schedule[r][c]] = true;

       for(int i = 0; i < mutation_cutoff; i++){
           int r_val = rand.nextInt(range);
           if(!courses[r_val]){
               s.schedule[x][y] = r_val;
               return;
           }
       }
   }

   // Your search algorithm should return a solution in the form of a valid
   // schedule before the deadline given (deadline is given by system time in ms)
   public Schedule solveGenetic(SchedulingProblem problem, long deadline) {
       System.out.println("Time amount received as parameter in Milliseconds: "+(deadline - System.currentTimeMillis()));
       int population_size = 50;
       double mutationRate= .05, sum = 0.0, fitness = 0.0;
       double[] score = new double[population_size];
       int range = problem.courses.size();
       Random rand = new Random();
       Schedule[] parents = new Schedule[population_size];

       // Initialize the population
       for(int i  = 0; i < population_size; i++){
          boolean[] courses = new boolean[range];
          parents[i] = problem.getEmptySchedule();
          int added_courses = 0;
          for(int r = 0; r < parents[i].schedule.length; r++){
              for(int c = 0 ; c < parents[i].schedule[r].length; c++){
                  int temp = rand.nextInt(range);
                  if (added_courses > range)
                      break;
                  else if (courses[temp] == false){
                      parents[i].schedule[r][c] = temp;
                      courses[temp] = true;
                      added_courses++;
                   }
                  else c--;
              }
              if (added_courses > range)
                  break;
          }
       }

       for(long t = System.currentTimeMillis();t < deadline-100; t = System.currentTimeMillis()){
          Schedule[] children = new Schedule[population_size];
          sum = 0;
          //evaluate_parents
          //System.out.print("Fitness: [");
          for(int i = 0; i < population_size; i++){
             fitness = problem.evaluateSchedule(parents[i]);
             if (fitness < 0) fitness = 0;
             sum += fitness;
             //System.out.print(fitness+", ");
             score[i] = sum;
          }
          //System.out.println("]");
          //System.out.println(sum + " ");
          //coordinates of current parents

          // Generate new population
          //works by taking two parents and making two children through crossover
          for(int i = 0; i < population_size; i+=2){
             double c1 = 0 + (sum - 0) * rand.nextDouble();
             double c2 = 0 + (sum - 0) * rand.nextDouble();
             if(c1 >  score[population_size-1]) System.out.println("error");
             for(int j = 0; j < population_size; j++){
                if(score[j] > c1){
                   children[i] = problem.getEmptySchedule();
                   this.copy(parents[j].schedule, children[i].schedule);
                   break;
                }
             }
             for(int j = 0; j < population_size; j++){
                if(score[j] > c2){
                   children[i+1] = problem.getEmptySchedule();
                   this.copy(parents[j].schedule, children[i+1].schedule);
                   break;
                }
             }

             //crossover
             int random_pivot = rand.nextInt(parents[0].schedule.length);
             //System.out.println(random_pivot);
             for(int k = 0; k < random_pivot; k++){
                for(int l = 0; l < parents[0].schedule[0].length; l++){
                   //System.out.println("k: " +k+ "  l: " +l + "  i: " + i);
                   int temp = children[i].schedule[k][l];
                   children[i].schedule[k][l] = children[i+1].schedule[k][l];
                   children[i+1].schedule[k][l] = temp;
                }
             }

             //check contradiction in crossover
             Stack<Integer> contradictions = new Stack<Integer>();
             //int numContradictions = 0;
             boolean[] courses1 = new boolean[range];
             for(int r = 0; r < parents[i].schedule.length; r++){
                for(int c = 0 ; c < parents[i].schedule[0].length; c++){
                   int temp = children[i].schedule[r][c];
                   if (courses1[temp] == false){
                      courses1[temp] = true;
                   }
                   else{
                      contradictions.push(r);
                      contradictions.push(c);
                   }
                }
             }
             int nv = 0;
             while (!contradictions.empty()){
                //find next valid
                for(; true; nv++){
                   if(courses1[nv] == false){
                      courses1[nv] = true;
                      break;
                   }
                }
                int c_temp = contradictions.pop();
                int r_temp = contradictions.pop();
                children[i].schedule[r_temp][c_temp] = nv;
             }

             boolean[] courses2 = new boolean[range];
             for(int r = 0; r < parents[i+1].schedule.length; r++){
               for(int c = 0 ; c < parents[i+1].schedule[0].length; c++){
                 int temp = children[i+1].schedule[r][c];
                 if (courses2[temp] == false){
                    courses2[temp] = true;
                 }
                 else{
                    contradictions.push(r);
                    contradictions.push(c);
                 }
               }
             }
             nv = 0;
             while (!contradictions.empty()){
                //find next valid
                for(; true; nv++){
                   if(courses2[nv] == false){
                      courses2[nv] = true;
                      break;
                   }
                }
                int c_temp = contradictions.pop();
                int r_temp = contradictions.pop();
                children[i+1].schedule[r_temp][c_temp] = nv;
             }
              //if(0 > problem.evaluateSchedule(children[i+1])) System.out.println("err before mutation");
             c1 = 0 + (1 - 0) * rand.nextDouble();
             c2 = 0 + (1 - 0) * rand.nextDouble();
             //mutation
             for(int r = 0; r < children[i].schedule.length; r++){
                for(int c = 0; c < children[i].schedule[r].length; c++){
                   if(c1 < mutationRate){
                     mutate(children[i], r, c, range);
                   }
                   if(c2 < mutationRate){
                     mutate(children[i+1], r, c, range);
                   }
                }
             }
                //if(0 > problem.evaluateSchedule(children[i+1])) System.out.println("err after mutation");
          }
          parents = children;
       }

       double max = 0.0;
       Schedule best = new Schedule(0,0);
       for(int i = 0; i < parents.length; i++)
       {
          if(max < problem.evaluateSchedule(parents[i])){
             max = problem.evaluateSchedule(parents[i]);
             best = parents[i];
          }
       }
       return best;
   }

   public Schedule solveAnnealing(SchedulingProblem problem, long deadline)
   {
      long start = System.currentTimeMillis();
      System.out.println("Time amount received as parameter in Milliseconds: "+(deadline - System.currentTimeMillis()));
      Schedule current = this.naiveBaseline(problem,deadline);
      System.out.println("Baseline score: "+ problem.evaluateSchedule(current));
      Schedule next;
      double max = 0.0;
      for(long t = System.currentTimeMillis();t < deadline-1; t = System.currentTimeMillis())
      {
         next = problem.getEmptySchedule();
         double T = schedule(t-start, (deadline-start)*0.99);
         if (T <= 0.0) return current;
         this.copy(current.schedule, next.schedule);
         Random rand = new Random();
         //Random Coordinates to move the values from the schedule.
         mutate(next, rand.nextInt(current.schedule.length), rand.nextInt(current.schedule[0].length), problem.courses.size());
         double delta_e = (problem.evaluateSchedule(next) - problem.evaluateSchedule(current)); //Difference
         if (delta_e > 0){
             current = next;
             max = problem.evaluateSchedule(next);
         }
         else{
             Random r = new Random();
             double probability = Math.pow(Math.E, (delta_e/T)); //Probability obtained
             double calculated_probability_value = 0.0 + (1.0 - 0.0) * r.nextDouble(); //Probability to compare against
             if(calculated_probability_value < probability)
             {
                current = next;
                max = problem.evaluateSchedule(next);
             }
         }
      }
      return current;
   }

   private void copy(int[][] src, int[][] copy){
      for(int i = 0; i < src.length; i++){
         for(int j = 0; j < src[i].length; j++){
             copy[i][j] = src[i][j];
         }
      }
   }

   public double schedule(double currentTime, double maximum){
      //Maximum Temperature will be close to 32 Celsius and Minimum will be close to 0.
      return Math.abs(((currentTime/maximum)*32) - 32);
   }

   // This is a very naive baseline scheduling strategy
   // It should be easily beaten by any reasonable strategy
   public Schedule naiveBaseline(SchedulingProblem problem, long deadline) {
     // get an empty solution to start from
     System.out.println("Time amount received as parameter: "+(deadline - System.currentTimeMillis()));
     Schedule solution = problem.getEmptySchedule();
     System.out.println("Size of the problem: "+ problem.courses.size());
     for (int i = 0; i < problem.courses.size(); i++) {
       Course c = problem.courses.get(i);
       boolean scheduled = false;
       for (int j = 0; j < c.timeSlotValues.length; j++) {
         if (scheduled) break;
         if (c.timeSlotValues[j] > 0) {
           for (int k = 0; k < problem.rooms.size(); k++) {
             if (solution.schedule[k][j] < 0) {
               solution.schedule[k][j] = i;
               scheduled = true;
               break;
             }
           }
         }
       }
     }
     return solution;
   }
}
