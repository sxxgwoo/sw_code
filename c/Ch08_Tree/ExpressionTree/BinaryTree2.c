#include <stdio.h>
#include <stdlib.h>
#include "BinaryTree2.h"

BTreeNode * MakeBTreeNode(void) // 새로운 노드를 동적 할당하여 생성하는 함수
{
	BTreeNode * nd = (BTreeNode*)malloc(sizeof(BTreeNode));  // 노드 메모리 할당

	nd->left = NULL;   // 왼쪽 자식 초기화
	nd->right = NULL;  // 오른쪽 자식 초기화
	return nd;
}

BTData GetData(BTreeNode * bt) // 노드에 저장된 데이터를 반환하는 함수
{
	return bt->data;
}

void SetData(BTreeNode * bt, BTData data) // 노드에 데이터를 설정하는 함수
{
	bt->data = data;
}

BTreeNode * GetLeftSubTree(BTreeNode * bt) // 왼쪽 subtree를 반환하는 함수
{
	return bt->left;
}

BTreeNode * GetRightSubTree(BTreeNode * bt) // 오른쪽 subtree를 반환하는 함수
{
	return bt->right;
}

void MakeLeftSubTree(BTreeNode * main, BTreeNode * sub) // 왼쪽 subtree를 설정하는 함수
{
	if(main->left != NULL)
		free(main->left);

	main->left = sub;
}

void MakeRightSubTree(BTreeNode * main, BTreeNode * sub) // 오른쪽 subtree를 설정하는 함수
{
	if(main->right != NULL)
		free(main->right);

	main->right = sub;
}

void PreorderTraverse(BTreeNode * bt, VisitFuncPtr action) // 루트 → 왼쪽 → 오른쪽
{
	if(bt == NULL)     // 현재 노드가 NULL이면 재귀 종료
		return;

	action(bt->data);
	PreorderTraverse(bt->left, action);
	PreorderTraverse(bt->right, action);
}

void InorderTraverse(BTreeNode * bt, VisitFuncPtr action) // 왼쪽 → 루트 → 오른쪽
{
	if(bt == NULL)     // 현재 노드가 NULL이면 재귀 종료
		return;

	InorderTraverse(bt->left, action);
	action(bt->data);
	InorderTraverse(bt->right, action);
}

void PostorderTraverse(BTreeNode * bt, VisitFuncPtr action) // 왼쪽 → 오른쪽 → 루트
{
	if(bt == NULL)     // 현재 노드가 NULL이면 재귀 종료
		return;

	PostorderTraverse(bt->left, action);
	PostorderTraverse(bt->right, action);
	action(bt->data);
}

