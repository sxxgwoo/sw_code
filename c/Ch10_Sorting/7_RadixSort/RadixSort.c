#include <stdio.h>
#include "ListBaseQueue.h"  // 큐 구조체 및 함수 정의 포함

#define BUCKET_NUM 10       // 0~9까지의 10진수 숫자마다 하나의 버킷(큐)

// -----------------------------
// 기수 정렬 함수
// arr[]     : 정렬할 배열
// num       : 배열 원소 개수
// maxLen    : 가장 긴 숫자의 자릿수
// -----------------------------
void RadixSort(int arr[], int num, int maxLen)
{
	Queue buckets[BUCKET_NUM];   // 0부터 9까지 각 자릿수용 큐(버킷)
	int bi;     // 버킷 인덱스
	int pos;    // 현재 정렬 중인 자릿수 위치 (0 = 1의 자리)
	int di;     // 데이터 인덱스
	int divfac = 1;     // 자릿수 추출용 나눗셈 계수 (1, 10, 100, ...)
	int radix;          // 자릿수 값 (0~9)

	// 모든 버킷(큐) 초기화
	for (bi = 0; bi < BUCKET_NUM; bi++)
		QueueInit(&buckets[bi]);

	// 자릿수 만큼 반복 (1의 자리 → 10의 자리 → ...)
	for (pos = 0; pos < maxLen; pos++)
	{
		// 현재 자릿수를 기준으로 데이터를 각각의 큐에 분배
		for (di = 0; di < num; di++)
		{
			radix = (arr[di] / divfac) % 10;  // 현재 자릿수 추출
			Enqueue(&buckets[radix], arr[di]); // 해당 버킷에 데이터 저장
		}

		// 버킷에 저장된 데이터를 다시 원래 배열로 재구성 (왼쪽부터 순서대로)
		for (bi = 0, di = 0; bi < BUCKET_NUM; bi++)
		{
			while (!QIsEmpty(&buckets[bi]))
				arr[di++] = Dequeue(&buckets[bi]);
		}

		// 다음 자릿수(10배 상위 자릿수)로 이동
		divfac *= 10;
	}
}

// -----------------------------
// 테스트용 메인 함수
// -----------------------------
int main(void)
{
	int arr[7] = {13, 212, 14, 7141, 10987, 6, 15};  // 정렬할 숫자 배열
	int len = sizeof(arr) / sizeof(int);            // 배열의 길이
	int i;

	RadixSort(arr, len, 5);   // 최대 5자리 수까지 정렬

	// 정렬된 결과 출력
	for (i = 0; i < len; i++)
		printf("%d ", arr[i]);

	printf("\n");
	return 0;
}
