#include <stdio.h>
#include <stdlib.h>
#include "DLinkedList.h"

// 리스트 초기화 함수
void ListInit(List * plist)
{
	// 더미(헤더) 노드 생성
	plist->head = (Node*)malloc(sizeof(Node));
	plist->head->next = NULL;

	// 정렬 기준 함수 초기화 (기본은 NULL)
	plist->comp = NULL;

	// 데이터 수 초기화
	plist->numOfData = 0;
}

// 정렬 없이 앞쪽에 노드 추가 (Head 바로 뒤에 삽입)
void FInsert(List * plist, LData data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;

	// 새 노드를 헤더 바로 뒤에 연결
	newNode->next = plist->head->next;
	plist->head->next = newNode;

	(plist->numOfData)++;
}

// 정렬 기준(comp 함수)을 기반으로 정렬 삽입
void SInsert(List * plist, LData data)
{
	Node * newNode = (Node*)malloc(sizeof(Node));
	Node * pred = plist->head;  // pred는 더미 노드를 가리킴
	newNode->data = data;

	// comp 함수 기준에 따라 올바른 위치 탐색
	while(pred->next != NULL &&
		plist->comp(data, pred->next->data) != 0)
	{
		pred = pred->next;
	}

	// 노드 삽입
	newNode->next = pred->next;
	pred->next = newNode;

	(plist->numOfData)++;
}

// 데이터 삽입 함수 (정렬 기준이 없으면 FInsert, 있으면 SInsert)
void LInsert(List * plist, LData data)
{
	if(plist->comp == NULL)
		FInsert(plist, data);     // 정렬 없이 삽입
	else
		SInsert(plist, data);     // 정렬 기준에 따라 삽입
}

// 리스트 탐색 시작 (첫 번째 요소)
int LFirst(List * plist, LData * pdata)
{
	// 리스트가 비어 있으면 FALSE 반환
	if(plist->head->next == NULL)
		return FALSE;

	// cur, before 포인터 설정
	plist->before = plist->head;
	plist->cur = plist->head->next;

	// 첫 번째 노드의 데이터를 반환
	*pdata = plist->cur->data;
	return TRUE;
}

// 리스트 다음 요소로 이동
int LNext(List * plist, LData * pdata)
{
	// 다음 노드가 없으면 FALSE
	if(plist->cur->next == NULL)
		return FALSE;

	// cur, before를 한 노드씩 이동
	plist->before = plist->cur;
	plist->cur = plist->cur->next;

	// 현재 노드의 데이터 반환
	*pdata = plist->cur->data;
	return TRUE;
}

// 현재 cur 위치의 노드를 삭제
LData LRemove(List * plist)
{
	Node * rpos = plist->cur;        // 소멸 대상의 주소 값을 rpos에 저장
	LData rdata = rpos->data;        // 소멸 대상의 데이터를 rdata에 저장

	// 삭제 노드의 이전 노드가 다음 노드를 건너뛰게 연결
	plist->before->next = plist->cur->next;

	// cur 위치를 이전 노드로 되돌림
	plist->cur = plist->before;

	free(rpos);                      // 메모리 해제
	(plist->numOfData)--;
	return rdata;                    // 삭제된 데이터 반환
}

// 리스트에 저장된 데이터 수 반환
int LCount(List * plist)
{
	return plist->numOfData;
}

// 정렬 기준(comp 함수 포인터)을 설정	
void SetSortRule(List * plist, int (*comp)(LData d1, LData d2))
{
	plist->comp = comp;
}
