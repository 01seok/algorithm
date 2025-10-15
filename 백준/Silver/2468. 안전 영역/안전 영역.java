import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static int[][] field;
    static boolean[][] visited;

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        field = new int[N][N];
        int maxHeight = 0; // 지역의 최대 높이

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                field[i][j] = Integer.parseInt(st.nextToken());
                if (field[i][j] > maxHeight) {
                    maxHeight = field[i][j];
                }
            }
        }

        int maxSafeZones = 0; // 최대 안전 영역의 개수

        // 최대 높이까지 모두 시뮬레이션
        for (int h = 0; h < maxHeight; h++) {
            visited = new boolean[N][N]; // 매 높이마다 방문 배열 초기화
            int currentSafeZones = 0;    // 현재 높이에서의 안전 영역 개수

            // 2차원 배열을 순회하며 안전 영역 찾기
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    // 물에 잠기지 않았고, 아직 방문하지 않은 새로운 안전 영역을 찾으면
                    if (field[i][j] > h && !visited[i][j]) {
                        currentSafeZones++; // 개수 증가
                        dfs(i, j, h);       // 연결된 모든 영역을 방문 처리
                    }
                }
            }
            // 현재 높이에서의 안전 영역 개수와 전체 최댓값 비교
            maxSafeZones = Math.max(maxSafeZones, currentSafeZones);
        }

        // 아무 지역도 물에 잠기지 않는 경우, 안전 영역은 1개
        if (maxSafeZones == 0) {
            System.out.println(1);
        } else {
            System.out.println(maxSafeZones);
        }
    }

    public static void dfs(int r, int c, int height) {
        visited[r][c] = true;

        for (int d = 0; d < 4; d++) {
            int nextR = r + dr[d];
            int nextC = c + dc[d];

            // 다음 위치가 지도 범위 안에 있고,
            if (nextR >= 0 && nextR < N && nextC >= 0 && nextC < N) {
                // 아직 방문하지 않았으며, 물에 잠기지 않았다면
                if (!visited[nextR][nextC] && field[nextR][nextC] > height) {
                    dfs(nextR, nextC, height); // 재귀
                }
            }
        }
    }
}