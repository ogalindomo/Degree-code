#include <stdio.h>
#include <stdlib.h>
#include "tokenizer.h"

int string_length(char* str)
{
  int size = 0;
  for(int i = 0; str[i] != '\0'; i++, size++);
  return size;

}

char is_valid_character(char c)
{
  if(c <= 32)
    return 0;
  return 1;
}

char* find_word_start(char* str)
{
  int i = 0;
  for(; !is_valid_character(*(str+i)); i++);
  return (str+ i);
}

char* find_word_end(char* str)
{
  char *w;
  if(!is_valid_character(*str))
    w = find_word_start(str);
  else
    w = str;
  int i = 0;
  for(; is_valid_character(*(w+i)); i++);
  return (w+i);
}

int count_words(char* str)
{
  char* t = str;
  int word_num = 0;
  while(string_length(t)>1)
  {
    t = find_word_start(t);
    t = find_word_end(t);
    word_num++;
  }
  return word_num;
}

void copy_word(char* str, char* copy)
{
  int i = 0;
  while(1)
  {
    char temp = *(str+i);
    *(copy+i) = temp;
    i = i + 1;
    if(!is_valid_character(temp)){
      *(copy+i-1) = '\0';
      break;
    }
  }
}

char** tokenize(char* str)
{
  int words = count_words(str);
  char** t = (char**)(malloc(sizeof(char*) * (words+1)));
  *(t+words) = malloc(sizeof(char));
  **(t+words) = '\0';
  for(int i = 0; i < words; i++)
  {
    char* start = find_word_start(str);
    char* end = find_word_end(str);
    str = end;
    int size_word = end - start;
    *(t+i) = (char*)(malloc(sizeof(char)*(size_word+1)));
    copy_word(start, *(t+i));
  }
  return t;
}

void print_tokens(char** tokens)
{
  char* part;
  for(int section = 0; *(part = tokens[section]); section++)
  {printf("%s \n",part);}
}

void free_tokens(char** tokens)
{
  for(int i = 0;;i++)
  {
    char temp = **(tokens+i);
    free(*(tokens+i));
    if(!temp) break;
  }
  free(tokens);
}
