import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int sumOfSquare = 0;

        for (int i = 0; i < 5; i++) {
            String token = st.nextToken();
            int num = Integer.parseInt(token);
            sumOfSquare += num * num;
        }

        int result = sumOfSquare % 10;
        System.out.println(result);
    }
}