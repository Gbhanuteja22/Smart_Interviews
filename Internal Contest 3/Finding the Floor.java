import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        int a[]=new int[n];
        for(int i=0;i<n;i++){
            a[i]=s.nextInt();
        }
        Arrays.sort(a);
        int q=s.nextInt();
        for(int i=0;i<q;i++){
            int x=s.nextInt();
            int low=0,high=n-1,res=Integer.MIN_VALUE;
            while(low<=high){
                int mid=(low+high)/2;
                if(a[mid]>x){
                    high=mid-1;
                }
                else{
                    res=a[mid];
                    low=mid+1;
                }
            }
            System.out.println(res);
        }
    }
}
