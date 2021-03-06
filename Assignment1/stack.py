class node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def push(head, data):
    new_node = node(data, head)
    head = new_node
    return head

def pop(head):
    if head is None:
        return None
    data = head.data
    head = head.next
    return data, head

def traverse(head):
    while head is not None:
        print(head.data)
        head = head.next

head = node(1, None)
head = push(head, 2)
head = push(head, 3) 
head = push(head, 4) 
data, head = pop(head) 
traverse(head) 