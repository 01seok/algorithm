import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long S = Long.parseLong(br.readLine());

        long sum = 0L;
        int N = 0;
        long num = 1L;

        while (true) {
            sum += num;
            if (sum > S) {
                break;
            }
            N ++;
            num ++;
            }
        System.out.println(N);
    }
}
