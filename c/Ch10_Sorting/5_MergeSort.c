#include <stdio.h>
#include <stdlib.h>

// 두 부분 배열을 정렬하여 하나로 병합하는 함수
void MergeTwoArea(int arr[], int left, int mid, int right)
{
	int fIdx = left;        // 왼쪽 부분 배열 시작 인덱스
	int rIdx = mid + 1;     // 오른쪽 부분 배열 시작 인덱스
	int i;

	// 병합 결과를 담을 배열 sortArr의 동적 할당! 저장할 임시 배열 생성
	int * sortArr = (int*)malloc(sizeof(int) * (right + 1));
	int sIdx = left;        // sortArr에 값을 채워 넣을 인덱스

	// 양쪽 배열에서 작은 값을 하나씩 sortArr에 채워 넣음
	while(fIdx <= mid && rIdx <= right)
	{
		// 병합 할 두 영역의 데이터들을 비교하여, 
		// 정렬 순서대로 sortArr에 하나씩 옮겨 담는다.
		if(arr[fIdx] <= arr[rIdx])
			sortArr[sIdx] = arr[fIdx++];
		else
			sortArr[sIdx] = arr[rIdx++];
		sIdx++;
	}

	if(fIdx > mid)
	{	
		// 배열의 앞부분이 모두 sortArr에 옮겨졌다면,
		// 배열의 뒷부분에 남은 데이터들을 sortArr에 그대로 옮긴다.
		for(i = rIdx; i <= right; i++, sIdx++)
			sortArr[sIdx] = arr[i];
	}
	else
	{
		// 배열의 뒷부분이 모두 sortArr에 옮겨졌다면,
		// 배열의 앞부분에 남은 데이터들을 sortArr에 그대로 옮긴다.
		for(i = fIdx; i <= mid; i++, sIdx++)
			sortArr[sIdx] = arr[i];
	}

	// 병합된 결과를 원래 배열(arr)에 복사
	for(i = left; i <= right; i++)
		arr[i] = sortArr[i];
	
	// 임시 배열 메모리 해제
	free(sortArr);
}

// 병합 정렬 함수 (재귀적 분할)
void MergeSort(int arr[], int left, int right)
{
	int mid;

	// 분할 기준: left < right일 때만 수행 (원소 2개 이상)
	if(left < right)
	{
		// 중간 지점 계산
		mid = (left + right) / 2;

		// 왼쪽 부분 배열 정렬
		MergeSort(arr, left, mid);

		// 오른쪽 부분 배열 정렬
		MergeSort(arr, mid + 1, right);

		// 정렬된 두 부분 배열 병합
		MergeTwoArea(arr, left, mid, right);
	}
}

int main(void)
{
	int arr[7] = {3, 2, 4, 1, 7, 6, 5};
	int i;

	// 배열 전체에 대해 병합 정렬 수행
	MergeSort(arr, 0, sizeof(arr) / sizeof(int) - 1);

	// 정렬 결과 출력
	for(i = 0; i < 7; i++)
		printf("%d ", arr[i]);

	printf("\n");
	return 0;
}
