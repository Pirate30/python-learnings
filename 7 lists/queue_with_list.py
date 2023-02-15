# QUEUE - linear data structue
# storage manner - FIFO
# ops - enqueue , dequeue, front, rear


q=[]

while True:
    op = int(
        input(
            '''
            Choose the queue operation:
            1. Push / enqueue
            2. Pop (first elem) / dequeue
            3. Front
            4. Rear
            5. Display Queue
            6. Exit
            '''
        )
    )

    if op==1:
        n=input('enter an element to push: ')
        q.append(n)
        print('result: ',q)
    elif op==2:
        if len(q)==0:
            print('empty queue. Nothing to pop',q)
        else:
            del q[0]
            print('result: ', q)
    elif op==3:
        if len(q)==0:
            print('empty queue. Nothing to show',q)
        else:
            print('front: ', q[0])
    elif op==4:
        if len(q)==0:
            print('empty queue. Nothing to show',q)
        else:
            print('rear: ', q[-1])
    elif op==5:
        print('displaying the queue: ',q)
    else:
        break