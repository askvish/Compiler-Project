import java.io.*;

class Function {

  int a, b, c, d, e;

  public static void calculate() {
    c = a + b;
  }

  public static void main(String[] args) {
    Scanner in;
    in = new Scanner();
    b = in.nextInt();
    a = in.nextInt();
    calculate();
    System.out.println(c);
  }
}
