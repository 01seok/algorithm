import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int M, N;
    static int[][] box;

    static Queue<int[]> queue = new LinkedList<>();
    static int unripeTomatoes = 0;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken()); // 가로
        N = Integer.parseInt(st.nextToken()); // 세로
        box = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                int state = Integer.parseInt(st.nextToken());
                box[i][j] = state;

                // 익은 토마토는 시작점이니 큐에 추가 (0일차)
                if (state == 1) {
                    queue.add(new int[]{i, j, 0});
                } else if (state == 0) {
                    unripeTomatoes++; // 안 익은 토마토 갯수 추가
                }
            }
        }

        // 처음부터 모든 토마토가 다 익은 경우
        if (unripeTomatoes == 0) {
            System.out.println(0);
            return;
        }

        int days = 0;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int curR = current[0];
            int curC = current[1];
            int curDay = current[2];

            days = curDay;

            for (int d = 0; d < 4; d++) {
                int nextR = curR + dr[d];
                int nextC = curC + dc[d];

                if (nextR >= 0 && nextR < N && nextC >= 0 && nextC < M) {
                    if (box[nextR][nextC] == 0) {
                        box[nextR][nextC] = 1;
                        queue.add(new int[]{nextR, nextC, curDay + 1});
                        unripeTomatoes--;
                    }
                }
            }
        }
        // bfs가 끝났는데도 안 익은게 있다면 불가능
        if (unripeTomatoes > 0) {
            System.out.println(-1);
        } else {
            System.out.println(days);
        }
    }
}
