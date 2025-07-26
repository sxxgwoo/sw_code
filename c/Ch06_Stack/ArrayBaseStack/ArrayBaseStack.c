#include <stdio.h>
#include <stdlib.h>
#include "ArrayBaseStack.h"

void StackInit(Stack * pstack)
{
    pstack->topIndex = -1;  // 스택의 최상단 인덱스를 -1로 초기화
}

int SIsEmpty(Stack * pstack)
{
    if(pstack->topIndex == -1) // 스택이 비어있는지 확인
        return TRUE;
    else
        return FALSE; // 스택이 비어있지 않으면 FALSE 반환
}

void SPush(Stack * pstack, Data data) // push 연산 담당 함수
{
    pstack->topIndex += 1; // 데이터 추가 시 최상단 인덱스 증가
    pstack->stackArr[pstack->topIndex] = data; // 데이터 저장   
}

Data SPop(Stack * pstack) // pop 연산 담당 함수
{
    int rIdx;

    if(SIsEmpty(pstack))
    {
        printf("Stack Memory Error!");
        exit(-1);
    }

    rIdx = pstack->topIndex;    // 삭제할 데이터의 인덱스 저장
    pstack->topIndex -= 1;      // 최상단 인덱스 감소

    return pstack->stackArr[rIdx]; // 삭제한 데이터 반환
}

Data SPeek(Stack * pstack)  // pop을 하면 데이터가 삭제되므로 이를 방지하면서 최상단 데이터를 반환하는 연산 담당 함수
{
    if(SIsEmpty(pstack))
    {
        printf("Stack Memory Error!");
        exit(-1);
    }

    return pstack->stackArr[pstack->topIndex];  // 최상단 데이터 반환
}