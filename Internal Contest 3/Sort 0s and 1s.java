import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t!=0){
            int n=sc.nextInt();
            int arr[]=new int[n];
            for(int i=0;i<n;i++){
                arr[i]=sc.nextInt();
            }
            int p1=0;
            int p2=n-1;
            while(p1<p2){
                while(p1<n && arr[p1]==0){
                    p1++;
                }
                while (p2>=0 && arr[p2]==1){
                    p2--;
                }
                if(p1<p2){
                    int temp=arr[p1];
                    arr[p1]=arr[p2];
                    arr[p2]=temp;
                    p2--;
                    p1++;
                }
            }
            for(int i=0;i<n;i++){
                System.out.print(arr[i]+" ");
            }
            System.out.println();
            t--;
        }
    }
}
