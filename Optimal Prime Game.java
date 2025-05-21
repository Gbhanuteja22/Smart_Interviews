import java.io.*;
import java.util.*;

public class Main {
    public static boolean[] sieve(int n){
        boolean[] isprime=new boolean[n+1];
        Arrays.fill(isprime,true);
        isprime[0]=isprime[1]=false;
        for(int i=2;i*i<=n;i++){
            if(isprime[i]){
                for(int j=i*i;j<=n;j+=i){
                    isprime[j]=false;
                }
            }
        }
        return isprime;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        int maxn=10000;
        boolean[] isprime=sieve(maxn);
        String[] winner=new String[maxn+1];
        winner[0]="Second";
        winner[1]="Second";
        for(int n=2;n<=maxn;n++){
            boolean res=false;
            for(int j=2;j<=n;j++){
                if(isprime[j] && n-j>=0 && winner[n-j].equals("Second")){
                    res=true;
                    break;
                }
            }
            if (res){
                winner[n]="First";
            }else{
                winner[n]="Second";
            }
        }
        while(t-->0){
            int n=sc.nextInt();
            System.out.println(winner[n]);
        }
    }
}
