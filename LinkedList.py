class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse_list(self):
        # предыдущее значение
        previous = None
        # текущее значение
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def sort_list(self):
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()


# Пример использования:
linked_list = LinkedList()
linked_list.add_element(5)
linked_list.add_element(2)
linked_list.add_element(8)
linked_list.add_element(1)

print("Исходный список:")
linked_list.print_list()
# 5 2 8 1

print("Перевернутый список")
linked_list.reverse_list()
linked_list.print_list()

# 1 8 2 5

print("Отсортированный список:")
linked_list.sort_list()
linked_list.print_list()
# 1 2 5 8
