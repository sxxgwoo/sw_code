#ifndef __C_QUEUE_H__
#define __C_QUEUE_H__

#define TRUE    1
#define FALSE   0

#define QUEUE_LEN    100

typedef int Data;

typedef struct _cQueue
{
    int front;  // 책에서 F라 표현했던 멤버
    int rear;   // 책에서 R이라 표현했던 멤버
    Data queArr[QUEUE_LEN];
} CQueue;

typedef CQueue Queue;

void QueueInit(Queue * pq);  // 큐 초기화
int QIsEmpty(Queue * pq);  // 큐가 비어있는지 확인

void Enqueue(Queue * pq, Data data);  // 큐에 데이터 추가
Data Dequeue(Queue * pq);  // 큐에서 데이터 삭제
Data QPeek(Queue * pq);  // 큐에서 데이터 확인

#endif