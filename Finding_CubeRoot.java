import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            long n=sc.nextLong();
            int flag=0;
            if (n<0){
                n=-1*(n);
                flag=1;
            }
            long i=0,j=1000000;
            long ans=0;
            while(i<=j){
                long mid=i+(j-i)/2;
                long midcubed=mid*mid*mid;
                if(midcubed==n){
                    ans=mid;
                    break;
                }else if(midcubed>n){
                    j=mid-1;
                }else{
                    i=mid+1;
                }
            }
            if(flag==1){
                System.out.println("-"+ans);
            }else{
                System.out.println(ans);
            }
        }
    }
}
