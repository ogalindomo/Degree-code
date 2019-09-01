import java.util.*;
import java.lang.*;
import java.io.*;
public class Search
{
    boolean[][] visited; //State checking board. 
    int size_x, size_y; //Size of the board of nodes.
    int init_x, init_y; //Coordinates of the initial position 
    int goal_x, goal_y; //Coordinates of the goal position.
    Position position [][]; //Array of the nodes used in the search algorithms.
    int time = 0; //in ms
    int numNodesExpanded; //Nodes used in aby iteration.
    int maxNumNodes= 1; //Maximum number of nodes used during execution.
    long start; //The long representation of time at which any execution starts.
    boolean cutoffHappened; //Boolean to indicate cutoff in Iterative Deepening Search.
    
    public static void main(String[] args)
    {
        try{
            new Search(new Scanner(new File(args[0])), args[1]); //Initialization of the searching, file and method received as arguments.
        }
        catch(IOException e){
            System.out.println("File was not found");
        }
        catch(Exception err){
            System.out.println("Something unexpected happened. Check the arguments given.");
        }
    }

    private Search(Scanner in, String searchmode)
    {
        try{
            get_sizes(in);//Imports the data of the goal, the end state, and the size of the board.
            position = new Position [size_x][size_y];//Creates an array of the size of the board indicated in the file.
            visited = new boolean [size_x][size_y];//Creates a boolean array to have a state checking during the searches.
            makeBoard(in);//Populates the position board with the information of every node.
            if(searchmode.equalsIgnoreCase("BFS"))//The search algorithm is selected according to the type.
                BFS();
            else if(searchmode.equalsIgnoreCase("IDS"))
                iterativeDeepeningSearch();
            else
                AStar();
        }
        catch(Exception e){
            System.out.println("Something went wrong, please check the the file that was referenced has all the necessary elements.");
        }
    }

    void BFS()//Breadth First Search
    {
        Queue list = new LinkedList();
        Position root = position[init_x][init_y];
        list.add(root);

        start = System.nanoTime(); //Timer is initialized
        while (!list.isEmpty() && time < 180000)
        {
            time = (int)((double)(System.nanoTime() - start) / 1_000_000.0); //Time into the algorithm is calculated.
            
            if(list.size() > maxNumNodes) maxNumNodes = list.size(); //The maximum number of nodes used is updated. 
            
            
            Position current = (Position)list.remove(); //The immediate next element is remove from the Queue.
            if(current == position[goal_x][goal_y])
            {
                time = (int)((double)(System.nanoTime() - start) / 1_000_000.0);//Time taken is stored
                printPath(current, 0, "BFS");//The path is sent to be printed.
                return;
            }

            //The node visits its child immediately up only if the position has a cost not equal to zero and the child has not been visited before.
            if(current.x -1 > 0 && !visited[current.x-1][current.y] && position[current.x-1][current.y].cost !=0){ 
                position[current.x-1][current.y].parent = current;
                numNodesExpanded++;
                list.add(position[current.x-1][current.y]);
            }
            
            //The node visits its child immediately to the right only if the position has a cost not equal to zero and the child has not been visited before.
            if(current.y + 1 < size_y && !visited[current.x][current.y + 1] && position[current.x][current.y + 1].cost != 0){
                position[current.x][current.y+1].parent = current;
                numNodesExpanded++;
                list.add(position[current.x][current.y+1]);
            }
            
            //The node visits its child immediately to the left only if the position has a cost not equal to zero and the child has not been visited before.
            if(current.y - 1 > 0 && !visited[current.x][current.y-1] && position[current.x][current.y - 1].cost != 0){
                position[current.x][current.y-1].parent = current;
                numNodesExpanded++;
                list.add(position[current.x][current.y-1]);
            }
            
            //The node visits its child immediately down only if the position has a cost not equal to zero and the child has not been visited before.
            if(current.x + 1 < size_x && !visited[current.x+1][current.y] && position[current.x + 1][current.y].cost != 0){
                position[current.x+1][current.y].parent = current;
                numNodesExpanded++;
                list.add(position[current.x+1][current.y]);
            }
            visited[current.x][current.y] = true; //The last element evaluated for possible childs is set as visited.
        }
        if(time >= 180000)System.out.println("BFS ran out of time!"); //If the time runs out of time it displays so.
        else{
            time = (int)((double)(System.nanoTime() - start) / 1_000_000.0);//Time is calculated if it fails to find an answer.
            printPath(null, -1, "BFS");
        }
    }

