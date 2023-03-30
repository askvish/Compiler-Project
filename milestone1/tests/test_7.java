
class Temp{  
    // function to convert temperature from degree Celsius to Kelvin  
    static float temperature(float celsius)  
    {  
        return (float)(celsius + 273.15);  
    }  
    public static void main (String[] args)  
    {  
        float celsius;  
        System.out.println("Enter the Temperature in Celsius: ");  
        Scanner sc = new Scanner(System.in);  
        celsius = sc.nextFloat();  
    System.out.println("The value of given Temperature in Kelvin (K) is = " + temperature(celsius));  
              
    }  
}  