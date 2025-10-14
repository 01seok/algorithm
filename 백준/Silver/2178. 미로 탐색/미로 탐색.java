import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, M;
    static int[][] maze;
    static boolean[][] visited;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        maze = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                maze[i][j] = line.charAt(j) - '0';
            }
        }
        bfs(0, 0);
    }

    public static void bfs(int startR, int startC) {
        Queue<int[]> queue = new LinkedList<>();

        // queue 시작점 정보 (행, 열, 거리) 저장
        // 시작 칸도 카운트
        queue.add(new int[]{startR, startC, 1});
        visited[startR][startC] = true;
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int curR = cur[0];
            int curC = cur[1];
            int curDist = cur[2];

            if (curR == N - 1 && curC == M - 1) {
                System.out.println(curDist);
                return;
            }

            for (int d = 0; d < 4; d++) {
                int nextR = curR + dr[d];
                int nextC = curC + dc[d];

                if (nextR >= 0 && nextR < N && nextC >= 0 && nextC < M && maze[nextR][nextC] != 0 && visited[nextR][nextC] != true) {
                    queue.add(new int[]{nextR, nextC, curDist + 1});
                    visited[nextR][nextC] = true;
                }
            }
        }
    }
}
