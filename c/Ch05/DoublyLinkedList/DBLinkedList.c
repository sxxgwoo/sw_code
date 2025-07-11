#include <stdio.h>
#include <stdlib.h>
#include "DBLinkedList.h"

// 리스트 초기화
void ListInit(List * plist)
{
	plist->head = NULL;       // 리스트가 비어있음을 나타냄
	plist->numOfData = 0;     // 데이터 수 0으로 초기화
}

// 리스트 앞부분에 노드 삽입
void LInsert(List * plist, Data data)
{
	// 새 노드 생성 및 데이터 저장
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	// 새 노드가 기존 head 앞에 삽입되므로
	newNode->next = plist->head;

	if (plist->head != NULL)
		plist->head->prev = newNode;  // 기존 첫 노드의 prev를 새 노드로 설정

	newNode->prev = NULL;            // 새 노드는 리스트의 맨 앞이므로 prev는 NULL
	plist->head = newNode;           // 리스트의 head를 새 노드로 갱신

	(plist->numOfData)++;            // 노드 수 증가
}

// 리스트 탐색 시작 (첫 번째 노드 선택)
int LFirst(List * plist, Data * pdata)
{
	if (plist->head == NULL)
		return FALSE;                // 리스트가 비어있으면 실패

	plist->cur = plist->head;       // cur을 리스트 맨 앞으로 이동
	*pdata = plist->cur->data;      // 현재 데이터 저장

	return TRUE;
}

// 다음 노드로 이동
int LNext(List * plist, Data * pdata)
{
	if (plist->cur->next == NULL)
		return FALSE;                // 다음 노드가 없으면 실패

	plist->cur = plist->cur->next;  // cur을 다음 노드로 이동
	*pdata = plist->cur->data;      // 현재 데이터 저장

	return TRUE;
}

// 이전 노드로 이동
int LPrevious(List * plist, Data * pdata)
{
	if (plist->cur->prev == NULL)
		return FALSE;                // 이전 노드가 없으면 실패

	plist->cur = plist->cur->prev;  // cur을 이전 노드로 이동
	*pdata = plist->cur->data;      // 현재 데이터 저장

	return TRUE;
}

// 리스트에 저장된 전체 노드 수 반환
int LCount(List * plist)
{
	return plist->numOfData;
}
