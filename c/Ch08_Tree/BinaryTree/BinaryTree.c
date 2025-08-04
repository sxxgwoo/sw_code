#include <stdio.h>
#include <stdlib.h>
#include "BinaryTree.h"

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
    if(main->left != NULL)       // 기존 왼쪽 자식 노드가 있으면
        free(main->left);        // 메모리 해제 (기존 subtree 제거)

    main->left = sub;            // 새로운 왼쪽 subtree 연결
}

void MakeRightSubTree(BTreeNode * main, BTreeNode * sub) // 오른쪽 subtree를 설정하는 함수
{
    if(main->right != NULL)      // 기존 오른쪽 자식 노드가 있으면
        free(main->right);       // 메모리 해제 (기존 subtree 제거)

    main->right = sub;           // 새로운 오른쪽 subtree 연결
}