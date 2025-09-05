import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int x = a, y = b;
            while (y != 0) {
                int temp = y;
                y = x % y;
                x = temp;
            }
            System.out.println(a * b / x);
        }
    }
}