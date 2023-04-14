import java.io.*;

class expression {

  int k;

  public static void main(String[] args) {
    int a, b, c, d, f, g, h, i;
    a = 5 + 6;
    b = 6 - a;
    c = a * b;
    if (a == 7 || b >= 6) {
      if (c < b) {
        System.out.println(1);
      }
      f = a + c;
    } else {
      System.out.println(0);
    }
  }
}
