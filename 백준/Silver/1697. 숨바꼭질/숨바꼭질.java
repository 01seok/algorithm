import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N; // 수빈의 위치
    static int K; // 동생 위치
    static boolean[] visited = new boolean[100001];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        // 수빈이가 동생보다 앞에 있는 경우엔 순간 이동 불가능
        if (N >= K) {
            System.out.println(N - K);
            return;
        }
        bfs();
    }

    static void bfs() {
        Queue<int[]> queue = new LinkedList<>();
        // 큐에 시작 위치와 시작 시간을 배열로 저장
        queue.add(new int[]{N, 0});
        visited[N] = true;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int curPos = cur[0];
            int curTime = cur[1];

            // 동생 위치면 종료
            if (curPos == K) {
                System.out.println(curTime);
                return;
            }

            // 선택지 3개
            int[] nextPos = {curPos -1, curPos + 1, curPos * 2};
            for (int nextPosition : nextPos) {
                if (nextPosition >= 0 && nextPosition <= 100000 && !visited[nextPosition]) {
                    visited[nextPosition] = true;
                    queue.add(new int[]{nextPosition, curTime + 1});
                }
            }
        }
    }
}
