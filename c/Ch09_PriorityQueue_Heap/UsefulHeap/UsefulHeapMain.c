#include <stdio.h>
#include "UsefulHeap.h"

// 우선순위 비교 함수 정의
int DataPriorityComp(char ch1, char ch2)
{	
	// 아스키 코드는 A<B이다.
	// A가 우선순위 가장 높다고 할 경우
	return ch2 - ch1;

	// A가 우선순위 가장 낮다고 할 경우
	// return ch1 - ch2;
}

int main(void)
{
	Heap heap;

	// 힙 초기화 + 우선순위 비교 함수 등록
	HeapInit(&heap, DataPriorityComp);

	// 첫 번째 데이터 삽입
	HInsert(&heap, 'A'); 
	HInsert(&heap, 'B'); 
	HInsert(&heap, 'C'); 

	printf("%c \n", HDelete(&heap));

	// 두 번째 데이터 삽입
	HInsert(&heap, 'A');
	HInsert(&heap, 'B');
	HInsert(&heap, 'C');

	printf("%c \n", HDelete(&heap));

	while (!HIsEmpty(&heap))
		printf("%c \n", HDelete(&heap));

	return 0;
}