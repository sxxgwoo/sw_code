#include <stdio.h>
#include "DBLinkedList.h"

int main(void)
{
	// 리스트 생성 및 초기화
	List list;
	int data;
	ListInit(&list);  // head = NULL, 데이터 수 0으로 초기화

	// 1~8까지의 정수 삽입 (앞에서부터 삽입되므로 역순 저장됨)
	LInsert(&list, 1);  // 1
	LInsert(&list, 2);  // 2 1
	LInsert(&list, 3);  // 3 2 1
	LInsert(&list, 4);  // 4 3 2 1
	LInsert(&list, 5);  // 5 4 3 2 1
	LInsert(&list, 6);  // 6 5 4 3 2 1
	LInsert(&list, 7);  // 7 6 5 4 3 2 1
	LInsert(&list, 8);  // 8 7 6 5 4 3 2 1

	// 리스트 앞 → 뒤 순회 후, 다시 뒤 → 앞으로 역순회
	if (LFirst(&list, &data))  // 처음 노드 선택
	{
		printf("%d ", data);   // 첫 노드 출력

		// ▶ 다음 노드로 계속 이동하며 출력 (8 → 1 순서로 출력)
		while (LNext(&list, &data))
			printf("%d ", data);

		// ◀ 다시 이전 노드로 이동하며 출력 (1 → 8 역순 출력)
		while (LPrevious(&list, &data))
			printf("%d ", data);

		printf("\n\n");
	}

	return 0;
}
