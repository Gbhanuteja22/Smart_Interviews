import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            int arr[][]=new int[n][n];
            for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){
                    arr[i][j]=sc.nextInt();
                }
            }
            int[] sums=new int[2*n-1];
            for(int j=0;j<n;j++){
                for(int k=0;k<n;k++){
                    int ind=k-j+n-1;
                    sums[ind]+=arr[j][k];
                }
            }
            for(int i=2*n-2;i>=0;i--){
                System.out.print(sums[i]+" ");
            }
            System.out.println();
        }
    }
}