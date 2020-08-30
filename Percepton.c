#include <stdio.h>
#include <stdbool.h>

float bidimensional[14][2] = {{1.0, 1.0},{1.1, 1.5}, {2.5, 1.7},{1.0 , 2.0},{0.3, 1.4},{2.8, 1.0},{0.8, 1.5}, {2.5, 0.5}, {2.3, 1.0},{0.5, 1.1},{1.9, 1.3},{2.0,0.9},{0.5, 1.8},{2.1, 0.6}};
float wanterior[2] = {0, 0};
float wnovo[2] = {0, 0};
float banterior = 0;
float bnovo = 0;
float alfa = 1;
int tabelaverdade[14] = {1 ,1 ,-1 ,1 ,1, -1 ,1 ,-1 ,-1 ,1 ,-1 ,-1 ,1 ,-1};
int limiar = 0;
int result;
bool counter = true;
float y = 0;
float x[4][2];

void pair_manipulation(int input);
void iteracao ();
void print_results();

int main()
{
  float pesoreferencia1 = wnovo[0];
  float pesoreferencia2 = wnovo[1];

  iteracao ();

  while((pesoreferencia1 != wnovo[0]) || (pesoreferencia2 != wnovo[1])){
       pesoreferencia1 = wnovo[0];
       pesoreferencia2 = wnovo[1];
       iteracao ();
   }
  print_results();

}

void iteracao (){

    for (int j = 0; j < 14; j++){

        counter = true;

        while(counter){
            counter = false;
            pair_manipulation(j);
        }
   }

}

void print_results(){
    for(int i = 0; i < 14 ; i++){

        float learning_Result = bnovo;
        int exp_result = tabelaverdade[i];

        for (int j = 0 ; j < 2 ; j++){
            learning_Result = learning_Result + (bidimensional[i][j] * wnovo[j]);
        }

        if (learning_Result < 0){
            learning_Result = -1;
        }
        else{
            learning_Result = 1;
        }

        printf("Expected result %i is % i , learning obtained %.1f\n ", i + 1 , exp_result , learning_Result);
    }
    printf(" W[0] = %.3f e W[1] = %.3f \n" , wnovo[0] , wnovo[1]);
}

void pair_manipulation(int input){

    y = bnovo + (bidimensional[input][0] * wnovo[0]) + (bidimensional[input][1] * wnovo[1]);

    if(y < 0){
      result = -1;
    }
    else{
      result = 1;
    }

    if(result != tabelaverdade[input]){
      wnovo[0] = wnovo[0] + (alfa * tabelaverdade[input] * bidimensional[input][0]);
      wnovo[1] = wnovo[1] + (alfa * tabelaverdade[input] * bidimensional[input][1]);
      bnovo = bnovo + (alfa *  tabelaverdade[input]);
      counter = true;
    }
}
