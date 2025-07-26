import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.NoSuchElementException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] inputs = new String[3];
        int targetNum = 0;  // 입력 다음에 올 숫자

        for (int i = 0; i < 3; i++) {
            inputs[i] = br.readLine();
        }
        for (int i = 0; i < 3; i++) {
            try {
                // 문자열을 숫자로 변환 시도
                int num = Integer.parseInt(inputs[i]);
            targetNum = num + (3-i);
            break;
            } catch (NumberFormatException e) {
                // 숫자 아니면 다음 입력 확인하기
                continue;
            }
        }
    if (targetNum % 3== 0 && targetNum % 5 == 0) {
        System.out.println("FizzBuzz");
    } else if (targetNum % 3 == 0) {
        System.out.println("Fizz");
    } else if (targetNum % 5 == 0) {
        System.out.println("Buzz");        
    } else {
        System.out.println(targetNum);
    }
    }
}


