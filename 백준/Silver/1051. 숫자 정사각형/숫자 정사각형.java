import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] arr = new int[N][M];

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = str.charAt(j) - '0';
            }
        }
        // 최소 1x1
        int max = 1;

        // 모든 시작점
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {

                // 1칸씩 넓혀가며 정사각형 확인
                for (int k = 1; i+k<N && j+k <M; k++)  {
                    int num = arr[i][j];

                    // 꼭지점 비교
                    if (arr[i][j+k] == num &&
                    arr[i+k][j] == num &&
                    arr[i+k][j+k] == num) {
                        max = Math.max(max, (k+1) * (k+1));
                    }
                }
            }
        }
        System.out.println(max);
    }
}
