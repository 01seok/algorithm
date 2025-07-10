import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());

//        String token = st.nextToken();
        int N = Integer.parseInt(br.readLine());

        if (N % 4 == 0 && (N % 100 != 0 || N % 400 == 0)) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }

    }
}