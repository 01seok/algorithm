import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int ans = 0;

        for (int i =0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());

            boolean isAns = true;

            if (num < 2) {
                isAns = false;
            } else {
                for (int j = 2; j * j <= num; j++) {
                    if (num % j == 0) {
                        isAns = false;
                        break;
                    }
                }
            }
            if (isAns) {
                ans++;
            }
        }
        System.out.println(ans);
        br.close();
    }
}