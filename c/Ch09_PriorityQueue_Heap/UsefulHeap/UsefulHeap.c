#include "UsefulHeap.h"

// 힙 초기화 함수
// 데이터 개수 0으로 설정하고 우선순위 비교 함수(comp)를 등록
void HeapInit(Heap * ph, PriorityComp pc)
{
	ph->numOfData = 0;
	ph->comp = pc;
}

// 힙이 비어있는지 확인
int HIsEmpty(Heap * ph)
{
	if(ph->numOfData == 0)
		return TRUE;
	else
		return FALSE;
}

// 부모 노드의 인덱스를 반환
int GetParentIDX(int idx) 
{ 
	return idx / 2; 
}

// 왼쪽 자식 노드의 인덱스를 반환
int GetLChildIDX(int idx) 
{ 
	return idx * 2; 
}

// 오른쪽 자식 노드의 인덱스를 반환
int GetRChildIDX(int idx) 
{ 
	return GetLChildIDX(idx) + 1; 
}

// 두 자식 노드 중 우선순위가 더 높은 쪽의 인덱스를 반환
int GetHiPriChildIDX(Heap * ph, int idx)
{
	if(GetLChildIDX(idx) > ph->numOfData)
		return 0;  // 자식이 없음

	else if(GetLChildIDX(idx) == ph->numOfData)
		return GetLChildIDX(idx);  // 왼쪽 자식만 존재

	else
	{
		// 두 자식 중 우선순위 높은 쪽 선택
		if(ph->comp(ph->heapArr[GetLChildIDX(idx)], 
					ph->heapArr[GetRChildIDX(idx)]) < 0)
			return GetRChildIDX(idx);  // 오른쪽 자식이 우선순위 높음
		else
			return GetLChildIDX(idx);  // 왼쪽 자식이 우선순위 높음
	}
}

// 힙에 새로운 데이터를 삽입
void HInsert(Heap * ph, HData data)
{
	int idx = ph->numOfData + 1;  // 삽입될 위치

	// 부모 노드와 비교해가며 올라가기 (heapify-up)
	while(idx != 1)
	{
		if(ph->comp(data, ph->heapArr[GetParentIDX(idx)]) > 0)
		{
			// 부모보다 우선순위가 높으면 부모를 한 칸 아래로 내림
			ph->heapArr[idx] = ph->heapArr[GetParentIDX(idx)];
			idx = GetParentIDX(idx);
		}
		else
		{
			break;
		}
	}
	
	// 적절한 위치에 새 데이터 삽입
	ph->heapArr[idx] = data;
	ph->numOfData += 1;
}

// 힙에서 우선순위가 가장 높은 데이터를 삭제하고 반환
HData HDelete(Heap * ph)
{
	HData retData = ph->heapArr[1];                  // 루트 노드(삭제할 데이터)
	HData lastElem = ph->heapArr[ph->numOfData];     // 마지막 노드

	int parentIdx = 1;
	int childIdx;

	// 마지막 노드를 루트로 올리고 자식들과 비교하며 내려가기 (heapify-down)
	while((childIdx = GetHiPriChildIDX(ph, parentIdx)) != 0)
	{
		if(ph->comp(lastElem, ph->heapArr[childIdx]) >= 0)
			break;  // 자식보다 우선순위가 높거나 같으면 종료

		// 자식을 부모 위치로 끌어올림
		ph->heapArr[parentIdx] = ph->heapArr[childIdx];
		parentIdx = childIdx;
	}

	// 마지막 노드를 적절한 위치에 삽입
	ph->heapArr[parentIdx] = lastElem;
	ph->numOfData -= 1;

	return retData;  // 삭제된 루트 노드 반환
}