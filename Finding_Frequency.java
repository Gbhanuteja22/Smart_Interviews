import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        Map<Integer,Integer>count=new TreeMap<>();
        for(int i=0;i<n;i++){
            count.put(arr[i],count.getOrDefault(arr[i],0)+1);
        }
        int t=sc.nextInt();
        for (int i=0;i<t;i++){
            int k=sc.nextInt();
            if(count.containsKey(k)){
                System.out.println(count.get(k));
            }else{
                System.out.println(0);
            }
        }
    }
}
