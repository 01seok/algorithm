import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 초기 자본
        int startCash = Integer.parseInt(br.readLine());

        // 14일 주가
        int[] prices = new int[14];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 14; i++) {
            prices[i] = Integer.parseInt(st.nextToken());
        }

        // 준현
        int joonhyeonCash = startCash;
        int joonhyeonPrice = 0; // 준현이 주식 수

        for (int price : prices) {
            // 현금으로 주식 살 수 있으면 전량 매수
            if (joonhyeonCash >= price) {
                joonhyeonPrice += joonhyeonCash / price;
                joonhyeonCash %= price; // 남은 현금
            }
        }

        // 준현이 최종 자산 계산 (현금 + 보유주식 수 * 마지막 날 주가)
        int joonhyeonTotal = joonhyeonCash + (joonhyeonPrice * prices[13]);

        // 성민
        int seongminCash = startCash;
        int seongminPrice = 0; // 성민이 주식 수
        int upCount = 0; // 상승 횟수
        int downCount = 0;

        // 전일 대비 비교 위해 인덱스 1부터
        for (int i = 1; i <14; i++) {
            // 주가 변동 추세 파악
            if (prices[i] > prices[i - 1]) {
                upCount++;
                downCount = 0;
            } else if (prices[i] < prices[i - 1]) {
                downCount++;
                upCount = 0;
            } else {
                // 전일과 동일하면 둘다 초기화
                upCount = 0;
                downCount = 0;
            }

            // 3일 연속 상승하면 매도
            if (upCount >= 3) {
                if (seongminPrice > 0) {
                    seongminCash += seongminPrice * prices[i];
                    seongminPrice = 0;
                }
            }

            // 3일 연속 하락하면 매수
            if (downCount >= 3) {
                if (seongminCash >= prices[i]) {
                    seongminPrice += seongminCash / prices[i];
                    seongminCash %= prices[i];
                }
            }
        }

        // 성민이 최종
        int seongminTotal = seongminCash + (seongminPrice * prices[13]);

        // 결과 비교
        if (joonhyeonTotal > seongminTotal) {
            System.out.println("BNP");
        } else if (joonhyeonTotal < seongminTotal) {
            System.out.println("TIMING");
        } else {
            System.out.println("SAMESAME");
        }
    }
}
