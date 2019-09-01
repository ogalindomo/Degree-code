import java.util.Scanner;
import java.util.Stack;
public class Postfix
{
   public static void main(String[] args)
   {
     System.out.println("Please introduce your expression, do not add spaces.");
     Scanner in = new Scanner(System.in);
     String read = in.nextLine();
     System.out.print("Input:"+read);
     in.close();
     
     Stack numbers = new Stack();
     Stack signs = new Stack();
     Stack toCalc = new Stack();
     Stack postOrder = new Stack();
     Stack result = new Stack();
     //String toCalculate = "";
     System.out.println(" ");
     System.out.print("Post-Order:");
     for(int i = 0; i < read.length(); i++)
     {
       if(read.charAt(i) == '0'||read.charAt(i) == '1'||read.charAt(i) == '2'||read.charAt(i) == '3'||read.charAt(i) == '4'||
          read.charAt(i) == '5'||read.charAt(i) == '6'||read.charAt(i) == '7'||read.charAt(i) == '8'||read.charAt(i) == '9')
        {
          numbers.push(read.charAt(i));
          System.out.print(read.charAt(i));
          toCalc.push(read.charAt(i));
        }
       else if(read.charAt(i) == '+'||read.charAt(i) == '/'||read.charAt(i) == '-'||read.charAt(i) == '*')
          signs.push(read.charAt(i));
       else if(read.charAt(i) == ')')
       {
          char sign = (char)signs.pop();
          System.out.print(sign);
          toCalc.push(sign);
       }
     }
     while(!(signs.isEmpty()))
     {
       char sign = (char)signs.pop();
       System.out.print(sign);
       toCalc.push(sign);
     }
     System.out.println("");
     while(!(toCalc.isEmpty()))
        postOrder.push(toCalc.pop());
     
     while(!(postOrder.isEmpty()))
     {
        char reading = (char)postOrder.pop();
        if(reading == '0'||reading == '1'||reading == '2'||reading == '3'||reading == '4'||reading == '5'||reading == '6'||
           reading == '7'||reading == '8'||reading == '9')
            result.push((double)(char)reading - '0');
        
        else if(reading == '+')
        {
          double left = (double)(result.pop());
          double right = (double)(result.pop());
          double resultOperation = left+right;
          result.push(resultOperation); 
        }
        else if(reading == '*')
        {
          double left = (double)(result.pop());
          double right = (double)(result.pop());
          double resultOperation = left*right;
          result.push(resultOperation);  
        }
        else if(reading == '/')
        {
          double left = (double)(result.pop());
          double right = (double)(result.pop());
          double resultOperation = right/left;
          result.push(resultOperation);    
        }
        else if(reading == '-')
        {
          double left = (double)(result.pop());
          double right = (double)(result.pop());
          double resultOperation = right-left;
          result.push(resultOperation);   
        }
     }
     System.out.println("Result:"+result.pop());
     System.out.println("");
   }
}
