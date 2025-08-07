#include <stdio.h>
#include "UsefulHeap.h"

// 우선순위 비교 함수
// n2 - n1 → 작은 수가 우선 → 최소 힙 (오름차순 정렬)
// n1 - n2 → 큰 수가 우선순위가 높음 → 최대 힙 (내림차순 정렬)
int PriComp(int n1, int n2)
{
	return n2 - n1; 
	// return n1 - n2;  // 최소 힙 정렬로 바꾸고 싶다면 이 줄 사용
}

// 힙 정렬 함수
void HeapSort(int arr[], int n, PriorityComp pc)
{
	Heap heap;
	int i;

	// 힙 초기화 및 우선순위 비교 함수 등록
	HeapInit(&heap, pc);

	// 배열의 모든 데이터를 힙에 삽입 (Build Heap)
	for(i = 0; i < n; i++)
		HInsert(&heap, arr[i]);

	// 힙에서 하나씩 삭제하여 정렬된 순서로 배열에 저장
	for(i = 0; i < n; i++)
		arr[i] = HDelete(&heap);
}

int main(void)
{
	int arr[4] = {3, 4, 2, 1};
	int i;

	// 힙 정렬 수행 (우선순위 비교 함수에 따라 정렬 방향 결정됨)
	HeapSort(arr, sizeof(arr) / sizeof(int), PriComp);

	// 정렬된 배열 출력
	for(i = 0; i < 4; i++)
		printf("%d ", arr[i]);

	printf("\n");
	return 0;
}
