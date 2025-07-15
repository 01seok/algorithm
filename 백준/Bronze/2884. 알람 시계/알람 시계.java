import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int totalMin = 60 * H + M;
        int alarmMin = totalMin - 45;
        
        // 밤 12시의 경우 음수가 나옴
        if (alarmMin < 0) {
            alarmMin += (24*60);    // 하루 추가한 분
        }
        int ansH = alarmMin / 60;
        int ansM = alarmMin % 60;
        System.out.println(ansH + " " + ansM);
        br.close();
    }
}