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
        float [] scores = new float[N];
        float maxScore = 0;
        for (int i = 0; i < N; i++) {
            scores[i] = Integer.parseInt(st.nextToken());
            if (scores[i] > maxScore) {
                maxScore = scores[i];

            }
        }
        float sumScore = 0;
        for (int i = 0; i < N; i++) {
            scores[i] = scores[i] / maxScore*100;
            sumScore += scores[i];
        }
        System.out.print(sumScore/N);

        br.close();
    }
}