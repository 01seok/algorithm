import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());
        System.out.println(A+B-C);

        String AB = String.valueOf(A) + String.valueOf(B);
        int AB_int = Integer.parseInt(AB);
        System.out.println(AB_int-C);

        br.close();
    }
}