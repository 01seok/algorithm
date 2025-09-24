import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] meetings = new int[N][2];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            meetings[i][0] = Integer.parseInt(st.nextToken()); // 시작 시간
            meetings[i][1] = Integer.parseInt(st.nextToken()); // 종료 시간
        }
        // 종료시간이 빠른 것부터 정렬, 같다면 시작시간이 더 빠른것부터
        Arrays.sort(meetings, (meet1, meet2) -> {
            if(meet1[1] == meet2[1]) {
                return meet1[0] - meet2[0];
            }
            return meet1[1] - meet2[1];
        });

        int cnt = 0; // 진행 가능한 회의
        int meetEndTime = 0;

        for (int[] meeting : meetings) {
            if (meeting[0] >= meetEndTime) {
                cnt++;
                meetEndTime = meeting[1];
            }
        }
        System.out.println(cnt);
    }
}
