import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, K;
    static int[] time = new int[100001];
    static int[] count =  new int[100001];
    static final int MAX_SIZE = 100000;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        // 시작점과 도착점이 같을 시
        if (N == K) {
            System.out.println(0);
            System.out.println(1);
            return;
        }

        // 시작점이 도착점보다 뒤에 있을 때
        if (N > K) {
            System.out.println(N-K);
            System.out.println(1);
            return;
        }

        // 시간 배열 채우고(visited 역할) 출발 세팅
        Arrays.fill(time, -1);

        Queue<Integer> queue = new LinkedList<>();
        queue.add(N);
        time[N] = 0;
        count[N] = 1;

        while (!queue.isEmpty()) {
            int cur = queue.poll();

            int[] nextPos = {cur -1, cur + 1, cur * 2};

            for (int next : nextPos) {
                // 유효성 검사
                if (next < 0 || next > MAX_SIZE) {
                    continue;
                }

                // 처음 방문이라면
                if (time[next] == -1) {
                    time[next] = time[cur] + 1;
                    count[next] = count[cur];
                    queue.add(next);
                }

                // 최단 시간이 같은 경우
                else if (time[next] == time[cur] + 1) {
                    count[next] += count[cur];
                }
            }
        }
        System.out.println(time[K]);
        System.out.println(count[K]);
    }
}
