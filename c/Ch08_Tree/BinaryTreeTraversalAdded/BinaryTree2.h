#ifndef __BINARY_TREE2_H__     // 헤더 파일 중복 포함 방지를 위한 전처리 지시문 시작
#define __BINARY_TREE2_H__

typedef int BTData;         // binary tree 노드에 저장될 데이터 타입을 정의

typedef struct _bTreeNode   // binary tree 노드를 표현하는 구조체 정의
{
    BTData data;                  // 노드에 저장될 데이터
    struct _bTreeNode * left;     // 왼쪽 자식 노드를 가리키는 포인터
    struct _bTreeNode * right;    // 오른쪽 자식 노드를 가리키는 포인터
} BTreeNode;

BTreeNode * MakeBTreeNode(void);             // 새로운 노드를 생성하는 함수
BTData GetData(BTreeNode * bt);              // 노드에 저장된 데이터를 반환하는 함수
void SetData(BTreeNode * bt, BTData data);   // 노드에 데이터를 저장하는 함수

BTreeNode * GetLeftSubTree(BTreeNode * bt);  // 왼쪽 subtree를 반환하는 함수
BTreeNode * GetRightSubTree(BTreeNode * bt); // 오른쪽 subtree를 반환하는 함수

void MakeLeftSubTree(BTreeNode * main, BTreeNode * sub);   // 왼쪽 subtree를 연결하는 함수
void MakeRightSubTree(BTreeNode * main, BTreeNode * sub);  // 오른쪽 subtree를 연결하는 함수

// VisitFuncPtr는 "BTData 타입의 인자를 받아 void를 반환하는 함수 포인터 타입"으로 정의된다. 즉, VisitFuncPtr은 어떤 함수를 가리키는 포인터 변수 타입으로 사용할 수 있다.
// 예: void Print(BTData d); 라는 함수가 있을 때
//     VisitFuncPtr pf = Print;  처럼 사용 가능하여, pf(10); → Print(10) 호출됨
typedef void (*VisitFuncPtr)(BTData data);

void PreorderTraverse(BTreeNode * bt, VisitFuncPtr action);  // 루트 → 왼쪽 → 오른쪽 순서로 트리를 순회하며 각 노드에 action 함수 적용
void InorderTraverse(BTreeNode * bt, VisitFuncPtr action);   // 왼쪽 → 루트 → 오른쪽 순서로 트리를 순회하며 각 노드에 action 함수 적용
void PostorderTraverse(BTreeNode * bt, VisitFuncPtr action); // 왼쪽 → 오른쪽 → 루트 순서로 트리를 순회하며 각 노드에 action 함수 적용

#endif  // __BINARY_TREE2_H__