#include <stdio.h>
#include "CLinkedList.h"

int main(void)
{
	// 리스트 생성 및 초기화
	List list;
	int data, i, nodeNum;
	ListInit(&list);  // tail, cur, before를 NULL로 초기화

	// 데이터 삽입: 뒷부분 삽입 3개, 앞부분 삽입 2개 (1~5)
	LInsert(&list, 3);      // tail 뒤 삽입 → 3
	LInsert(&list, 4);      // tail 뒤 삽입 → 3 4
	LInsert(&list, 5);      // tail 뒤 삽입 → 3 4 5
	LInsertFront(&list, 2); // head 앞 삽입 → 2 3 4 5
	LInsertFront(&list, 1); // head 앞 삽입 → 1 2 3 4 5

	// 리스트 순회 출력 (전체 데이터 3회 반복 출력)
	if (LFirst(&list, &data))
	{
		printf("%d ", data);  // 첫 번째 노드 출력

		// 총 노드 수 * 3 - 1 만큼 순회하며 출력
		for (i = 0; i < LCount(&list) * 3 - 1; i++)
		{
			if (LNext(&list, &data))
				printf("%d ", data);
		}
	}
	printf("\n");

	// 짝수 값 노드를 찾아 모두 삭제
	nodeNum = LCount(&list);  // 삭제 전 노드 개수 저장

	if (nodeNum != 0)
	{
		LFirst(&list, &data);  // 첫 노드부터 탐색 시작

		if (data % 2 == 0)     // 짝수면 삭제
			LRemove(&list);

		for (i = 0; i < nodeNum - 1; i++)
		{
			LNext(&list, &data);

			if (data % 2 == 0) // 짝수면 삭제
				LRemove(&list);
		}
	}

	// 삭제 후 리스트 전체 한 바퀴 순회 출력
	if (LFirst(&list, &data))
	{
		printf("%d ", data);

		for (i = 0; i < LCount(&list) - 1; i++)
		{
			if (LNext(&list, &data))
				printf("%d ", data);
		}
	}

	return 0;
}
