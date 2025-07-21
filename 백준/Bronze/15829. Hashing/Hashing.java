import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int L = Integer.parseInt(br.readLine());
        String s = br.readLine();
        
        long r = 31;
        long M = 1234567891;
        
        long hash = 0;
        long rPower = 1;
        
        for (int i = 0; i < L; i++) {
            char ch = s.charAt(i);
            long charValue = (long)(ch - 'a' + 1);
            long term = (charValue * rPower) % M;
            hash = (hash + term) % M;
            rPower = (rPower * r) % M;
        }
        System.out.println(hash);
        br.close();
    }
}