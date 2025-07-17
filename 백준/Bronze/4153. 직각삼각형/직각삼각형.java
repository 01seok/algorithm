import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {

        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        if (a == 0 && b == 0 && c == 0) {
            break;
        }

        int[] sides = {a, b, c};
        Arrays.sort(sides);

        if (sides[0] * sides[0] + sides[1] * sides[1] == sides[2] * sides[2]) {
            sb.append("right").append('\n');
        } else {
            sb.append("wrong").append('\n');
            }
        }
        System.out.print(sb.toString());
        br.close();
    }
}