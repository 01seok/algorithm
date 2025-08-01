import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        int[] baskets = new int[n];
        
        for (int a = 0; a < m; a++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            
            for (int b = i - 1; b < j; b++) {
                baskets[b] = k;
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for (int ball : baskets) {
            sb.append(ball).append(" ");
        }
        
        System.out.println(sb.toString().trim());
        
        br.close();
    }
}