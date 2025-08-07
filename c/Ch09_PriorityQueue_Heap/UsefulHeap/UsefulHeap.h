#ifndef __USEFUL_HEAP_H__
#define __USEFUL_HEAP_H__

#define TRUE	1
#define FALSE	0

/*** 힙 관련 설정 상수 ***/
#define HEAP_LEN	100		// 힙의 최대 저장 개수

typedef char HData;			// 힙에 저장할 데이터의 자료형

/*** 우선순위 비교 함수 포인터 타입 정의 ***/
// 두 데이터 d1, d2를 비교하여
// - d1이 우선순위가 높으면 0보다 큰 값 반환
// - d2가 우선순위가 높으면 0보다 작은 값 반환
// - 둘의 우선순위가 같으면 0 반환
typedef int PriorityComp(HData d1, HData d2);

/*** 힙 구조체 정의 ***/
typedef struct _heap
{
	PriorityComp * comp;			// 우선순위 비교 함수 포인터
	int numOfData;					// 저장된 데이터의 수
	HData heapArr[HEAP_LEN];		// 힙 배열 (index: 1부터 시작)
} Heap;

/*** 힙의 기본 연산 함수들 ***/
void HeapInit(Heap * ph, PriorityComp pc);	// 힙 초기화 + 비교 함수 등록
int HIsEmpty(Heap * ph);					// 힙이 비었는지 확인

void HInsert(Heap * ph, HData data);		// 힙에 데이터 삽입
HData HDelete(Heap * ph);					// 우선순위 가장 높은 데이터 삭제 및 반환

#endif