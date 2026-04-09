import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] sw = new int[N + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            sw[i] = Integer.parseInt(st.nextToken());
        }

        int students = Integer.parseInt(br.readLine());

        for (int s = 0; s < students; s++) {
            st = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());

            if (gender == 1) {
                for (int i = num; i <= N; i += num) {
                    sw[i] = 1 - sw[i];
                }
            } else {
                sw[num] = 1 - sw[num];

                int left = num - 1;
                int right = num + 1;

                while (left >= 1 && right <= N && sw[left] == sw[right]) {
                    sw[left] = 1 - sw[left];
                    sw[right] = 1 - sw[right];
                    left--;
                    right++;
                }
            }
        }

        for (int i = 1; i <= N; i++) {
            System.out.print(sw[i] + " ");
            if (i % 20 == 0) {
                System.out.println();
            }
        }
    }
}