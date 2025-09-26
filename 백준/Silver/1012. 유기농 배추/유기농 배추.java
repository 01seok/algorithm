import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int M, N; // 가로, 세로
    static  int[][] map; // 2차원 배열 맵
    static boolean[][] visited; // visited 배열
    static int[] dr = {0, 0, -1, 1}; // 델타 배열
    static int[] dc = {-1, 1, 0, 0};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken()); // 배추 수

            map = new int[N][M];
            visited = new boolean[N][M];

            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                int c =  Integer.parseInt(st.nextToken());
                int r = Integer.parseInt(st.nextToken());
                map[r][c] = 1;
            }

            int cnt = 0;
            // 배추 밭 스캔
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < M; c++) {
                    if (map[r][c] == 1 && !visited[r][c]) {
                        bfs(r,c);
                        cnt ++;
                    }
                }
            }
            System.out.println(cnt);
        }
    }

    public static void bfs(int startR, int startC) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {startR, startC});
        visited[startR][startC] = true;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int cur_r = cur[0];
            int cur_c = cur[1];

            for (int d = 0; d < 4; d++) {
                int nextR = cur_r + dr[d];
                int nextC = cur_c + dc[d];

                if (0 <= nextR && nextR < N && 0 <= nextC && nextC < M &&  !visited[nextR][nextC] && map[nextR][nextC] == 1) {
                    queue.add(new int[] {nextR, nextC});
                    visited[nextR][nextC] = true;
                }
            }
        }
    }
}
