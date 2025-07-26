#ifndef __LB_QUEUE_H__
#define __LB_QUEUE_H__

#define TRUE    1
#define FALSE   0

typedef int Data;

typedef struct _node
{
    Data data;
    struct _node * next;
} Node;

typedef struct _lQueue
{
    Node * front;
    Node * rear;
} LQueue;

typedef LQueue Queue;

void QueueInit(Queue * pq);  // 큐 초기화
int QIsEmpty(Queue * pq);  // 큐가 비어있는지 확인

void Enqueue(Queue * pq, Data data);  // 데이터 추가
Data Dequeue(Queue * pq);  // 데이터 삭제
Data QPeek(Queue * pq);  // 데이터 확인

#endif