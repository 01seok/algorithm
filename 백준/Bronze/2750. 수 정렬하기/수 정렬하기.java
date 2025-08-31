import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine().trim());
        int[] a=new int[n];
        for(int i=0;i<n;i++) a[i]=Integer.parseInt(br.readLine().trim());
        Arrays.sort(a);
        StringBuilder sb=new StringBuilder();
        for(int v:a) sb.append(v).append('\n');
        System.out.print(sb.toString());
    }
}