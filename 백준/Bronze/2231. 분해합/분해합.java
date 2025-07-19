import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int result = 0; // 생성자를 저장할 변수

        // 1부터 N까지의 모든 숫자를 반복하며 검사
        for (int i = 1; i <= N; i++) {
            int currentNum = i; // 현재 검사할 숫자
            int sumOfDigits = 0; // currentNum의 각 자릿수의 합

            int tempNum = currentNum;
            while (tempNum > 0) {
                sumOfDigits += tempNum % 10; //
                tempNum /= 10;
            }

            int totalSum = currentNum + sumOfDigits;

            // 만약 총합이 N과 같다면, currentNum은 N의 생성자
            if (totalSum == N) {
                result = currentNum;
                break;
            }
        }
        System.out.println(result);
    }
}