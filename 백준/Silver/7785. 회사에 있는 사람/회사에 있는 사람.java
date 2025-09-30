import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args)throws Exception{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        HashSet<String> set=new HashSet<>();
        for(int i=0;i<n;i++){
            String[] arr=br.readLine().split(" ");
            if(arr[1].equals("enter")) set.add(arr[0]);
            else set.remove(arr[0]);
        }
        ArrayList<String> list=new ArrayList<>(set);
        Collections.sort(list,Collections.reverseOrder());
        StringBuilder sb=new StringBuilder();
        for(String x:list) sb.append(x).append("\n");
        System.out.print(sb);
    }
}