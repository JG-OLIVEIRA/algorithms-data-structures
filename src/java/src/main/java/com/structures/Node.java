package com.structures;

public class Node {

    private String data;
    public Node prev;
    public Node next;

    public Node(String data, Node next){
        this.data = data;
        this.next = next;
    }

    public Node(String data){
        this.data = data;
    }

    public String getData(){
        return data;
    }

    public void setData(String data){
        this.data = data;
    }
}
