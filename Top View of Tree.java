import java.io.*;
import java.util.*;

public class Main {
    public static class Node{
        int data;
        Node left,right;
        Node(int data){
            this.data=data;
        }
    }
    public static class Pair{
        int val;
        Node node;
        Pair(Node node,int val){
            this.val=val;
            this.node=node;
        }
    }
    public static Node insert(Node root,int val){
        if(root==null){ 
            return new Node(val);
        }
        if(val<root.data) root.left=insert(root.left,val);
        else root.right=insert(root.right,val);
        return root;
    }
    public static void topview(Node root){
        Queue<Pair> q=new LinkedList<>();
        if(root==null) return;
        q.add(new Pair(root,0));
        TreeMap<Integer,Integer> hm=new TreeMap<>();
        while(!q.isEmpty()){
            Pair curr=q.remove();
            Node node=curr.node;
            int level=curr.val;
            if(!hm.containsKey(level)){
                hm.put(level,node.data);
            }
            if(node.left!=null) q.add(new Pair(node.left,level-1));
            if(node.right!=null) q.add(new Pair(node.right,level+1));
        }
        for(int i:hm.values()){
            System.out.print(i+" ");
        }
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            Node root=null;
            for(int i=0;i<n;i++){
                int val=sc.nextInt();
                root=insert(root,val);
            }
            topview(root);
            System.out.println();
        }
    }
}
