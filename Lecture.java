import java.util.Scanner;  // Scanner helps us to accept input from the user
public class Lecture{
//  private enum Month{JAN,FEB,OCT};
  public static void main(String[]args){
    Month d;
    d = Month.JAN;
    int x=4;
    if(x<4){
      System.out.println("x not less than 4");
    }
    else if(x>4){
      System.out.println("x not  not less than 4");
    }
     else{
        System.out.println("x not than 4");  //default
      }
     
      switch (d){  // using switch for an enum
          case JAN:
            System.out.println("January");
            break;
          case OCT:
           System.out.println("October");
     
            //do while loop 
      int p = 0; // initial for accumulator
      int i = 0; // initial for while loop
      do{
        p = p +1;  
        i++;  // post condition
      }while(i<5);
      System.out.println(p);
      System.out.println(i);z
      
       //while loop
      int p = 0;
      int i = 0;
      while (i<5){
        p+= i;
        i++;
      }
      System.out.print(p);
      System.out.print(i);// dont understand
      
      // getting an input from the user
      Scanner dx = new Scanner(System.in); // an instance of Scanner and the parameter implies that we want an input
      System.out.println("Enter a double");
      double f = dx.nextDouble();
      System.out.println("f");
      
      
}
}
      
//      // adding the members of an array
//      double[]g = {2,5,8,3};
//      double p = 0;
//        for (double c:g){ // this is like saying for c in g
//          p+=c;
//        }
//        System.out.println(p);
//}
//}
