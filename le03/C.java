// WHATIS: 双方向連結リスト

import java.io.*;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        NodeList node = new NodeList();
        int n = Integer.parseInt(scan.next());
        int x;
        char[] query = new char[15];
        for(int i=0; i<n; i++) {
            switch (scan.next()) {
                case "insert":
                    node.Insert(Integer.parseInt(scan.next()));
                    break;
                case "delete":
                    node.SearchDelete(Integer.parseInt(scan.next()));
                    break;
                case "deleteFirst":
                    node.DeleteFirst();
                    break;
                case "deleteLast":
                    node.DeleteLast();
                    break;
            }
        }
        node.Print();
    }

}

class Node{
    int key ;
    Node right;
    Node left;

    Node(int key){
        this.key = key;
    }
}

class NodeList{
    Node head;

    NodeList(){
        this.head = new Node(-1);
        this.head.right = this.head;
        this.head.left = this.head;
    }

    void Insert(int x){
        Node newNode = new Node(x);
        newNode.right = this.head.right;
        newNode.right.left = newNode;
        this.head.right = newNode;
        newNode.left = this.head;
    }

    void Print(){
        PrintWriter out = new PrintWriter(System.out);
        for(Node point = this.head.right; point != this.head.left; point = point.right) {
            out.print(point.key + " ");
        }
        out.println(this.head.left.key);
        out.flush();
    }

    void Delete(Node point){
        point.right.left = point.left;
        point.left.right = point.right;
    }

    void SearchDelete(int x){
        for(Node point = this.head.right; point != this.head; point = point.right) {
            if(point.key == x){this.Delete(point); break;}
        }
    }

    void DeleteFirst(){
        this.Delete(this.head.right);
    }

    void DeleteLast(){
        this.Delete(this.head.left);
    }

}