import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int c = sc.nextInt();
            System.out.printf("%d %d %d %d\n", c / 25, (c % 25) / 10, (c % 25 % 10) / 5, c % 5);
        }
    }
}