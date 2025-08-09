import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int hour = Integer.parseInt(st.nextToken());
        int minute = Integer.parseInt(st.nextToken());

        int cookTime = Integer.parseInt(br.readLine());

        // 총 분 계산
        int totalMinutes = hour * 60 + minute + cookTime;

        // 시와 분으로 변환
        int resultHour = (totalMinutes / 60) % 24;
        int resultMinute = totalMinutes % 60;

        System.out.println(resultHour + " " + resultMinute);
    }
}
