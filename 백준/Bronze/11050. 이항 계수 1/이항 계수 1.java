import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {

    public static long factorial(int num) {
        if (num == 0) {
            return 1;
        }
        long reult = 1;
        for (int i = 1; i <= num; i++) {
            reult *= i;
        }
        return reult;
    }


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K  = Integer.parseInt(st.nextToken());

        if (K < 0 || K > N) {
            System.out.println(0);
            return;
            }
        long bigNum = factorial(N);
        long smallNum = factorial(K) * factorial(N - K);
        
        long result = bigNum / smallNum;
        System.out.println(result);
        br.close();
        }
    }


