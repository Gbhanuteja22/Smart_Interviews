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
                arr[sc.nextInt()]++;
            }
            for(int i=0;i<n;i++){
                if(arr[i]>=2){
                    System.out.print(i+" ");
                }
            }
            System.out.println();
        }
    }
}
