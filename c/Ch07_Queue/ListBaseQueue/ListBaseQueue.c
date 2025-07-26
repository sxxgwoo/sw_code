#include <stdio.h>
#include <stdlib.h>
#include "ListBaseQueue.h"

void QueueInit(Queue * pq)
{
    pq->front = NULL;
    pq->rear = NULL;
}

int QIsEmpty(Queue * pq)
{
    if(pq->front == NULL)   // F에 NULL이 들어가 있으면 큐가 비어있음
        return TRUE;
    else
        return FALSE;
}

void Enqueue(Queue * pq, Data data)
{
    Node * newNode = (Node*)malloc(sizeof(Node));
    newNode->next = NULL;
    newNode->data = data;

    if(QIsEmpty(pq))  // 첫 번째 노드를 추가하는 경우
    {
        pq->front = newNode;  // F가 새로운 노드를 가리킴
        pq->rear = newNode;   // R이 새로운 노드를 가리킴
    }
    else    // 두 번째 이후 노드를 추가하는 경우
    {
        pq->rear->next = newNode;  // 마지막 노드가 새로운 노드를 가리킴
        pq->rear = newNode;        // R이 새로운 노드를 가리킴
    }
}

Data Dequeue(Queue * pq)
{
    Node * delNode;
    Data retData;

    if(QIsEmpty(pq))
    {
        printf("Queue Memory Error!");
        exit(-1);
    }
    
    delNode = pq->front;    // 삭제할 노드의 주소를 저장
    retData = delNode->data;    // 삭제할 노드의 데이터를 저장
    pq->front = pq->front->next;    // F가 다음 노드를 가리킴

    free(delNode);  // 삭제할 노드의 메모리 해제
    return retData;  // 삭제한 노드의 데이터를 반환
}

Data QPeek(Queue * pq)
{
    if(QIsEmpty(pq))
    {
        printf("Queue Memory Error!");
        exit(-1);
    }

    return pq->front->data;  // F가 가리키는 노드의 데이터를 반환
}