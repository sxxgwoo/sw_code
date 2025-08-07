#ifndef __SIMPLE_HEAP_H__
#define __SIMPLE_HEAP_H__

// 논리형 상수 정의
#define TRUE	1
#define FALSE	0

// 힙에 저장할 수 있는 최대 데이터 수
#define HEAP_LEN	100

// 힙에 저장될 데이터의 자료형 정의
typedef char HData;          // 실제 저장할 데이터의 타입 (문자형)
typedef int Priority;        // 우선순위 타입 (정수형)

// 힙 요소를 표현하는 구조체
typedef struct _heapElem
{
	Priority pr;	// 우선순위 값: 값이 작을수록 높은 우선순위
	HData data;     // 저장할 실제 데이터
} HeapElem;

// 힙을 표현하는 구조체
typedef struct _heap
{
	int numOfData;			           // 현재 저장된 데이터 수
	HeapElem heapArr[HEAP_LEN];       // 힙 배열: 0번 인덱스는 사용하지 않음
} Heap;

// 힙 초기화 함수
void HeapInit(Heap * ph);

// 힙이 비어있는지 확인하는 함수
int HIsEmpty(Heap * ph);

// 힙에 데이터와 우선순위를 삽입하는 함수
void HInsert(Heap * ph, HData data, Priority pr);

// 힙에서 우선순위가 가장 높은 데이터를 삭제하고 반환하는 함수
HData HDelete(Heap * ph);

#endif