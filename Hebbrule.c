#include <stdio.h>
#include <string.h>

int main(int argc , char* argv[])
{
   if (!(argc == 5)){
      printf("Input counter invalid value, please provide 4 values\n");
      return 1;
      }

   int reference[4] = {0 , 0, 0, 0};
   char* try1 = ("-1");
   char* try2 = ("1");

   for (int k = 0 ; k < 4 ; k++){
       if(strcmp(argv[k + 1],try1) == 0){
           reference[k] = -1;
       }
       else if(strcmp(argv[k + 1],try2) == 0){
           reference[k] = 1;
       }
       else{
          printf("Invalid input value , please try 1 or -1\n");
          return 2;
       }}

  int bidimensional[4][2] = {{1, 1},{-1, 1}, {1, -1},{-1, -1}};
  int wanterior[2] = {0, 0};
  int wnovo[2] = {0, 0};
  int banterior = 0;
  int bnovo = 0;
  int limiar = 0;
  int y;
  int x[4][2];

  for (int i = 0; i < 4; i++) {
    y = reference[i];
    wnovo[0] = (wanterior[0] + (bidimensional[i][0] * y));
    wnovo[1] = (wanterior[1] + (bidimensional[i][1] * y));
    bnovo = banterior + y;
    wanterior[0] = wnovo[0];
    wanterior[1] = wnovo[1];
    banterior = bnovo;
    }


  printf("Resultado  da aprendizagem\n");
  int output;
  for (int j = 0; j < 4 ; j++){
      int yliquid = (wnovo[0] * bidimensional[j][0]) + (wnovo[1] * bidimensional[j][1]) + bnovo;
      if (yliquid >= limiar){
         output = 1;}
      else{
         output = -1;}
      printf("%i ",output);
      };
   printf("\n");
   return 0;
};
