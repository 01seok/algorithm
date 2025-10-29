import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

    // 좌표 저장하기 위한 class
    class Pos {
        int r;
        int c;

        Pos(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

public class Main {

    static int N, M;
    static List<Pos> houses = new ArrayList<>(); // 집 좌표 리스트
    static List<Pos> chickenShops = new ArrayList<>(); // 치킨 집 좌표 리스트
    static Pos[] selectChickens; // M개 조합 치킨집 임시 저장 배열
    static int minTotal = Integer.MAX_VALUE; // 정답 (도시의 최소 치킨 거리 값)

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        // M개 치킨집 조합 저장 배열 초기화 해주기
        selectChickens = new Pos[M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int locationData = Integer.parseInt(st.nextToken());
                if (locationData == 1) {
                    houses.add(new Pos(i, j));
                } else if (locationData == 2) {
                    chickenShops.add(new Pos(i, j));
                }
            }
        }

        dfs(0, 0);
        System.out.println(minTotal);
    }

    // 조합 시작할 치킨집들 리스트 인덱스와 현재까지 고른 치킨집 수
    public static void dfs(int startIdx, int cnt) {
        if (cnt == M) {
            solve();
            return;
        }

        for (int i = startIdx; i < chickenShops.size(); i++) {
            selectChickens[cnt] = chickenShops.get(i);
            dfs(i + 1, cnt + 1);
        }
    }

    // 치킨거리 계산 함수
    public static void solve() {
        int totalDist = 0;

        for (Pos house : houses) {
            int minHouseDist = Integer.MAX_VALUE; // 이 집의 최소 치킨 거리 초기화
            for (Pos shop : selectChickens) {
                int dist = Math.abs(house.r - shop.r) + Math.abs(house.c - shop.c);
                minHouseDist = Math.min(minHouseDist, dist); // 가까운 치킨집 찾기
            }

            totalDist += minHouseDist;
        }

        minTotal = Math.min(minTotal, totalDist);
    }
}
