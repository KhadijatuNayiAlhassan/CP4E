//  import java.util.Arrays;
public class Tutorial{
 // declaring an enum
 public enum DaysOfWeek{MON,TUE,WED,THUR,FRI,SAT,SUN};
 
 System.out.println(DaysOfWeek.MON);
 
  public static void main(String [] args){
//    // different ways of declaring an array
//    //int [] a = new int [2];// we are creating a new list with tow spaces at index 0 and 1
//    //a[0] = 1; // at index 0 in a, put 1
//    //a[1] = 2;
//     
//   // int d = a[0]*a[1];
//    System.out.println(d);
//    //System.out.println(Arrays.toString(a)); // toString converts a to string and then prints it
//  
//    // another way of initialising arrays
//    int [] b = {3,4,5};
//    
//    //third way of declaring a variable
//    Integer [] c = new Integer [] {7,8,9};
//    //System.out.println(Arrays.toString(c));
//    
//    // special literal methods
//     //System.out.println("Hi/there"); //this prints hi tab here
      int a = 100;
        int d = 10;
        int b = a-- - --d+ d++;
       System.out.println(a);
       System.out.println(b);
       System.out.println(d);
  }


}