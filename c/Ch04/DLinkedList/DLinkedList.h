#ifndef __D_LINKED_LIST_H__    // 헤더 중복 포함 방지 시작
#define __D_LINKED_LIST_H__

#define TRUE	1               // 논리 상수를 위한 매크로
#define FALSE	0

// LData는 리스트에 저장할 데이터의 자료형 (지금은 int, 필요시 typedef만 바꾸면 됨)
typedef int LData;

// 연결 리스트의 노드 정의
typedef struct _node
{
	LData data;            // 실제 저장되는 데이터
	struct _node * next;   // 다음 노드를 가리키는 포인터 (단방향 연결)
} Node;

// 연결 리스트를 관리하는 구조체 정의
typedef struct _linkedList
{
	Node * head;           // 더미 헤더 노드를 가리키는 포인터
	Node * cur;            // 현재 탐색 중인 노드를 가리키는 포인터
	Node * before;         // 삭제를 돕는 멤버, 현재 노드 바로 앞 노드를 가리키는 포인터
	int numOfData;         // 리스트에 저장된 데이터의 수
	int (*comp)(LData d1, LData d2);	// 정렬 기준 함수 포인터 (NULL이면 정렬 안함)
} LinkedList;

// LinkedList를 간단히 List라는 이름으로 사용
typedef LinkedList List;

/*** 함수 원형 선언들 ***/

// 리스트 초기화 (더미 노드 생성, 멤버 초기화)
void ListInit(List * plist);

// 데이터 삽입 (정렬 기준에 따라 FInsert or SInsert 내부적으로 선택)
void LInsert(List * plist, LData data);

// 리스트 탐색 시작 (첫 번째 데이터 반환)
int LFirst(List * plist, LData * pdata);

// 리스트 다음 요소로 이동 (다음 데이터 반환)
int LNext(List * plist, LData * pdata);

// 현재 커서(cur)가 가리키는 노드 삭제
LData LRemove(List * plist);

// 리스트에 저장된 데이터의 개수 반환
int LCount(List * plist);

// 정렬 기준 설정 함수 (사용자가 정의한 비교 함수 설정)
void SetSortRule(List * plist, int (*comp)(LData d1, LData d2));

#endif   // __D_LINKED_LIST_H__
