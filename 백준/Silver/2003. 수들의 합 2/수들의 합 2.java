import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int [] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int start = 0;
        int end = 0;
        int sum = 0;
        int cnt = 0;

        while (true) {

            // 현재 합이 목표 숫자보다 크면 start 포인트 줄이기
            if (sum > M) {
                sum -= arr[start++];
            }
            // 끝까지 다 갔으면 종료
            else if (end == N) {
                break;
            }
            // 현재 합이 목표 숫자보다 작다면 end 포인트 늘리기
            else {
                sum += arr[end++];
            }

            // 포인터 조정 후 합이 M과 같은지 확인
            if (sum == M) {
                cnt++;
            }
        }

        System.out.println(cnt);
    }
}
