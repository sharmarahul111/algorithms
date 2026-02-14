#include<stdio.h>
#include<stdlib.h>
typedef struct Node{
  int value;
  struct Node *next;
} Node;
typedef struct {
  Node *head;
} LinkedList;
void append(LinkedList *list, int i);
int main(){
  LinkedList l1 ;
  l1.head = NULL;
  append(&l1, 20);
  append(&l1, 10);
  printf("%d %d\n",
         l1.head->value,
         l1.head->next->value
  );
  return 0;
}
void append(LinkedList *list, int i){
  Node *n = malloc(sizeof(Node));
  if(!n) exit(1);
  n->value = i;
  n->next = NULL;
  if(list->head == NULL){
    list->head = n;
  } else {
    Node *curr = list->head;
    while(curr->next){
      curr = curr->next;
    }
    curr->next = n;
  }
}
