import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 자바 알고리즘 재활 시작 1일차
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 100 x 100 2차원 배열 생성 (default = 흰색, false)
        boolean[][] paper = new boolean[100][100];

        // 검은색 영역 저장할 변수
        int totalArea = 0;

        // 첫 줄에 있는 색종이 개수
        int N = Integer.parseInt(br.readLine());

        // 색종이 개수만큼 반복
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            // 입력 받은 x,y 좌표로 부터 10칸씩 검은색으로 색칠
            for (int r = x; r < x + 10; r ++) {
                for (int c = y; c < y + 10; c ++) {

                    // 색칠 안되어있는 칸이면 true로 처리
                    if (!paper[r][c]) {
                        paper[r][c] = true;
                        totalArea++;
                    }
                }
            }
        }
        System.out.println(totalArea);
    }
}
