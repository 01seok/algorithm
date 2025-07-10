import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());

//        String token = st.nextToken();
        int N = Integer.parseInt(br.readLine());

        for (int i = 1; i <= N; i++) {
            System.out.println(i);
        }


    }
}