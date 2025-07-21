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
            String N = br.readLine();
            if (N.equals("0")) {
                break;
            }
            boolean isPalindrome = true;
            int length = N.length();
            
            for (int i=0; i<length/2; i++) {
                if (N.charAt(i) != N.charAt(length - 1 - i)) {
                    isPalindrome = false;
                    break;
                }
            }
            if (isPalindrome) {
                sb.append("yes\n");
            } else{
                sb.append("no\n");
            }
        }
        System.out.print(sb.toString());
        br.close();
    }
}