    void iterativeDeepeningSearch(){
        start = System.nanoTime(); //Timer is initialized
        for(int depth = 0; time < 180000; depth++){
            time = (int)((double)(System.nanoTime() - start) / 1_000_000.0);//Time is recalculated after every iteration.
            resetBoard();//Visited board is reseted after the depth is extended. 
            Position result = depthLimitedSearch(depth);//Result is obtained out of the recursive call.
            if(result.failure){
                time = (int)((double)(System.nanoTime() - start) / 1_000_000.0);
                printPath(null, -1, "IDS");
                return;
            }
            if(!result.cutoff){
                time = (int)((double)(System.nanoTime() - start) / 1_000_000.0);
                printPath(result,0,"IDS");
                return;
            }
        }
        System.out.println("IDS search ran out of time."); //This message is displayed if the search runs out of time. 
    }

    Position depthLimitedSearch(int limit){//A recursive search is initialized with a new depth limit.
        return recursiveDepthLimited(position[init_x][init_y], limit, 1);
    }

    Position recursiveDepthLimited(Position current, int limit, int nodenum){
        visited[current.x][current.y] = true; //The current node evaluated is set as visited.
        
        if(maxNumNodes < nodenum) maxNumNodes = nodenum; //If the maximum number of expanded nodes is found then 
        if(current == position[goal_x][goal_y]){ //If the goal is the position then it is returned.
            return current;
        }
        else if (limit == 0) //If the limit is achieved then a cutoff occurs and the 
        {
            current.cutoff = true;
            return current;
        }
        else{
            cutoffHappened = false; 
            Position result;
            //The node visits its child immediately up only if the position has a cost not equal to zero and the child has not been visited before.
            if(current.x -1 > 0 && !visited[current.x-1][current.y] && position[current.x-1][current.y].cost !=0){
                position[current.x-1][current.y].parent = current; //The child's parent is sent to be the current node.
                visited[current.x - 1][current.y] = true; //The current node is set as visited.
                numNodesExpanded++;
                result = recursiveDepthLimited(position[current.x - 1][current.y], limit - 1, nodenum + 1); //Result of the recursive call is obtained
                if (result.cutoff == true) //If a cutoff occurs the state of the cutoff variable is updated.
                    cutoffHappened = true;
                else if (!current.failure){ //If a fialure occurs- that is you are trapped the node, containing the failure is returned.
                    return result;
                }
            }
            
            //The node visits its child immediately to the right only if the position has a cost not equal to zero and the child has not been visited before.
            if(current.y + 1 < size_y && !visited[current.x][current.y + 1] && position[current.x][current.y + 1].cost != 0){
                position[current.x][current.y+1].parent = current; //The child's parent is sent to be the current node.
                visited[current.x][current.y + 1] = true; //The current node is set as visited.
                numNodesExpanded++;
                result = recursiveDepthLimited(position[current.x][current.y+1], limit - 1, nodenum + 1); //Result of the recursive call is obtained
                if (result.cutoff == true) //If a cutoff occurs the state of the cutoff variable is updated.
                    cutoffHappened = true;
                else if (!current.failure){ //If a fialure occurs- that is you are trapped the node, containing the failure is returned.
                    return result;
                }
            }
            
            //The node visits its child immediately to the left only if the position has a cost not equal to zero and the child has not been visited before.
            if(current.y - 1 > 0 && !visited[current.x][current.y-1] && position[current.x][current.y - 1].cost != 0){
                position[current.x][current.y-1].parent = current; //The child's parent is sent to be the current node.
                visited[current.x][current.y - 1] = true; //The current node is set as visited.
                numNodesExpanded++;
                result = recursiveDepthLimited(position[current.x][current.y-1], limit - 1, nodenum + 1); //Result of the recursive call is obtained
                if (result.cutoff == true) //If a cutoff occurs the state of the cutoff variable is updated.
                    cutoffHappened = true;
                else if (!current.failure){ //If a fialure occurs- that is you are trapped the node, containing the failure is returned.
                    return result;
                }
            }
            
            //The node visits its child immediately down only if the position has a cost not equal to zero and the child has not been visited before.
            if(current.x + 1 < size_x && !visited[current.x+1][current.y] && position[current.x + 1][current.y].cost != 0){
                position[current.x+1][current.y].parent = current; //The child's parent is sent to be the current node.
                visited[current.x + 1][current.y] = true; //The current node is set as visited.
                numNodesExpanded++;
                result = recursiveDepthLimited(position[current.x+1][current.y], limit - 1, nodenum + 1); //Result of the recursive call is obtained
                if (result.cutoff == true) //If a cutoff occurs the state of the cutoff variable is updated.
                    cutoffHappened = true;
                else if (!current.failure){ //If a fialure occurs- that is you are trapped the node, containing the failure is returned.
                    return result;
                }
            }
        }
        if (cutoffHappened == true){ //A cutoff is returned if during the recursions the a cutoff occured.
            current.cutoff = true;
            return current;
        }
        else{ //If during the execution a failure is found then a node containing that information is returned.
            current.failure = true;
            return current;
        }
    }

