import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int[] heights = new int[9];
        int sum = 0;
        
        for (int i = 0; i < 9; i++) {
            heights[i] = Integer.parseInt(br.readLine());
            sum += heights[i];
        }
        
        int spyIndex1 = -1;
        int spyIndex2 = -1;
        
        outerloop:
        for (int i = 0; i < 8; i++) {
            for (int j = i + 1; j < 9; j++) {
                if (sum - (heights[i] + heights[j]) == 100) {
                    spyIndex1 = i;
                    spyIndex2 = j;
                    break outerloop;
                }
            }
        }
        
        for (int i = 0; i < 9; i++) {
            if (i != spyIndex1 && i != spyIndex2) {
                System.out.println(heights[i]);
            }
        }
    }
}
