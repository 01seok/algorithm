import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            for (int s = 0; s < n - i; s++) sb.append(' ');
            for (int k = 0; k < 2 * i - 1; k++) sb.append('*');
            sb.append('\n');
        }
        for (int i = n - 1; i >= 1; i--) {
            for (int s = 0; s < n - i; s++) sb.append(' ');
            for (int k = 0; k < 2 * i - 1; k++) sb.append('*');
            sb.append('\n');
        }
        System.out.print(sb.toString());
    }
}