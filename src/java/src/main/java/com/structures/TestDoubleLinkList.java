package com.structures;

public class TestDoubleLinkList {

    private static Node head;
    private static Node tail;

    public static void init(){

        // the first node called by head node
        head = new Node("A");

        head.prev = null;
        head.next = null;

        Node nodeB = new Node("B");
        nodeB.prev = head;
        nodeB.next = null;
        head.next = nodeB;

        Node nodeC = new Node("C");
        nodeC.prev = nodeB;
        nodeC.next = null;
        nodeB.next = nodeC;

        // the last node called by tail node
        tail = new Node("D");

        tail.prev = nodeC;
        tail.next = null;
        nodeC.next = tail;

    }

    public static void print(Node node){
        Node p = node;
        Node end = null;
        while(p != null)
        {
            String data = p.getData();
            System.out.print(data + " -> " );
            end = p;
            p = p.next;
        }
        System.out.print("End\n");

        p = end;
        while(p != null)
        {
            String data = p.getData();
            System.out.print(data + " -> ");
            p = p.prev;
        }
        System.out.print("Start\n\n");
    }

    public static void main(String[] args){
        init();
        print(head);
    }
}
