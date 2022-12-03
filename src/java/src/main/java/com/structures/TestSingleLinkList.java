package com.structures;

public class TestSingleLinkList {

    private static Node head;
    private static Node tail;

    public static Node init(){

        // the first node called by head node
        head = new Node("A", null);

        Node nodeB = new Node("B", null);
        head.next = nodeB;

        Node nodeC = new Node("C", null);
        nodeB.next = nodeC;

        // the last node called by tail node
        tail = new Node("D", null);
        nodeC.next = tail;

        return head;
    }

    public static void remove(int removePosition){
        Node p = head;
        int i = 0;

        while(p.next != null && i < removePosition - 1){
            p = p.next;
            i++;
        }

        Node temp = p.next;
        p.next = p.next.next;
        temp.next = null;
    }

    public static void print(){
        Node p = head;
        while(p != null)
        {
            System.out.print(p.data + "-> ");
            p = p.next;
        }
        System.out.print("End\n\n");
    }

    public static void main(String[] args){
        init();
        remove(2);
        print();
    }
}
