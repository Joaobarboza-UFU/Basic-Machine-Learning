#include <stdio.h>
#include <stdbool.h>

float bidimensional[14][2] = {{1.0, 1.0},{1.1, 1.5}, {2.5, 1.7},{1.0 , 2.0},{0.3, 1.4},{2.8, 1.0},{0.8, 1.5}, {2.5, 0.5}, {2.3, 1.0},{0.5, 1.1},{1.9, 1.3},{2.0,0.9},{0.5, 1.8},{2.1, 0.6}};
float wanterior[2] = {0, 0};
float wnovo[2] = {0.4997989 , 0.1696729};
float banterior = 0;
float bnovo = 0;
float alfa = 0.01;
float tabelaverdade[14] = {1 ,1 ,-1 ,1 ,1, -1 ,1 ,-1 ,-1 ,1 ,-1 ,-1 ,1 ,-1};
int cicle_counter = 0;
float yliquid;
float erro;

void weight_update(int input);
void liquid_calculator(int input1);
bool stop_condition();



int main(){

    while(!(stop_condition())){
        erro = 0;
        yliquid = 0;
        for(int i = 0 ; i < 14 ; i ++){
          liquid_calculator(i);
          weight_update(i);
        }
        printf("erro : %.15f \n" ,erro);
    }
}

void weight_update(int input){
    wnovo[0] = wanterior[0] + (alfa * (tabelaverdade[input] - yliquid) * bidimensional[input][0]);
    wnovo[1] = wanterior[1] + (alfa * (tabelaverdade[input] - yliquid) * bidimensional[input][1]);
    bnovo = banterior + (alfa * (tabelaverdade[input] - yliquid));
    banterior = bnovo;
    wanterior[0] = wnovo[0];
    wanterior[1] = wnovo[1];
}
void liquid_calculator(int input1){

    yliquid = (bidimensional[input1][0] * wanterior[0]) + (bidimensional[input1][1] * wanterior[1]);
    erro = erro + ((tabelaverdade[input1] - yliquid)*(tabelaverdade[input1] - yliquid));
}

bool stop_condition(){

    if (cicle_counter > 1000){
        return true;
    }
    else{
        cicle_counter = cicle_counter + 1;
        return false;
    }
}
