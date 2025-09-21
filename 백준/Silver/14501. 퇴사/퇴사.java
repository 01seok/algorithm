import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N;
    static int[] T;
    static int[] P;
    static int maxProfit = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        T = new int[N+1];
        P = new int[N+1];

        for (int i = 1; i<=N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine()," ");
            T[i] = Integer.parseInt(st.nextToken());
            P[i] = Integer.parseInt(st.nextToken());
        }

        solve(1, 0);
        System.out.println(maxProfit);
    }

    public static void solve(int day, int profit) {
        // 퇴사일 됐으면 최대 수익 return
        if (day > N) {
            maxProfit = Math.max(maxProfit, profit);
            return;
        }

        // 상담을 한다면 (퇴사일 전에 끝나는 경우만 가능)
        if (day + T[day] -1 <= N) {
            solve(day+T[day], profit + P[day]);
        }

        // 상담 안하면
        solve(day+1, profit);

    }
}
