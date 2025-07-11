import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int H = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());

            int floor;
            int roomNumber;

            // 층 계산
            if (N % H == 0) {
                floor = H;
                roomNumber = N / H;
            } else {
                floor = N % H;
                roomNumber = (N / H) + 1;
            }

            if (roomNumber < 10) {
                System.out.println(floor +"0" + roomNumber);
            } else {
                System.out.println(floor + "" + roomNumber);
            }

        }
        br.close();

    }
}