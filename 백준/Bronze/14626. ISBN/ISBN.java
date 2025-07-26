import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String isbn = br.readLine();

        int sum = 0;
        int missingIndex = -1;
        int[] weights = {1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1};

        for (int i = 0; i < 13; i++) {
            char c = isbn.charAt(i);
            if (c == '*') {
                missingIndex = i;
            } else {
                int digit = c - '0';
                sum += digit * weights[i];
            }
        }

        for (int x = 0; x <= 9; x++) {
            int totalSum = sum + (x * weights[missingIndex]);
            if (totalSum % 10 == 0) {
                System.out.println(x);
                break;
            }
        }
    }
}