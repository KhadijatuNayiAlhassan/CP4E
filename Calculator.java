public class Calculator {
  private int a; // declaration of instance variables
  private int b; // this a and b 
  
  public Calculator(){} // constructor 
  public Calculator(int x,int y){  // we want to have control over the variables x and y, so we make a constructor 
                                   // which stores the input x and y in a and b
    a = x;
    b = y;
    
  }
  public int addNum(int a,int b){
    //int c = a + b;
    int d = this.a +this.b;
    return d;
  }
}