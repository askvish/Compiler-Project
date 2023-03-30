public class LongToString {
    public static void main(String[] args) {
        
        long lvar = 123;
        String str = String.valueOf(lvar);
        System.out.println("lvar is: "+lvar);
        
        long lvar2 = 200;
        String str2 = Long.toString(lvar2);
        System.out.println("lvar2 is: "+lvar2);
    }
}
