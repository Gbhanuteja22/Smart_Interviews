import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            int[] arr=new int[n];
            for(int i=0;i<n;i++){
                arr[i]=sc.nextInt();
            }
            int res=0;
            for(int i=0;i<32;i++){
                int count=0;
                for(int j=0;j<n;j++){
                    if(((arr[j])&(1<<i))!=0){
                        count++;
                    }
                }
                if(count%3>0){
                    res|=(1<<i);
                }
            }
            System.out.println(res);
        }
    }
}
