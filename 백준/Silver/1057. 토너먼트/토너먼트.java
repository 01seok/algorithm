import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int kimNum = Integer.parseInt(st.nextToken());
        int limNum = Integer.parseInt(st.nextToken());

        int round = 0;
        while (kimNum != limNum) {
            kimNum = (kimNum + 1) / 2;
            limNum = (limNum + 1) / 2;

            round++;
        }
        System.out.println(round);
    }
}
