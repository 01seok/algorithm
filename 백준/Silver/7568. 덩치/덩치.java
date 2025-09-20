import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // 비교 할 사람 수
    int N = Integer.parseInt(br.readLine());

    // 2차원 배열로 N명 몸무게, 키 정보 저장하기 위해 2차원 배열 생성
    int[][] people = new int[N][2];

    for (int i = 0; i < N; i++) {
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        people[i][0] = Integer.parseInt(st.nextToken()); // 몸무게
        people[i][1] = Integer.parseInt(st.nextToken()); // 키
    }

    StringBuilder sb = new StringBuilder();

    // 등수 계산
    for (int i = 0; i < N; i++) {
        int rank = 1; // 각 사람 등수를 1등으로 초기화 해두기

        for (int j = 0; j < N; j++) {

            // 자기 자신 비교 할 필요 없음
            if (i == j) continue;
            
            // i번째 사람보다 j번째 사람이 덩치가 더 클 때
            if (people[i][0] < people[j][0] && people[i][1] < people[j][1]) {
                rank++;
            }
        }
        // 계산된 등수를 sb에 추가
        sb.append(rank).append(" ");
    }
        System.out.println(sb);
    }
}

