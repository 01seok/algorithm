import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        int time = 0;

        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            if (ch >= 'A' && ch <= 'C') time += 3;
            else if (ch >= 'D' && ch <= 'F') time += 4;
            else if (ch >= 'G' && ch <= 'I') time += 5;
            else if (ch >= 'J' && ch <= 'L') time += 6;
            else if (ch >= 'M' && ch <= 'O') time += 7;
            else if (ch >= 'P' && ch <= 'S') time += 8;
            else if (ch >= 'T' && ch <= 'V') time += 9;
            else if (ch >= 'W' && ch <= 'Z') time += 10;
        }

        System.out.println(time);
    }
}