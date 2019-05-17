public class Student{
  private name;
  private age;
  private major;
  
  public Student(){
    System.out.println("the empty constructor ");
  }
    public Student(String name){
      System.out.println(" the constructor that takes a string pqrameter");
    }
      public Student(String name, int age){
        System.out.println("the constructor that takes a string and int parameters");
      }

      public Student(String name,int age, String major){
        this.name = name;    // this.name refers to the instance variable name but not the one as the constructor parameter
        this.age = age;         // if the instance variable = parameter in the constructor, we use this. to refer to the instance variable
        this.major = major;
        
        public String getName(){
          return this.name;
} 