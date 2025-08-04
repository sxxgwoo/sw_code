#include <stdio.h>
#include "BinaryTree.h"

void InorderTraverse(BTreeNode * bt)   // 왼쪽 → 루트 → 오른쪽 순서로 노드를 방문
{
	if(bt == NULL)    // 현재 노드가 NULL이면 재귀 종료
		return;

	InorderTraverse(bt->left);    // 왼쪽 subtree 순회
	printf("%d \n", bt->data);    // 현재 노드의 데이터 출력
	InorderTraverse(bt->right);   // 오른쪽 subtree 순회
}

void PreorderTraverse(BTreeNode * bt)   // 루트 → 왼쪽 → 오른쪽 순서로 노드를 방문
{
	if(bt == NULL)    // 현재 노드가 NULL이면 재귀 종료
		return;

    printf("%d \n", bt->data);     // 현재 노드의 데이터 출력
	PreorderTraverse(bt->left);    // 왼쪽 subtree 순회
	PreorderTraverse(bt->right);   // 오른쪽 subtree 순회
}

void PostorderTraverse(BTreeNode * bt)   // 왼쪽 → 오른쪽 → 루트 순서로 노드를 방문
{
	if(bt == NULL)    // 현재 노드가 NULL이면 재귀 종료
		return;

	PostorderTraverse(bt->left);    // 왼쪽 subtree 순회
	PostorderTraverse(bt->right);   // 오른쪽 subtree 순회
    printf("%d \n", bt->data);      // 현재 노드의 데이터 출력
}

// 트리 구조 만들기  //
//       bt1     //
//      /   \    //
//    bt2   bt3  //
//    /          //
//  bt4          //

int main(void)
{
	BTreeNode * bt1 = MakeBTreeNode();
	BTreeNode * bt2 = MakeBTreeNode();
	BTreeNode * bt3 = MakeBTreeNode();
	BTreeNode * bt4 = MakeBTreeNode();

	SetData(bt1, 1); 
	SetData(bt2, 2);
	SetData(bt3, 3);
	SetData(bt4, 4);

	MakeLeftSubTree(bt1, bt2);
	MakeRightSubTree(bt1, bt3);
	MakeLeftSubTree(bt2, bt4);

	InorderTraverse(bt1);   // 출력 순서: bt4 → bt2 → bt1 → bt3 (4 2 1 3)
	return 0; 
}