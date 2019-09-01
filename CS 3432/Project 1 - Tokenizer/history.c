#include <stdio.h>
#include <stdlib.h>
#include "history.h"
#include "tokenizer.h"
List* init_history()
{
  return (List*)(malloc(sizeof(List))); 
}

void add_history(List* list, char* str)
{
  void copy_sentence(char* original, char* copy);
  if(list == NULL)
    return;
  else if(list->root == NULL){
    list->root = (Item*)(malloc(sizeof(Item)));
    list->root->str = (char*)(malloc(sizeof(char) * (string_length(str)+1)));
    copy_sentence(str,list->root->str);
    list->root->id = 1;
    list->root->next = NULL;
  }
  else{
    // printf("Here: %s \n",str);
    Item* p = list->root;
    while(p->next !=  NULL){p = p->next;}
    p->next = (Item*)(malloc(sizeof(Item)));
    p->next->str = (char*)(malloc(sizeof(char) *(string_length(str)+1)));
    copy_sentence(str, p->next->str);
    p->next->id = (p->id)+1;
    p->next->next = NULL;
  }
}

char* get_history(List* list, int id)
{
  Item* p = list->root;
  for(;;p = p->next)
  {
    if(p == NULL)
      return "Index not found";
    else if(p->id == id)
      return p->str;
  }
  
}

void print_history(List* list)
{
  Item* p = list->root;
  printf("History: \n");
  while(p)
  {
    if(p->str)
      printf("%d %s \n", p->id, p->str);
    p = p->next;
  }
}

void free_history(List* list)
{
  Item* current = list->root;
  Item* temp;
  if(list != NULL){
    current = list->root;
  }
  while(current != NULL)
  {
    temp = current;
    current = current->next;
    free(temp);
  }
  free(list);
}

void copy_sentence(char* original, char* copy)
{
  int i = 0, size = string_length(original);
  //printf("Size: %d \n", size);
  for(;i < size; i++)
    *(copy + i) = *(original +i);
  *(copy + size) = '\0';
}
