import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), cnt = 0;
        for (int i = 0; i < n; i++) {
            String s = sc.next();
            boolean[] v = new boolean[26];
            boolean ok = true;
            for (int j = 0; j < s.length(); j++) {
                int idx = s.charAt(j) - 'a';
                if (v[idx] && s.charAt(j) != s.charAt(j - 1)) {
                    ok = false;
                    break;
                }
                v[idx] = true;
            }
            if (ok) cnt++;
        }
        System.out.println(cnt);
    }
}