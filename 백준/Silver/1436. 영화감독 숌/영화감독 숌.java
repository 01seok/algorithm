import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N =  Integer.parseInt(br.readLine());
        
        int cnt = 0;
        int num = 665;  // 666부터 검사하기 위해서
        
        while (cnt < N) {
            num ++;
            if (String.valueOf(num).contains("666")) {
                cnt ++;
            }
        }
        System.out.println(num);
    }
}


