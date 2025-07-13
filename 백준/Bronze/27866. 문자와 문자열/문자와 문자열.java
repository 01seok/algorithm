import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String ans = br.readLine();
        int num = Integer.parseInt(br.readLine());
        System.out.print(ans.charAt(num-1));
        br.close();
    }
}