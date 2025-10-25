import java.io.*;
public class Main {
    static int cnt;
    static int check(String s, int l, int r){
        cnt++;
        if(l>=r) return 1;
        if(s.charAt(l)!=s.charAt(r)) return 0;
        return check(s,l+1,r-1);
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int t=Integer.parseInt(br.readLine().trim());
        StringBuilder sb=new StringBuilder();
        while(t-->0){
            String s=br.readLine().trim();
            cnt=0;
            int res=check(s,0,s.length()-1);
            sb.append(res).append(" ").append(cnt).append("\n");
        }
        System.out.print(sb.toString());
    }
}