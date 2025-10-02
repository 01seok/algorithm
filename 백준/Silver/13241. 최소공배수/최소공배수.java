import java.util.*;
public class Main{
    static long gcd(long a,long b){
        while(b!=0){
            long t=a%b;
            a=b;
            b=t;
        }
        return a;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        long a=sc.nextLong();
        long b=sc.nextLong();
        System.out.println(a*b/gcd(a,b));
    }
}