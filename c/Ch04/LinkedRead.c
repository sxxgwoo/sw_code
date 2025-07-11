#include <stdio.h>
#include <stdlib.h>
/*
[head]                                     [tail]
  ↓                                          ↓
+-------+------+     +-------+------+     +-------+------+
|   5   | o----->----|   7   | o----->----|   2   | NULL |
+-------+------+     +-------+------+     +-------+------+

*/
// 단일 연결 리스트의 노드 정의
typedef struct _node
{
	int data;
	struct _node * next;	//구조체 내부에 자기 자신의 타입을 포인터로 다시 사용하는 구조
} Node; //별명 지어주는것임 typedef와 같이 사용

int main(void)
{
	Node * head = NULL;  // 리스트의 첫 번째 노드를 가리키는 포인터
	Node * tail = NULL;  // 리스트의 마지막 노드를 가리키는 포인터
	Node * cur = NULL;   // 리스트 순회에 사용할 포인터
	Node * newNode = NULL;
	int readData;

	/**** 데이터를 입력받아 연결 리스트에 저장하는 과정 ****/
	while(1)
	{
		printf("자연수 입력: ");
		scanf("%d", &readData);

		if(readData < 1)  // 1 미만의 수를 입력하면 입력 종료
			break;

		// 새 노드 생성 및 데이터 저장
		newNode = (Node*)malloc(sizeof(Node));
		newNode->data = readData;
		newNode->next = NULL;

		// 첫 번째 노드인 경우
		if(head == NULL)
			head = newNode;
		else
			tail->next = newNode;  // 이전 노드의 next가 새 노드를 가리키게 함

		tail = newNode;  // tail을 새 노드로 갱신
	}
	printf("\n");

	/**** 입력 받은 데이터를 순차적으로 출력하는 과정 ****/
	printf("입력 받은 데이터의 전체 출력!\n");
	if(head == NULL) 
	{
		printf("저장된 자연수가 존재하지 않습니다.\n");
	}
	else 
	{
		cur = head;
		// 첫 번째 노드의 데이터 출력
		printf("%d  ", cur->data);
		
		// 두 번째 노드부터 순차적으로 출력
		while(cur->next != NULL)
		{
			cur = cur->next;
			printf("%d  ", cur->data);
		}
	}
	printf("\n\n");

	/**** 연결 리스트에 할당된 메모리를 해제하는 과정 ****/
	if(head == NULL) 
	{
		return 0;  // 해제할 노드가 없음
	}
	else 
	{
		Node * delNode = head;         // 삭제할 노드를 가리키는 포인터
		Node * delNextNode = head->next; // 다음 노드를 가리키는 포인터

		// 첫 번째 노드 삭제
		printf("%d을(를) 삭제합니다.\n", delNode->data);
		free(delNode);

		// 나머지 노드들 삭제
		while(delNextNode != NULL)
		{
			delNode = delNextNode;
			delNextNode = delNextNode->next;

			printf("%d을(를) 삭제합니다.\n", delNode->data);
			free(delNode);
		}
		// 모든 노드 삭제 후 포인터 초기화
		head = NULL;
		tail = NULL;
	}

	return 0;
}
