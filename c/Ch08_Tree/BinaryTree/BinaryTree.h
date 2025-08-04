#ifndef __BINARY_TREE_H__     // 이 헤더 파일이 중복 포함되는 것을 방지하는 전처리 지시문
#define __BINARY_TREE_H__

typedef int BTData;           // binary tree 노드에 저장될 데이터 타입을 정의

typedef struct _bTreeNode     // binary tree 노드를 표현하는 구조체 정의
{
	BTData data;                  // 노드에 저장될 데이터
	struct _bTreeNode * left;     // 왼쪽 자식 노드를 가리키는 포인터
	struct _bTreeNode * right;    // 오른쪽 자식 노드를 가리키는 포인터
} BTreeNode;

BTreeNode * MakeBTreeNode(void);            // 새로운 노드를 생성하는 함수
BTData GetData(BTreeNode * bt);             // 노드에 저장된 데이터를 반환하는 함수
void SetData(BTreeNode * bt, BTData data);  // 노드에 데이터를 저장하는 함수

BTreeNode * GetLeftSubTree(BTreeNode * bt);   // 왼쪽 subtree를 반환하는 함수
BTreeNode * GetRightSubTree(BTreeNode * bt);  // 오른쪽 subtree를 반환하는 함수

void MakeLeftSubTree(BTreeNode * main, BTreeNode * sub);   // 왼쪽 subtree를 연결하는 함수
void MakeRightSubTree(BTreeNode * main, BTreeNode * sub);  // 오른쪽 subtree를 연결하는 함수

#endif  // __BINARY_TREE_H__