    void AStar()
    {
        Comparator<Position> comparator = new PositionComparator();
        PriorityQueue list = new PriorityQueue(1, comparator);
        list.add(position[init_x][init_y]);

        start = System.nanoTime();
        int global_optimal = 0;
        visited[init_x][init_y] = true;
        while (!list.isEmpty() && time < 180000)
        {
            time = (int)((double)(System.nanoTime() - start) / 1_000_000.0);
            if(list.size() > maxNumNodes) maxNumNodes = list.size(); //Maximum number of nodes considered is updated after every iteration.
            Position current = (Position)list.poll();
            
            //The node visits its child immediately up only if the position has a cost not equal to zero and the child has not been visited before.
            if(current == position[goal_x][goal_y])            
            {
                time = (int)((double)(System.nanoTime() - start) / 1_000_000.0); //Before the answer is displayed the time is calculated.
                printPath(current, 0, "A*"); //Answer is sent to be displayed.
                global_optimal = sum_path(current, 0); //Optimal is calculated.
                return;
            }

            if(current.x -1 > 0 && !visited[current.x-1][current.y] && position[current.x-1][current.y].cost !=0){
                position[current.x-1][current.y].parent = current;
                position[current.x-1][current.y].cumulativeCost = current.cumulativeCost + position[current.x-1][current.y].cost;
                visited[current.x-1][current.y] = true;
                list.add(position[current.x-1][current.y]);
                numNodesExpanded++;
            }
            
            //The node visits its child immediately to the right only if the position has a cost not equal to zero and the child has not been visited before.
            if(current.y + 1 < size_y && !visited[current.x][current.y + 1] && position[current.x][current.y + 1].cost != 0){
                position[current.x][current.y+1].parent = current;
                position[current.x][current.y+1].cumulativeCost = current.cumulativeCost + position[current.x][current.y+1].cost;
                visited[current.x][current.y+1] = true;
                list.add(position[current.x][current.y+1]);
                numNodesExpanded++;
            }
            
            //The node visits its child immediately to the left only if the position has a cost not equal to zero and the child has not been visited before.
            if(current.y - 1 > 0 && !visited[current.x][current.y-1] && position[current.x][current.y - 1].cost != 0){
                position[current.x][current.y-1].parent = current;
                position[current.x][current.y-1].cumulativeCost = current.cumulativeCost + position[current.x][current.y-1].cost;
                visited[current.x][current.y-1] = true;
                list.add(position[current.x][current.y-1]);
                numNodesExpanded++;
            }
            
            //The node visits its child immediately down only if the position has a cost not equal to zero and the child has not been visited before.
            if(current.x + 1 < size_x && !visited[current.x+1][current.y] && position[current.x + 1][current.y].cost != 0){
                position[current.x+1][current.y].parent = current;
                position[current.x+1][current.y].cumulativeCost = current.cumulativeCost + position[current.x+1][current.y].cost;
                visited[current.x+1][current.y] = true;
                list.add(position[current.x+1][current.y]);
                numNodesExpanded++;
            }
            //visited[current.x][current.y] = true;
        }
        if(time >= 180000 )System.out.println("A* ran out of time!"); // If the time runs out the search displays a message.
        else{
            time = (int)((double)(System.nanoTime() - start) / 1_000_000.0);//Before an answer is displayed the time it took to end is calculated.
            printPath(null, -1, "A*"); //The fialure to find a path is sent to be printed.
        }
    }

