    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    import java.util.ArrayDeque;
    import java.util.Deque;

    public class Main {
        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int K = Integer.parseInt(br.readLine());

            Deque<Integer> stack = new ArrayDeque<>();
            int sum = 0;
            for (int i = 0; i < K; i++) {
                int num = Integer.parseInt(br.readLine());

                if (num == 0) {
                    sum -= stack.pollLast();
                } else {
                    stack.addLast(num);
                    sum += num;
                }
            }
            System.out.println(sum);
        }
    }