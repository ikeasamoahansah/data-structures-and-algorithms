package java;

class Node{
    int data;

    Node(int d){
        data = d;
    }
}

class Stack{
    Node head;
    Node prev;
    Stack(Node h){
        head = h;
        prev = null;
    }

    private int peek(){
        return this.head.data;
    }

    private int push(Node item){
        Node new_node = new Node(item);
        if(this.head != null){
            new_node.prev = this.head;
            this.head = new_node;
            return this.head.data;
        }
        this.head = new_node;
    }

    private int pop(){

    }
}