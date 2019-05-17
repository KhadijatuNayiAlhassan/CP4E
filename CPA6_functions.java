public class CPA6_functions{
    String  n;
    public CPA6_functions(String  n){
        this.n = n;
    }
    
    public int find_sum(String n){
        try {
            int sum_num = 0;
            int i = 0;
            while(i < this.n.length()){

                char num = this.n.charAt(i);
                String number = Character.toString(num);// converts char to string
                int number1 = Integer.parseInt(number);
                System.out.println(number1);
                sum_num  = sum_num + number1;
                i++;
            }
            System.out.println(sum_num);
            return sum_num;
            }

        catch (Exception e) {
            System.out.println("Please check your input,it should be a whole number");
        }
        return 0;
    }

    }
