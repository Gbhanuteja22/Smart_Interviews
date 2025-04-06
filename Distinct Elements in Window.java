import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            int k=sc.nextInt();
            int[] arr=new int[n];
            for(int i=0;i<n;i++){
                arr[i]=sc.nextInt();
            }
            List<Integer> res=new ArrayList<>();
            Map<Integer,Integer> freq=new HashMap<>();
            for(int i=0;i<k;i++){
                freq.put(arr[i],freq.getOrDefault(arr[i],0)+1);
            }
            res.add(freq.size());
            for(int i=k;i<n;i++){
                int out=arr[i-k];
                freq.put(out,freq.get(out)-1);
                if(freq.get(out)==0){
                    freq.remove(out);
                }
                int in=arr[i];
                freq.put(in,freq.getOrDefault(in,0)+1);
                res.add(freq.size());
            }
            for(int i=0;i<res.size();i++){
                System.out.print(res.get(i)+" ");
            }
            System.out.println();
        }
    }
}
