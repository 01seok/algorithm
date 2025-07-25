import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        line = line.trim();
        if (line.isEmpty()) {
            System.out.println(0);
        } else {
            String[] words = line.split(" +");
            System.out.println(words.length);
        }
        br.close();
    }
}