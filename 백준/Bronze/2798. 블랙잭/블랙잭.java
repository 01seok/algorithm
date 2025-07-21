import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int [] cards = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }
        int max_sum = 0;

        for (int a = 0; a < N; a++) {
            for (int b = a+1; b < N; b++) {
                for (int c = b+1; c < N; c++) {
                    int new_sum = cards[a] + cards[b] + cards[c];
                    if (new_sum > max_sum && new_sum <= M) {
                        max_sum = new_sum;
                    }
                }
            }
        }
        System.out.println(max_sum);

        br.close();
    }
}