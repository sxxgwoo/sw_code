#include <stdio.h>
#include <stdlib.h>
#include "Deque.h"

void DequeInit(Deque * pdeq)
{
    pdeq->head = NULL;
    pdeq->tail = NULL;
}

int DQIsEmpty(Deque * pdeq)
{
    if(pdeq->head == NULL)
        return TRUE;
    else
        return FALSE;
}

void DQAddFirst(Deque * pdeq, Data data)
{
    Node * newNode = (Node*)malloc(sizeof(Node));   // 새로운 노드 생성
    newNode->data = data;  // 새로운 노드에 데이터 저장

    newNode->next = pdeq->head;  // 새로운 노드의 다음 노드에 기존 머리 노드의 주소 저장

    if(DQIsEmpty(pdeq))
        pdeq->tail = newNode;  // 덱이 비어있으면 새로운 노드를 꼬리 노드로 설정
    else
        pdeq->head->prev = newNode;  // 덱이 비어있지 않으면 기존 머리 노드의 이전 노드에 새로운 노드의 주소 저장

    newNode->prev = NULL;   // 새로운 노드의 이전 노드는 NULL
    pdeq->head = newNode;   // 새로운 노드를 머리 노드로 설정
}

void DQAddLast(Deque * pdeq, Data data)
{
    Node * newNode = (Node*)malloc(sizeof(Node));   // 새로운 노드 생성
    newNode->data = data;  // 새로운 노드에 데이터 저장

    newNode->prev = pdeq->tail;  // 새로운 노드의 이전 노드에 기존 꼬리 노드의 주소 저장

    if(DQIsEmpty(pdeq))
        pdeq->head = newNode;  // 덱이 비어있으면 새로운 노드를 머리 노드로 설정
    else
        pdeq->tail->next = newNode;  // 덱이 비어있지 않으면 기존 꼬리 노드의 다음 노드에 새로운 노드의 주소 저장

    newNode->next = NULL;   // 새로운 노드의 다음 노드는 NULL
    pdeq->tail = newNode;   // 새로운 노드를 꼬리 노드로 설정
}

Data DQRemoveFirst(Deque * pdeq)
{
    Node * rnode = pdeq->head;  // 삭제할 노드의 주소를 저장
    Data rdata;

    if(DQIsEmpty(pdeq))
    {
        printf("Deque Memory Error!");
        exit(-1);
    }

    rdata = pdeq->head->data;  // 삭제할 노드의 데이터를 저장

    pdeq->head = pdeq->head->next;  // 머리 노드를 다음 노드로 이동
    free(rnode);  // 삭제할 노드의 메모리 해제

    if(pdeq->head == NULL)
        pdeq->tail = NULL;  // 덱이 비어있으면 꼬리 노드를 NULL로 설정
    else
        pdeq->head->prev = NULL;  // 덱이 비어있지 않으면 머리 노드의 이전 노드를 NULL로 설정

    return rdata;
}

Data DQRemoveLast(Deque * pdeq)
{
    Node * rnode = pdeq->tail;
    Data rdata;

    if(DQIsEmpty(pdeq))
    {
        printf("Deque Memory Error!");
        exit(-1);
    }

    rdata = pdeq->tail->data;  // 삭제할 노드의 데이터를 저장

    pdeq->tail = pdeq->tail->prev;  // 꼬리 노드를 이전 노드로 이동
    free(rnode);

    if(pdeq->tail == NULL)
        pdeq->head = NULL;  // 덱이 비어있으면 머리 노드를 NULL로 설정
    else
        pdeq->tail->next = NULL;  // 덱이 비어있지 않으면 꼬리 노드의 다음 노드를 NULL로 설정

    return rdata;
}

Data DQGetFirst(Deque * pdeq)
{
    if(DQIsEmpty(pdeq))
    {
        printf("Deque Memory Error!");
        exit(-1);
    }

    return pdeq->head->data;
}

Data DQGetLast(Deque * pdeq)
{
    if(DQIsEmpty(pdeq))
    {
        printf("Deque Memory Error!");
        exit(-1);
    }

    return pdeq->tail->data;
}