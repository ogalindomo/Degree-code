#include <stdio.h>
#include <stdlib.h>
#include "tokenizer.h"
#include "history.h"
#define BUFFER 100
int main()
{
  char *p;
  int i = 0;
  int secretInput(char*w, int size);
  int identity(char*w, int size);
  int history(char* w, int size);
  int erase(char*w, int size);
  int access(char*w, int size);
  List* inputs = init_history();
 while(1)
 {
   p = (char*)(malloc(sizeof(char) * BUFFER));
   printf("* ");
   for(char t;(t = getchar()) != '\n' && i < BUFFER && !(t < 32); i++)
   {
       *(p+i) = t;
   }
   ////GOOD DO NOT TOUCH////
   if(secretInput(p, i))
     printf("Beautiful!!!");
   else if(identity(p, i))
     printf("Galindo");
   else{
     // for(int j = 0; j < i && j < BUFFER; j++){
       int num =0;
       if(history(p,i))
       {
	 print_history(inputs);
       }
       else if(erase(p,i)){
         free_history(inputs);
	 printf("Bye!\n");
	 exit(0);
       }
       else if((num = access(p,i)) > 0)
       {
	 printf("%s \n", get_history(inputs,num));
       }
       else
       {
	 add_history(inputs, p);
	 char** in = tokenize(p);
	 print_tokens(in);
	 free_tokens(in);
       }
       //printf("%c",*(p+j));
   }  
   printf("\n");
   i = 0;
 }
   ////////////////////////
}

 int secretInput (char* w, int size)
{
  if(size != 3)
    return 0;
  char secret [] = "Hey";
  for(int i = 0; i < size; i+=1)
  {
    if(*(w+i) != *(secret+i))
      return 0;
  }
  return 1;
}

int access (char*w, int size)
{
  //printf("Size of input %d\n",size);
  if(size < 3)
    return 0;
  else{
    char in[] ="get";
    for(int i = 0; i < 3; i+=1)
      if(*(w+i) != *(in+i))
	return 0;
    int piece = 0;
    char*start = find_word_end(w);
    start = find_word_start(start);
    char* end = find_word_end(start);
    //printf("%s \n",start);
    //printf("Size: %d\n",(end-start));
    int size = end-start;
    for(int i = 0; i < size; i++)
    {
      piece = piece*10 + ((int)(*(start+i) -'0'));
      printf("%d \n",piece);
    }
    return piece;
  }

}

int erase(char*w, int size)
{
  if(size != 4)
    return 0;
  char word[] = "free";
  for(int i = 0; i < size; i+=1)
  {
    if(*(w+i) != *(word+i))
      return 0;
  }
  return 1;
}

int history (char* w, int size){
  if(size != 7)
    return 0;
  char history [] = "history";
  for(int i = 0; i < size; i+=1)
  {
    if(*(w+i) != *(history+i))
      return 0;
  }
  return 1;
}

int identity (char* w, int size)
{
  if(size != 9)
    return 0;
  char id [] = "who am I?";
  for(int i = 0; i < size; i+=1)
  {
    if(*(w+i) != *(id+i))
      return 0;
  }
  return 1;
}
