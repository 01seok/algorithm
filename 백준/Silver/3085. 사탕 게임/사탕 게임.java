import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;
    static char[][] board;
    static int answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        board = new char[N][N];

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < N; j++) {
                board[i][j] = str.charAt(j);
            }
        }

        // 모든 칸에 대해서 오른쪽, 아래쪽만 교환
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {

                if (j + 1 < N) {
                    swap(i, j, i, j + 1);
                    answer = Math.max(answer, check());
                    swap(i, j, i, j + 1);
                }

                if (i + 1 < N) {
                    swap(i, j, i + 1, j);
                    answer = Math.max(answer, check());
                    swap(i, j, i + 1, j);
                }
            }
        }

        System.out.println(answer);
    }

    static void swap(int x1, int y1, int x2, int y2) {
        char temp = board[x1][y1];
        board[x1][y1] = board[x2][y2];
        board[x2][y2] = temp;
    }

    static int check() {
        int max = 1;

        // 행 검사
        for (int i = 0; i < N; i++) {
            int cnt = 1;
            for (int j = 1; j < N; j++) {
                if (board[i][j] == board[i][j - 1]) {
                    cnt++;
                } else {
                    cnt = 1;
                }
                max = Math.max(max, cnt);
            }
        }

        // 열 검사
        for (int j = 0; j < N; j++) {
            int cnt = 1;
            for (int i = 1; i < N; i++) {
                if (board[i][j] == board[i - 1][j]) {
                    cnt++;
                } else {
                    cnt = 1;
                }
                max = Math.max(max, cnt);
            }
        }

        return max;
    }
}