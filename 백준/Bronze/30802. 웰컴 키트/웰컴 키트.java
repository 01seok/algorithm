import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] sizes = new int[6]; // 티셔츠 사이즈 별 신청자 수 담을 리스트
        for (int i = 0; i < 6; i++) {
            sizes[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        long totalTShirt = 0;   // 필요한 티셔츠 묶음
        for (int i = 0; i < 6; i++) {
            int requiredTShirt = sizes[i];
            if (requiredTShirt % T == 0) {
                totalTShirt += requiredTShirt/T;
            } else {
                totalTShirt += (requiredTShirt/T) + 1; // 한 묶음 더 추가
            }
        }

        long totalPen = N / P; // 필요한 펜 묶음
        long remainPen = N % P; // 필요한 낱개 펜

        System.out.println(totalTShirt);
        System.out.println(totalPen+" "+remainPen);

        br.close();
    }
}