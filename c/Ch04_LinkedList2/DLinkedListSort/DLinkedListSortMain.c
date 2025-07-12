#include <stdio.h>
#include "DLinkedList.h"

// 정렬 기준 함수: 오름차순
int WhoIsPrecede(int d1, int d2)
{
	if (d1 < d2)
		return 0;    // d1이 정렬 순서상 앞선다 (자리 그대로 유지)
	else
		return 1;    // d2가 d1보다 작거나 같으면, d2가 먼저 오도록 정렬
}

int main(void)
{
	// 리스트 생성 및 초기화
	List list;
	int data;
	ListInit(&list);  // 내부적으로 더미 헤더 노드 생성

	// 정렬 기준 설정 (오름차순)
	SetSortRule(&list, WhoIsPrecede);

	// 데이터 삽입 (정렬 기준에 따라 자동 정렬됨)
	LInsert(&list, 33);
	LInsert(&list, 11);  
	LInsert(&list, 11);
	LInsert(&list, 22);  
	LInsert(&list, 22);
	

	// 현재 리스트에 저장된 데이터 수 출력
	printf("현재 데이터의 수: %d \n", LCount(&list));

	// 전체 데이터 출력 (앞에서부터 차례대로 순회)
	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		while (LNext(&list, &data))
			printf("%d ", data);
	}
	printf("\n\n");

	// 데이터 값이 22인 노드를 모두 삭제
	if (LFirst(&list, &data))
	{
		if (data == 22)
			LRemove(&list);

		while (LNext(&list, &data))
		{
			if (data == 22)
				LRemove(&list);
		}
	}

	// 삭제 후 남아있는 전체 데이터 출력
	printf("현재 데이터의 수: %d \n", LCount(&list));

	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		while (LNext(&list, &data))
			printf("%d ", data);
	}
	printf("\n\n");

	return 0;
}
