import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String nums = br.readLine();
        int sum = 0;
        for (int i=0; i<nums.length(); i++) {
            sum += Integer.parseInt(String.valueOf(nums.charAt(i)));
        }
        System.out.println(sum);
        br.close();
    }
}