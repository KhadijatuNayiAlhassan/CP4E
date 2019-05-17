public class constant{
    public static void main(String[]args){
        String empty = "";
        String name = "Khadijatu";
        int l = name.length();
        char a = 'a';
        char b = 'r';
        String  c = a + "";
        

        //for(int i:){
            //empty = empty + name.charAt(-i);
            for(int i = 0; i < l;i++){
                 empty = name.charAt(i) + empty;
                
            }
            System.out.println(empty);

        }

    }
