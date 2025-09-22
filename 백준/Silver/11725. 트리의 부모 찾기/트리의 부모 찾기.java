import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // 인접 리스트 생성
        ArrayList<Integer>[] list = new ArrayList[N+1];
        for (int i = 1; i <= N; i++) {
            list[i] = new ArrayList<>();
        }

        // 간선 정보 (간선 = 노드 갯수 -1)
        for (int i = 0; i < N-1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            list[a].add(b); // 양방향
            list[b].add(a);
        }

        // 부모 노드 저장 배열 및 BFS 준비
        // 각 노드의 부모 기록할 parent 배열
        int[] parent = new int[N+1];
        Queue<Integer> queue = new LinkedList<>();

        queue.add(1);
        parent[1] = 1; // 루트 노드 방문 처리

        while (!queue.isEmpty()) {
            int now = queue.poll();

            for (int next : list[now]) {
                if (parent[next] == 0) {
                    parent[next] = now; // 아직 방문하지 않았는데 인접 리스트에 있다면 다음에 나오는 숫자의 부모는 now
                    queue.add(next);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 2; i <= N; i++) {
            sb.append(parent[i]).append('\n');
        }
        System.out.println(sb);
    }
}
