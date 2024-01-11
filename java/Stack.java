package java;

class Node{
    int data;
    Node prev;

    Node(int d){
        data = d;
        prev = null;
    }
}

class Stack{
    Node head;
    Stack(Node h){
        head = h;
    }

    private int peek(){
        return this.head.data;
    }

    private int push(Node item){
        Node new_node = new Node(item.data);
        if(this.head != null){
            new_node.prev = this.head;
            this.head = new_node;
            return this.head.data;
        }
        this.head = new_node;
        return this.head.data;
    }

    private int pop(){
        if(this.head != null){
            Node head = new Node(this.head.data);
            this.head = head.prev;
            return head.data;
        }
        return -1;
    }
}