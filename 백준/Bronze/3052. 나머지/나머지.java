import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.NoSuchElementException;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Set<Integer> remains = new HashSet<>();

        for (int i = 0; i < 10; i++) {
            int number = Integer.parseInt(br.readLine());
            int remain = number % 42;
            remains.add(remain);
        }
        System.out.println(remains.size());
        br.close();
    }
}