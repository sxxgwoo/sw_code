#include <stdio.h>
#include <stdlib.h>
#include "CLinkedList.h"

// 리스트 초기화 함수
void ListInit(List * plist)
{
	plist->tail = NULL;    // tail이 NULL이면 리스트가 비어있음을 의미
	plist->cur = NULL;     // 현재 노드를 가리킬 포인터
	plist->before = NULL;  // 현재 노드의 이전 노드를 가리킬 포인터
	plist->numOfData = 0;  // 저장된 데이터 수 초기화
}

// 원형 리스트의 앞부분에 노드 삽입
void LInsertFront(List * plist, Data data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	if(plist->tail == NULL) 
	{
		// 첫 번째 노드 삽입 시: 자기 자신을 가리키도록 설정
		plist->tail = newNode;
		newNode->next = newNode;
	}
	else
	{
		// 새 노드를 tail 다음 위치에 삽입
		newNode->next = plist->tail->next;
		plist->tail->next = newNode;
	}

	(plist->numOfData)++;
}

// 원형 리스트의 뒷부분(tail 뒤)에 노드 삽입
void LInsert(List * plist, Data data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	if(plist->tail == NULL) 
	{
		// 첫 번째 노드 삽입 시: 자기 자신을 가리킴
		plist->tail = newNode;
		newNode->next = newNode;
	}
	else 
	{
		// tail 뒤에 새 노드 삽입 후 tail 갱신
		newNode->next = plist->tail->next; // 새 노드가 head를 가리키게 함
		plist->tail->next = newNode;       // 기존 tail이 새 노드를 가리키게 함
		plist->tail = newNode;             // tail을 새 노드로 갱신
	}

	(plist->numOfData)++;
}

// 리스트 순회 시작 (첫 번째 노드로 이동)
int LFirst(List * plist, Data * pdata)
{
	if(plist->tail == NULL)    // 리스트가 비어 있으면 실패
		return FALSE;

	plist->before = plist->tail;        // before는 tail부터 시작
	plist->cur = plist->tail->next;     // cur은 head 위치로 시작

	*pdata = plist->cur->data;          // 현재 노드의 데이터 출력
	return TRUE;
}

// 리스트 순회 다음 노드로 이동
int LNext(List * plist, Data * pdata)
{
	if(plist->tail == NULL)    // 리스트가 비어 있으면 실패
		return FALSE;

	plist->before = plist->cur;         // before는 현재 위치로 이동
	plist->cur = plist->cur->next;      // cur은 다음 노드로 이동

	*pdata = plist->cur->data;          // 현재 노드의 데이터 출력
	return TRUE;
}

// 현재 cur 위치의 노드를 삭제
Data LRemove(List * plist)
{
	Node * rpos = plist->cur;           // 삭제 대상 노드
	Data rdata = rpos->data;            // 삭제할 데이터 복사

	if(rpos == plist->tail)    // 삭제 대상이 tail일 경우
	{
		if(plist->tail == plist->tail->next)    // 노드가 1개뿐이면
			plist->tail = NULL;                 // tail을 NULL로 초기화 (리스트 비어짐)
		else
			plist->tail = plist->before;        // tail을 이전 노드로 이동
	}

	// 삭제 대상 제거: 이전 노드가 다음 노드를 건너뛰도록 연결
	plist->before->next = plist->cur->next;
	plist->cur = plist->before;        // cur 포인터를 이전 노드로 되돌림

	free(rpos);                        // 메모리 해제
	(plist->numOfData)--;
	return rdata;                      // 삭제한 데이터 반환
}

// 리스트에 저장된 데이터의 수 반환
int LCount(List * plist)
{
	return plist->numOfData;
}
