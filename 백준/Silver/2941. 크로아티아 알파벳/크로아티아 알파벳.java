import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        String[] arr={"c=","c-","dz=","d-","lj","nj","s=","z="};
        for(String t:arr) s=s.replace(t,"*");
        System.out.print(s.length());
    }
}