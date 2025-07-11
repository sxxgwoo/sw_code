#include <stdio.h>
#include "DBDLinkedList.h"

int main(void)
{
	// 리스트 생성 및 초기화
	List list;
	int data;
	ListInit(&list);  // head, tail 더미 노드 생성 및 연결

	// 1~8까지의 정수를 리스트에 삽입 (tail 앞에 삽입되므로 순서대로 저장됨)
	LInsert(&list, 1);  LInsert(&list, 2);
	LInsert(&list, 3);  LInsert(&list, 4);
	LInsert(&list, 5);  LInsert(&list, 6);
	LInsert(&list, 7);  LInsert(&list, 8);

	// ▶ 리스트 전체 순회 출력 (1부터 8까지 출력)
	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		while (LNext(&list, &data)) 
			printf("%d ", data);

		printf("\n");
	}

	// 짝수 데이터를 모두 찾아 삭제
	if (LFirst(&list, &data))
	{
		if (data % 2 == 0)
			LRemove(&list);  // 현재 노드가 짝수면 삭제

		while (LNext(&list, &data)) 
		{
			if (data % 2 == 0)
				LRemove(&list);  // 이후 노드 중 짝수도 삭제
		}
	}

	// 삭제 후 남은 리스트 데이터 출력 (홀수만 출력됨)
	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		while (LNext(&list, &data)) 
			printf("%d ", data);

		printf("\n\n");
	}

	return 0;
}
