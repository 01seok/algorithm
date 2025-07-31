import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num1 = Integer.parseInt(br.readLine());
        int num2 = Integer.parseInt(br.readLine()); 

        int unit_digit = num2 % 10;
        int ten_digit = (num2 / 10) % 10;
        int hundred_digit = num2 / 100;

        System.out.println(num1 * unit_digit);
        System.out.println(num1 * ten_digit);
        System.out.println(num1 * hundred_digit);
        System.out.println(num1 * num2);

        br.close();
    }
}