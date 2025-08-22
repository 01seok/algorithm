import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String a = scanner.next();
        String b = scanner.next();

        String reversedA = new StringBuilder(a).reverse().toString();
        String reversedB = new StringBuilder(b).reverse().toString();

        int numA = Integer.parseInt(reversedA);
        int numB = Integer.parseInt(reversedB);

        System.out.println(Math.max(numA, numB));

        scanner.close();
    }
}