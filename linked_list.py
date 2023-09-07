# https://www.youtube.com/watch?v=KOCm7uZPeYw&t=2s&ab_channel=%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D1%8B


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0

        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range")
            return
        
        new_node.next = current.next
        current.next = new_node

    def remove(self, target):
        if not self.head:
            return  # List is empty, nothing to remove

        if self.head.data == target:
            self.head = self.head.next
            return  # Target was the head of the list

        current = self.head
        while current.next:
            if current.next.data == target:
                current.next = current.next.next
                return  # Target found and removed
            current = current.next

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next  # Store the next node temporarily
            current.next = prev  # Reverse the pointer
            prev = current  # Move prev to the current node
            current = next_node  # Move current to the next node

        self.head = prev  # Update the head to the last node


    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

ll.display()  # Output: 1 -> 2 -> 3 -> None

ll.remove(2)
print("\nLinked list after removing 2:")
ll.display()  # Output: 1 -> 3 -> None


ll.insert(4, 1)  # Insert 4 at position 1
print("\nLinked list after inserting 4 at position 1:")
ll.display()  # Output: 1 -> 4 -> 3 -> None

ll.reverse()
print("\nLinked list after reversal:")
ll.display()  # Output: 3 -> 2 -> 1 -> None