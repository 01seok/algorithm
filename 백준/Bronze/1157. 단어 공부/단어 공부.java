import java.io.*;
public class Main{
    public static void main(String[] args) throws Exception{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String s=br.readLine().toUpperCase();
        int[] cnt=new int[26];
        for(int i=0;i<s.length();i++){
            char c=s.charAt(i);
            if('A'<=c&&c<='Z') cnt[c-'A']++;
        }
        int max=-1, idx=-1; boolean tie=false;
        for(int i=0;i<26;i++){
            if(cnt[i]>max){max=cnt[i];idx=i;tie=false;}
            else if(cnt[i]==max) tie=true;
        }
        System.out.println(tie?'?':(char)('A'+idx));
    }
}