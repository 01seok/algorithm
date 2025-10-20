import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int R, C;
    static char[][] map;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        map = new char[R][C];
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                map[i][j] = line.charAt(j);
            }
        }

        int maxDistance = 0; // 모든 bfs 결과 중 최대값

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                // 육지라면 해당 위치 시작점으로 bfs 실행
                if (map[i][j] == 'L') {
                    maxDistance = Math.max(maxDistance, bfs(i, j));
                }
            }
        }
        System.out.println(maxDistance);
    }

    public static int bfs(int startR, int startC) {
        // 매번 bfs할 때마다 visited 배열이랑 queue 초기화 되어야함
        boolean[][] visited = new boolean[R][C];
        Queue<int[]> queue = new LinkedList<>();

        // 이번 bfs에서 가장 먼 거리 저장할 변수
        int maxDistanceThisBfs = 0;

        // 시작점 추가, 거리 0
        queue.add(new int[]{startR, startC, 0});
        visited[startR][startC] = true;

        while (!queue.isEmpty()) {
            int [] cur = queue.poll();
            int r = cur[0];
            int c = cur[1];
            int distance = cur[2];

            // 큐에서 꺼낼 떄 마다 현재 거리가 이번 bfs의 최대 거리인지 확인
            maxDistanceThisBfs = Math.max(maxDistanceThisBfs, distance);

            for (int d = 0; d < 4; d++) {
                int nextR = r + dr[d];
                int nextC = c + dc[d];

                if (nextR >= 0 && nextR < R && nextC >= 0 && nextC < C) {
                    if (!visited[nextR][nextC] && map[nextR][nextC] == 'L') {
                        visited[nextR][nextC] = true;
                        queue.add(new int[]{nextR, nextC, distance + 1});
                    }
                }
            }
        }
        return maxDistanceThisBfs;
    }
}
