import java.io.*;
import java.util.*;

public class Main {
    static final int mod=1000000007;
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            String s=sc.next();
            long ans=0;
            int i=0;
            while(i<n){
                char curr=s.charAt(i);
                int count=0;
                while(i<n && curr==s.charAt(i)){
                    i++;
                    count++;
                }
                ans=(ans+(long)count*(count+1)/2)%mod;
            }
            System.out.println(ans);
        }
    }
}
