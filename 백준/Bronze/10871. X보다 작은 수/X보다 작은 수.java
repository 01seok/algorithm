import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        StringBuilder sb = new StringBuilder(); // 효율적인 출력을 위해 가변 문자열 생성

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (num < X) {
                sb.append(num).append(" ");
            }
        }
        System.out.println(sb.toString().trim());
        // 제일 앞, 제일 뒤 공백 제거 trim, toString 안 쓰면 trim 사용 못함
    }
}