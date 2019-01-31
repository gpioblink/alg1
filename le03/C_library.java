import java.io.*;
import java.util.NoSuchElementException;
import java.util.Scanner;

 public class Main {

     public static void main(String[] args) {
        FastScanner scan = new FastScanner();
        NodeList node = new NodeList();
        int n = scan.nextInt();
        int x;
        char[] query = new char[15];
         for(int i=0; i<n; i++) {
             switch (scan.next()) {
                 case "insert":
                     node.Insert(scan.nextInt());
                     break;
                 case "delete":
                     node.SearchDelete(scan.nextInt());
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

// https://qiita.com/p_shiki37/items/65c18f88f4d24b2c528b
//入力高速化ライブラリ
class FastScanner {
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;
    private boolean hasNextByte() {
        if (ptr < buflen) {
            return true;
        }else{
            ptr = 0;
            try {
                buflen = in.read(buffer);
            } catch (IOException e) {
                e.printStackTrace();
            }
            if (buflen <= 0) {
                return false;
            }
        }
        return true;
    }
    private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
    private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
    private void skipUnprintable() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++;}
    public boolean hasNext() { skipUnprintable(); return hasNextByte();}
    public String next() {
        if (!hasNext()) throw new NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        int b = readByte();
        while(isPrintableChar(b)) {
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }
    public int nextInt() {
        if (!hasNext()) throw new NoSuchElementException();
        int n = 0;
        boolean minus = false;
        int b = readByte();
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        if (b < '0' || '9' < b) {
            throw new NumberFormatException();
        }
        while(true){
            if ('0' <= b && b <= '9') {
                n *= 10;
                n += b - '0';
            }else if(b == -1 || !isPrintableChar(b)){
                return minus ? -n : n;
            }else{
                throw new NumberFormatException();
            }
            b = readByte();
        }
    }
}

