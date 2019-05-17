// writing a class and invocator in the same class
public class Justice{
  public Justice(){}
  public enum Aix{MALE,FEMALE}
  
    public static void main(String[] args){
//    // explain the diff between char and string
//      char a ='a';
//      String b = "Kofi";
//      
//      //explain indexing
//      char c  = b.charAt(1); //same as [] in python
//      //System.out.println(c);   //returns o
//      String bb = b+c;
//      String cc = b+b;
//      int dd = c+c; // + operator converts c into the ascii values so returns 222. adding two chars give a number
//      
//      
//      //System.out.println(cc);
      
//      // using stringbuilder class for manipulation
//      StringBuilder dd = new StringBuilder("Kwame Justice"); // before we use the class we need to create an instance of the class. we are 
//                                                                                               // literally saying dd="Kwame Justice"
//      char p = 'f';
//      dd.setCharAt(1,'o');   // replace the character at index 1 with o, returns koame Justice
//      dd.insert(3,p);  // results in a shift, adds character at index 3
//      System.out.println(a);  // Koafme Justice
//      
//      
//      
//      // data types
//      int a = 8;
//      Integer b = new Integer(12);
//      int c = a+b;
//      int d = b.intValue(); //getter
//      System.out.println(c);
//      
      
//      // Array
//      //Unlike python java does not allow us to put different things in an array
//      int[]p = {2,4,9};
//      integer []q=new Integer[]{2,4,9};
//      Integer[]w = new Integer[3];// the 3 creates 3 empty spaces 
//      w[0]=2;
//      w[1]=4;
//      w[2]=9;
//      
//      System.out.println(w[0]);
//      //enumeration is a list that is clearly defined and does not change
//      Aix ix;
//      ix = Aix.MALE;
//      System.out.println(ix);
//      
//      //Concatenation
//      char s = 'c';
//      String p = "Ko";
//      int w = s+s;
//      String d = s+p;
//      String e = p + 5;
      //Increment and decrement operators
      int p =4;
      int w = p++;
      int s = ++p;
      int d = w+--s;
      System.out.println(p);
      System.out.println(w);
      System.out.println(p);
      System.out.println(s);
      System.out.println(p);
      System.out.println(d);
      System.out.println(p);
      
      int ww = d+++s;
      int ww1 = d+s++;
      int  ww2 = ++d-s--;
      System.out.println(ww);
      System.out.println(ww1);
      System.out.println(ww2);
      
      
//      // type casting
//      int d = 4;
//      double f = 2.9;
//      double dd = (double) d; //converts d from int to double
//      int ff = (int) f; // converts from double to int
//      // casting with strings 
//      string ffd = Integer.toString(d) + 's';
//      String ds = "212";
//      int dx = Integer.parseInt(ds);
//      
//      //implicit type casting
//      double w = 4 + 5.2;  // java automatically converts 4 to 4.0 and adds. this is implicit type casting
//      
      }
    }
  
  

