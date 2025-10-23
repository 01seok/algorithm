import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, K;
    static int[] time = new int[100001];
    static final int MAX_SIZE = 100000;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        // 서로 같은 위치에 있으면 바로 종료
        if (N == K) {
            System.out.println(0);
            return;
        }

        // 수빈이가 더 앞에 있다면 뒤로만 갈 수 있음
        else if (N > K) {
            System.out.println(N - K);
            return;
        }

        // time 배열을 -1로 채워서 visited 배열로 사용하기
        Arrays.fill(time, -1);
        
        // 텔레포트의 소요시간이 0초이므로 queue말고 deque 사용해서 양 끝에서 데이터 넣고 빼기
        Deque<Integer> deque = new LinkedList<>();
        deque.addFirst(N);
        time[N] = 0;

        while (!deque.isEmpty()) {
            int cur = deque.pollFirst();

            if (cur == K) {
                break;
            }
            
            // 시간 0초 걸리는 텔레포트를 우선적으로 탐색
            int teleportPos = cur * 2;
            if (teleportPos >= 0 && teleportPos <= MAX_SIZE && time[teleportPos] == -1) {
                time[teleportPos] = time[cur];
                deque.addFirst(teleportPos);
            }

            int backPos = cur - 1;
            if (backPos >= 0 && backPos <= MAX_SIZE && time[backPos] == -1) {
                time[backPos] = time[cur] + 1;
                deque.addLast(backPos);
            }

            int forwardPos = cur + 1;
            if (forwardPos >= 0 && forwardPos <= MAX_SIZE && time[forwardPos] == -1) {
                time[forwardPos] = time[cur] + 1;
                deque.addLast(forwardPos);
            }
        }
        System.out.println(time[K]);
    }
}
