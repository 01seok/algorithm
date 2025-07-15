import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 1; i <= N; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 1; j <= N-i; j++) {
                sb.append(" ");
            }
            for (int k = 1; k <= i; k++) {
                sb.append("*");
            }
            System.out.println(sb.toString());
        }

        br.close();
    }
}