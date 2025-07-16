import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        int[] first = new int[26];
        Arrays.fill(first, -1);

        for (int i = 0; i < S.length(); i++) {
            char currentChar = S.charAt(i);

            int alphabetIndex = currentChar - 'a'; // a로부터 상대적인 인덱스로 변환하면 0,1,2 ...

            if (first[alphabetIndex] == -1) {
                first[alphabetIndex] = i; // 현재 인덱스 저장
            }
        }

        for (int i = 0; i < 26; i++) {
            System.out.print(first[i] + " ");
        }

        br.close();
    }
}