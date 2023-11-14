package java;

class Node {
    Node next;
    int data;

    Node(int d){
        data = d;
    }
    void appendToTail(int d){
        Node new_node = new Node(d);
        Node n = this;
        while(n.next != null){
            n = n.next;
        }
        n.next = new_node;
    }
    
}

Node deleteNode(Node head, int d){
    Node n = head;

    if(n.data == d){
        return head.next;
    }

    while(n.next != null){
        if(n.next.data == d){
            n.next = n.next.next;
            return head;
        }
        n = n.next;
    }
    return head;
}

class LinkedList{
    Node head;

    LinkedList(Node h){
        head = h;
    }
}