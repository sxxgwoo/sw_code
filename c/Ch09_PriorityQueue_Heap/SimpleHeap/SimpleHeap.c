#include "SimpleHeap.h"

// 힙 초기화: 데이터 수를 0으로 설정
void HeapInit(Heap * ph)
{
	ph->numOfData = 0;
}

// 힙이 비어 있는지 확인
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

// 현재 노드에서 더 높은 우선순위를 가진 자식 노드의 인덱스를 반환
// 우선순위는 숫자가 작을수록 높음
int GetHiPriChildIDX(Heap * ph, int idx)
{
	// 자식 노드가 존재하지 않을 경우
	if(GetLChildIDX(idx) > ph->numOfData)
		return 0;

	// 왼쪽 자식만 존재하는 경우
	else if(GetLChildIDX(idx) == ph->numOfData)
		return GetLChildIDX(idx);

	else
	{
		// 양쪽 자식 중 우선순위가 더 높은 쪽을 선택
		if(ph->heapArr[GetLChildIDX(idx)].pr 
			> ph->heapArr[GetRChildIDX(idx)].pr)
			return GetRChildIDX(idx);
		else
			return GetLChildIDX(idx);
	}
}

// 힙에 새로운 데이터를 삽입하는 함수
void HInsert(Heap * ph, HData data, Priority pr)
{
	int idx = ph->numOfData + 1;  // 새 노드가 들어갈 인덱스
	HeapElem nelem = {pr, data};  // 새 노드 생성

	// 부모 노드와 우선순위 비교하여 위치를 찾아감
	while(idx != 1)	//가장 위에 까지
	{
		if(pr < (ph->heapArr[GetParentIDX(idx)].pr))  // 부모보다 우선순위가 높으면
		{
			// 부모의 값을 아래로 내리고
			ph->heapArr[idx] = ph->heapArr[GetParentIDX(idx)];
			// 인덱스를 위로 이동 즉 부모 index를 원래 나의 Index로 변경
			idx = GetParentIDX(idx);
		}
		else
			break;
	}
	
	// 적절한 위치에 새 노드를 삽입
	ph->heapArr[idx] = nelem;
	ph->numOfData += 1;
}

// 힙에서 우선순위가 가장 높은(가장 작은 pr 값) 데이터를 삭제하고 반환
HData HDelete(Heap * ph)
{
	// 반환할 최상위 노드 데이터 (루트)
	HData retData = (ph->heapArr[1]).data;

	// 마지막 노드를 임시 저장
	HeapElem lastElem = ph->heapArr[ph->numOfData];

	int parentIdx = 1;  // 현재 부모 인덱스
	int childIdx;

	// 자식과 우선순위를 비교해가며 적절한 위치를 찾아 내려감 (힙 속성 유지)
	// while(childIdx = GetHiPriChildIDX(ph, parentIdx))
	while ((childIdx = GetHiPriChildIDX(ph, parentIdx)) != 0)
	{
		// 마지막 노드가 자식보다 우선순위가 높거나 같다면 멈춤
		if(lastElem.pr <= ph->heapArr[childIdx].pr)
			break;

		// 자식을 한 단계 위로 끌어올림
		ph->heapArr[parentIdx] = ph->heapArr[childIdx];
		parentIdx = childIdx;
	}

	// 마지막 노드를 적절한 위치에 삽입
	ph->heapArr[parentIdx] = lastElem;
	ph->numOfData -= 1;

	return retData;
}