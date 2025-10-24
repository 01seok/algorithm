import java.io.*;
public class Main {
    static int f(int n) {
        return n < 2 ? n : f(n - 1) + f(n - 2);
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        System.out.println(f(n));
    }
}