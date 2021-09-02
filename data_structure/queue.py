queue=[]
size=int(input("enter the size you want: "))
front=0
rear=0
n=0
def insert():
    global front, rear, size, queue
    if rear>=size:
        print("queue is full")
    else:
        p = int(input("enter the element want to insert: "))
        queue.insert(rear, p)
        #insert(position,element)(syntax)
        rear+=1
        for i in range(front, rear):
            print(queue[i])
def delete():
    global front,rear, size, queue
    if rear==front:
        print("queue is empty")
    else:
        front +=1
        for i in range(front, rear):
            print(queue[i])
while n!=1:
    print("enter the operation want to perform")
    opt = int(input("press \n1)enqueue\n2)dequeue"))
    if opt==1:
        insert()
    elif opt==2:
        delete()


