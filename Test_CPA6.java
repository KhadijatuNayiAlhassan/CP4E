import java.util.Scanner;

public class Test_CPA6{
    public static void main(String[]args){
      
        System.out.print("Please enter a number: "); //asks for input from the user
        Scanner ix = new Scanner(System.in);
        String  n = ix.next();
       
        if(n.length() > 0){ // checks the length of the input
            CPA6_functions Run = new CPA6_functions(n);
            Run.find_sum(n);
            ix.close();
        } 
        else{ // empty string denotes void input
            System.out.println("your input is void, please enter a number");//if void input, this statement is displayed
        }
    }
}