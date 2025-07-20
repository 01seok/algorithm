import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        // 1번 방 = 1개
        // 2~7번 방 = 2개
        // 8~19번방 = 3개
        // 20 ~ 37번방 = 4개
        // 6, 12, 18 .. 6의 배수
        int stair = 1; // 지나가는 방의 개수 (층)
        int nextStair = 2; // 다음 층의 첫 숫자 (갱신용)
        if (N == 1) {
            System.out.println(1);
        } else {
            while (nextStair <= N) {
                nextStair = nextStair + (6 * stair);
                stair++;
            }
            System.out.println(stair);
        }
        
        br.close();
    }
}