import java.util.Scanner;

//import com.sun.org.apache.xalan.internal.xsltc.util.IntegerArray;

public class TestSwitch{

    public enum Month{JAN,FEB};


    public static String test(String s){
       return Month.s;
    }

    public static void main(String[]args){
        System.out.println("Enter a Month(eg.JAN): ");
        Scanner swi = new Scanner(System.in);
        String s = swi.next();
        swi.close();
        System.out.println("the value you entered is: "+s);
        TestSwitch.test(s); // s is a string

        switch(s){
            case "JAN":
                System.out.println("January");
                break;
            case "FEB":
                System.out.println("February");
                break;
            default:    // that is if the user does not enter anything i declared, just break
              System.out.println("you entered the wrong month"); 
            break;

        }
        // while loop
        // int i = 0;
        // int list1[] = new int[8];{
        // while(i<=5){
        //     list1[i] = i;
        //     i++;
        // }
        // System.out.println(list1);
            
            

        


    }
}

