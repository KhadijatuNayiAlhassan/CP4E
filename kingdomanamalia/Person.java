  package kingdomanamalia;
public class Person{
  
  private double height;
  private double age;
    
  public Person(double height, double age){ 
    this.height = height;
    this.age = age;
  }
  
  public double getHeight(){
    return this.height;
  }
  
  public void setHeight( double height){
    this.height = height;
  }
  
  public double getAge(){
    return this.age;
  }
  
    public void setAge(double age){
      this.age = age;
    }
}