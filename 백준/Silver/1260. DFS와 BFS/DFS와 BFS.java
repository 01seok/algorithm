import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N, M, V;
    static ArrayList<Integer>[] adj;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        // 인접 리스트 초기화
        adj = new ArrayList[N+1];
        for (int i = 1; i <= N; i++) {
            adj[i] = new ArrayList<>();
        }

        // 간선 정보 입력받아 인접 리스트에 저장
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            adj[a].add(b);
            adj[b].add(a); // 양방향 그래프
        }

        // 정점 번호가 작은 것을 먼저 방문해야하니 정렬
        for (int i = 1; i <= N; i++) {
            Collections.sort(adj[i]);
        }

        // dfs
        visited = new boolean[N+1];
        dfs(V);
        sb.append("\n");

        // bfs
        visited = new boolean[N+1];
        bfs(V);

        System.out.println(sb);

    }

    public static void dfs(int node) {
        visited[node] = true;
        sb.append(node).append(" ");

        for (int nextNode : adj[node]) {
            if (!visited[nextNode]) {
                dfs(nextNode);
            }
        }
    }

    public static void bfs(int start) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int curNode = queue.poll();
            sb.append(curNode).append(" ");

            for (int nextNode : adj[curNode]) {
                if (!visited[nextNode]) {
                    queue.add(nextNode);
                    visited[nextNode] = true;
                }
            }
        }
    }
}
