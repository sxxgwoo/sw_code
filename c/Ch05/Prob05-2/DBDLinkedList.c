#include <stdio.h>
#include <stdlib.h>
#include "DBDLinkedList.h"

// 리스트 초기화 함수
void ListInit(List * plist)
{
	// 더미 노드(head, tail) 동적 생성
	plist->head = (Node*)malloc(sizeof(Node));
	plist->tail = (Node*)malloc(sizeof(Node));

	// head와 tail을 서로 연결
	plist->head->prev = NULL;
	plist->head->next = plist->tail;

	plist->tail->next = NULL;
	plist->tail->prev = plist->head;

	// 데이터 개수 초기화
	plist->numOfData = 0;
}

// 리스트의 끝(tail 앞)에 노드 삽입
void LInsert(List * plist, Data data) 
{
	// 새 노드 생성 및 데이터 저장
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	// 새 노드의 prev는 기존 마지막 노드 (tail의 앞 노드)
	newNode->prev = plist->tail->prev;

	// 새 노드의 앞 노드가 새 노드를 가리키도록 연결
	plist->tail->prev->next = newNode;

	// 새 노드의 next는 tail을 가리킴
	newNode->next = plist->tail;

	// tail의 prev를 새 노드로 갱신
	plist->tail->prev = newNode;

	// 노드 개수 증가
	(plist->numOfData)++;
}

// 첫 번째 노드(cur 초기화)로 이동 및 데이터 반환
int LFirst(List * plist, Data * pdata)
{
	// 리스트가 비어 있으면 FALSE 반환
	if (plist->head->next == plist->tail)
		return FALSE;

	// cur을 첫 번째 실제 노드로 설정
	plist->cur = plist->head->next;

	// cur이 가리키는 데이터 반환
	*pdata = plist->cur->data;
	return TRUE;
}

// 다음 노드로 이동 및 데이터 반환
int LNext(List * plist, Data * pdata)
{
	// tail에 도달했으면 실패
	if (plist->cur->next == plist->tail)
		return FALSE;

	// cur을 다음 노드로 이동
	plist->cur = plist->cur->next;

	// cur이 가리키는 데이터 반환
	*pdata = plist->cur->data;
	return TRUE;
}

// 현재 노드(cur)를 삭제하고 삭제된 값 반환
Data LRemove(List * plist)
{
	Node * rpos = plist->cur;        // 삭제할 노드
	Data remv = rpos->data;          // 삭제할 데이터 저장

	// 이전 노드와 다음 노드를 서로 연결하여 rpos 건너뜀
	plist->cur->prev->next = plist->cur->next;
	plist->cur->next->prev = plist->cur->prev;

	// cur을 이전 노드로 되돌림
	plist->cur = plist->cur->prev;

	// 노드 메모리 해제
	free(rpos);
	(plist->numOfData)--;
	return remv;
}

// 현재 리스트에 저장된 데이터 수 반환
int LCount(List * plist)
{
	return plist->numOfData;
}
