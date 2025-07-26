#include <stdio.h>
#include <stdlib.h>
#include "CircularQueue.h"

void QueueInit(Queue * pq)  // 텅 빈 경우 front와 rear가 같은 위치를 가리킴
{
    pq->front = 0;
    pq->rear = 0;
}

int QIsEmpty(Queue * pq)  // 큐가 비어있는지 확인
{
    if(pq->front == pq->rear)   // 큐가 비어있는 경우
        return TRUE;
    else
        return FALSE;
}

int NextPosIdx(int pos)  // 다음 인덱스 반환
{
    if(pos == QUEUE_LEN - 1)  // 마지막 인덱스인 경우 0으로 변경
        return 0;
    else
        return pos + 1;  // 다음 인덱스 반환
}

void Enqueue(Queue * pq, Data data)  // 데이터 추가
{
    if(NextPosIdx(pq->rear) == pq->front)  // 큐가 꽉 차있는 경우
    {
        printf("Queue Memory Error!");
        exit(-1);
    }

    pq->rear = NextPosIdx(pq->rear);  // rear을 한 칸 이동
    pq->queArr[pq->rear] = data;  // rear가 가리키는 공간에 데이터 저장
}

Data Dequeue(Queue * pq)  // 데이터 삭제
{
    if(QIsEmpty(pq))
    {
        printf("Queue Memory Error!");
        exit(-1);
    }

    pq->front = NextPosIdx(pq->front);  // front을 한 칸 이동
    return pq->queArr[pq->front];  // front가 가리키는 공간에 저장된 데이터 반환
}

Data QPeek(Queue * pq)  // 데이터 확인
{
    if(QIsEmpty(pq))
    {
        printf("Queue Memory Error!");
        exit(-1);
    }

    return pq->queArr[NextPosIdx(pq->front)];  // front가 가리키는 공간에 저장된 데이터 반환
}
