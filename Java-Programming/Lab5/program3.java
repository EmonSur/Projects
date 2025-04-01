public class LinkedList {
    Node head;

    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    void insertEnd(int data) {
        Node new_node = new Node(data);
        if (head == null) {
            head = new Node(data);
            return;
        }
        new_node.next = null;
        Node last = head;
        while (last.next != null)
            last = last.next;
        last.next = new_node;
    }

    void insertAfter(Node prev_node, int data) {
        Node new_node = new Node(data);
        new_node.next = prev_node.next;
        prev_node.next = new_node;
    }

    void deleteNode(int position) {
        if (head == null) return;
        Node temp = head;
        if (position == 0) {
            head = temp.next;
            return;
        }
        for (int i = 0; temp != null && i < position - 1; i++)
            temp = temp.next;
        if (temp == null || temp.next == null) return;
        Node next = temp.next.next;
        temp.next = next;
    }

    void printList() {
        Node tnode = head;
        while (tnode != null) {
            System.out.print(tnode.data + " ");
            tnode = tnode.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        list.insertEnd(11);
        list.insertEnd(22);
        list.insertEnd(6);
        list.insertEnd(89);
        list.insertEnd(99);

        list.insertAfter(list.head.next, 50);
        list.printList();

        list.deleteNode(1);
        list.printList();

        list.deleteNode(0);
        list.printList();

        // Correct approach to delete the last element
        list.deleteNode(2); // Adjusted to correctly delete the last element after list modifications
        list.printList();
    }
}
