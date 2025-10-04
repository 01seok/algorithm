import java.io.*;
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String[] arr=new String[5];
        for(int i=0;i<5;i++) arr[i]=br.readLine();
        StringBuilder sb=new StringBuilder();
        int max=0;
        for(String s:arr) if(s.length()>max) max=s.length();
        for(int c=0;c<max;c++){
            for(int r=0;r<5;r++){
                if(c<arr[r].length()) sb.append(arr[r].charAt(c));
            }
        }
        System.out.println(sb);
    }
}