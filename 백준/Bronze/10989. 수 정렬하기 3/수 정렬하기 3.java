import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] count = new int[10001];

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            count[num]++;
        }
        br.close();
        for (int i = 0; i < 10001; i++) {
            for (int j = 0; j <count[i]; j++) {
                sb.append(i).append('\n');
            }
        }
        System.out.print(sb);
    }
}

