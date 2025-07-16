import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String quizResult = br.readLine();

            int total = 0;
            int bonusScore = 0;

            for (int j = 0; j < quizResult.length(); j++) {
                char curChar = quizResult.charAt(j);
                if (curChar == 'O') {
                    bonusScore++;
                    total += bonusScore;
                } else {
                    bonusScore = 0;
                }
            }
            System.out.println(total);
        }
        br.close();
    }
}