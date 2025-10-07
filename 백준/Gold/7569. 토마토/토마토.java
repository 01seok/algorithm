import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());

        // 3차원 박스 배열
        int[][][] box = new int[H][N][M];
        // 큐 생성
        Queue<int[]> q = new LinkedList<>();

        // 안 익은 토마토, 처음부터 0이면 0 출력
        int unripeTomatoes = 0;

        // 층 마다 세로 길이 만큼 입력 들어옴
        for (int h = 0; h < H; h++) {
            for (int n = 0; n < N; n++) {
                st = new StringTokenizer(br.readLine());
                for (int m = 0; m < M; m++) {
                    int state = Integer.parseInt(st.nextToken());
                    box[h][n][m] = state;

                    if (state == 1) {
                        q.add(new int[]{h, n, m, 0});
                    } else if (state == 0) {
                        unripeTomatoes++;
                    }
                }
            }
        }
        // 처음부터 토마토가 다 익어있으면 종료
        if (unripeTomatoes == 0) {
            System.out.println(0);
            return;
        }

        int days = 0;
        int[] dh = {-1, 1, 0, 0, 0, 0};
        int[] dr = {0, 0, -1, 1, 0, 0};
        int[] dc = {0, 0, 0, 0, -1, 1};

        while (!q.isEmpty()) {
            int[] cur =  q.poll();
            int curH = cur[0];
            int curN = cur[1];
            int curM = cur[2];
            int curDay = cur[3];

            // 현재 날짜로 갱신
            days = curDay;

            for (int d = 0; d < 6; d++) {
                int nextH = curH + dh[d];
                int nextN = curN + dr[d];
                int nextM = curM + dc[d];

                if (0 <= nextH && nextH < H && 0 <= nextN && nextN < N && 0 <= nextM && nextM < M) {
                    if (box[nextH][nextN][nextM] == 0) {
                        box[nextH][nextN][nextM] = 1;
                        q.add(new int[]{nextH, nextN, nextM, curDay+1});
                        unripeTomatoes--;
                    }
                }
            }
        }

        if (unripeTomatoes > 0) {
            System.out.println(-1);
        } else if (unripeTomatoes == 0) {
            System.out.println(days);
        }

    }
}
