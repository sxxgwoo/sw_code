#include <stdio.h>
#include <stdlib.h>
#include "ListBaseStack.h"

void StackInit(Stack * pstack)
{
    pstack->head = NULL; // 스택의 최상단 노드를 NULL로 초기화
}

int SIsEmpty(Stack * pstack)
{
    if(pstack->head == NULL) // 스택이 비어있는지 확인
        return TRUE;
    else
        return FALSE; // 스택이 비어있지 않으면 FALSE 반환
}

void SPush(Stack * pstack, Data data)
{
    Node * newNode = (Node*)malloc(sizeof(Node)); // 새로운 노드 생성

    newNode->data = data; // 새로운 노드에 데이터 저장
    newNode->next = pstack->head; // 새로운 노드가 최근에 추가된 노드를 가리키게 함

    pstack->head = newNode; // 새로운 노드를 스택의 최상단 노드로 설정
}

Data SPop(Stack * pstack)
{
    Data rdata;
    Node * rnode;

    if(SIsEmpty(pstack))
    {
        printf("Stack Memory Error!");
        exit(-1);
    }
    
    rdata = pstack->head->data; // 삭제할 노드의 데이터를 임시로 저장
    rnode = pstack->head; // 삭제할 노드의 주소를 임시로 저장

    pstack->head = pstack->head->next; // 삭제할 노드의 다음 노드를 최상단 노드로 설정
    free(rnode); // 삭제할 노드의 메모리 해제

    return rdata; // 삭제한 노드의 데이터 반환
}

Data SPeek(Stack * pstack)
{
    if(SIsEmpty(pstack))
    {
        printf("Stack Memory Error!");
        exit(-1);
    }

    return pstack->head->data; // 최상단 노드의 데이터 반환
}