    void resetBoard() //The visited array, which checks the states that were visited is re-initialized.
    {
        for(int i = 0; i < visited.length; i++)
            for(int j = 0; j < visited[i].length;j++)
                visited[i][j] = false;
    }

    void printPath(Position element, int sum, String method)//Prints the information once the searching has been finished. 
    {
        if(sum == -1 || element.parent == null)
        {
            System.out.println("Method: " + method);
            System.out.println("Total Cost: "+ sum);
            System.out.println("Number of Nodes Expanded: " + numNodesExpanded);
            System.out.println("Maximum number of nodes held in memory: " + maxNumNodes );
            System.out.println("Time: " + time + "ms");
            if (sum == -1)
                System.out.println("Path Squence: NULL");
            else 
                System.out.println("Start: X:" + (element.x) + " Y:" + (element.y));
            return;
        }
        else{
            printPath(element.parent, sum+element.cost, method);
            System.out.println("Coordinates: X:"+(element.x)+" Y:"+(element.y)+" Cost:"+element.cost);
        }
    }
    
    private class Position //Child class which contains the information about the nodes neing visited and the results of the paths traveled.
    {
        int x, y, cost;
        boolean cutoff, failure;//Booleans utilized during Iterative Deepening Search to indicate the status of extending the depth in the direction of this node.
        int cumulativeCost = 0;
        Position parent;
        private Position(int x, int y, int cost)
        {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }
    }

    private class PositionComparator implements Comparator<Position> //This class implements the Comparator interface for the Posisitons priorization in the Priority Queue.
    {
        public int compare(Position e1, Position e2){
            int fe1 = manhattanDistance(e1.x,e1.y) + e1.cumulativeCost;
            int fe2 = manhattanDistance(e2.x,e2.y) + e2.cumulativeCost;
            return (fe1 > fe2) ? 1 : (fe1 == fe2) ? 0 : -1; //If the cost of e1 is greated than e2 return a 1, if the cost of e1 is equal than e2 return 0, else return -1. 
        }
    }

    int sum_path(Position element, int sum){ //Sums the total cost of the path traveled but excludes the cost from where you start.
        if(element.parent == null)
            return sum;
        else
            return sum_path(element.parent, sum+element.cost);
    }

    int manhattanDistance(int x_src, int y_src) //Calculate the Manhattan distance.
    {
        return (Math.abs(x_src-goal_x) + Math.abs(y_src-goal_y));
    }

    void get_sizes(Scanner in) throws Exception //Reads the first lines of the file and imports the information into the global variables.
    {
        String[] sizes = in.nextLine().split(" ",-2);
        size_x = Integer.parseInt(sizes[0]);
        size_y = Integer.parseInt(sizes[1]);
        System.out.println("Size of Board X:"+size_x+" Y:"+size_y);
        String[] start = in.nextLine().split(" ",-2);
        init_x = Integer.parseInt(start[0]);
        init_y = Integer.parseInt(start[1]);
        System.out.println("Start Coordinates: X:"+init_x+" Y:"+init_y);
        String[] goal = in.nextLine().split(" ",-2);
        goal_x = Integer.parseInt(goal[0]);
        goal_y = Integer.parseInt(goal[1]);
        System.out.println("Goal Coordinates: X:"+goal_x+" Y:"+goal_y);
    }

    void makeBoard(Scanner in) //The Position array is initialized with nodes containing the information in the file.
    {
        for(int i = 0; i < position.length; i++)
        {
            String temp [] = in.nextLine().split(" ",-2);
            for(int j = 0; j < temp.length; j++)
            {
                position[i][j] = new Position(i, j, Integer.parseInt(temp[j]));
                System.out.print(position[i][j].cost+" ");
            }
            System.out.println(" ");
        }
    }
}
