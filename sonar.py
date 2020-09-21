# Developed by João Barboza Rodrigues
# Computer engineering student at Federal University of Uberlândia , Brazil
# 09/19/2020
# Machine learning implementation used to analise the output of a sonar
# https://www.linkedin.com/in/jo%C3%A3o-barboza-a8b8a2195/

from random import uniform
import math

#initial values
alfa = 0.01 # taxa de aprendizagem
numero_ciclos = 4500 # numero de ciclos previstos
ciclos_executados = 0 # numero de ciclos executados 
camada_escondida = 20 # numero de neuronios da camada escondida
entrada = 60 # numero de dados de entrada
saida = 1 # numero de neuronios de saida
training = open("trainingset", "r")

testingset = open("testingset","r")
#initial variables
entrada_valores = []
saida_valores = []
tabela_entrada = []
teste_entrada = []
teste_saida = []
tabela_verdade = 0
weights_hidden_layer = []
weights_final_layer = []
bias_hidden_layer = []
bias_final_layer = []
z_final = []
delta_w = []
delta_h = []
delta_bias_final = []
delta_bias_hidden = []
z_ink_deriv = []
deltinha_j = []
y_ink_deriv = 0
deltinha_k = 0
y_final = 0

#inicia listas
for i in range(60):
    tabela_entrada.append(0)
for i in range(camada_escondida):
    z_ink_deriv.append(0)
    z_final.append(0)
    deltinha_j.append(0)
    delta_bias_hidden.append(0)
for i in range(saida):
    delta_bias_final.append(0)
for i in range (saida):
    aux = []
    for j in range (camada_escondida):
        aux.append(0)
    delta_w.append(aux)    
for i in range(camada_escondida):
    aux = []
    for j in range(entrada):
        aux.append(0)
    delta_h.append(aux)

#generates randon values between -0.5 and 0.5
def initial_weight_gen():
    result = uniform(-0.5, 0.5)
    return result


def read_input_values():
    for line in training:
        floats =[]
        res =[]
        line1= line[:(len(line)-3)]
        numbers=line1.split(",")
        if (len(numbers)>1):
            for number in numbers:
                floats.append(float(number))
            if(len(floats)!=0):
                entrada_valores.append(floats)
        line2= line[len(line)-2:len(line)-1]
        if(line2=='M'):
            saida_valores.append(1.0)
        elif(line2 =='R'):
            saida_valores.append(-1.0)

def func_activ(x):
    result = (2/(1+math.exp(-x)))-1
    return result

def func_deriv(x):
    x = func_activ(x)
    result = 0.5*(1+x)*(1-x)
    return result

def init_weights():
    for i in range (camada_escondida):
        layer_weights = []
        bias_hidden_layer.append(initial_weight_gen())
        for k in range (entrada):
            layer_weights.append(initial_weight_gen())
        weights_hidden_layer.append(layer_weights)
    for k in range (saida):
        bias_final_layer.append(initial_weight_gen())
        for j in range (camada_escondida):
            layer_weights.append(initial_weight_gen())
        weights_final_layer.append(layer_weights)            
        

#responsavel por chamar as outras funcoes auxiliares pora gerir o aprendizado
def training_master():
    global ciclos_executados, y_final , tabela_verdade
    while stop_condition():
        erroQ=0
        for i in range (129):
            tabela_verdade = saida_valores[i]
            for j in range (60):
                tabela_entrada[j] = entrada_valores[i][j]
            training_pair()
        ciclos_executados = ciclos_executados + 1
        erroQ = erroQ + 0.5*((saida_valores[i]-y_final)*(saida_valores[i]-y_final))
        print("Ciclo Atual:" + str(ciclos_executados) + " Erro quadratico:" + str(erroQ) +"\n")

#Utilizada para checar se as condicoes de parada já foram satisfeitas
def stop_condition():
    if ciclos_executados < numero_ciclos : 
        return True
    else:
        return False

#utilizada para realizadar a aprendizagem para um conjunto de 60 entradas e uma saida atualizando os pesos após aaprendizagem 
def training_pair():
    feed_forward()
    retro_propagation()
    weight_update()


#realiza a alimentação da camada de saída antes da retropropagação do erro
def feed_forward():
    feed_forward_hidden_layer()
    feed_forward_out_layer()

#uses the input array to determine the output
def feed_forward_hidden_layer():
    for x in range (camada_escondida):
        sum_i = bias_hidden_layer[x]
        for i in range (entrada):
            sum_i = sum_i +  weights_hidden_layer[x][i] * tabela_entrada[i]
        z_ink_deriv[x] = func_deriv(sum_i)
        z_final[x] = func_activ(sum_i)
    return z_final , z_ink_deriv
        
#uses the output of feed_forward_hidden_layer() as reference
def feed_forward_out_layer():
    global y_final , y_ink_deriv
    for k in range (saida):
        sum_k = bias_final_layer[k]
        for i in range (camada_escondida):
            sum_k = sum_k + weights_final_layer[k][i] * z_final[i]
        y_ink_deriv = func_deriv(sum_k)
        y_final = func_activ(sum_k)
    return y_ink_deriv , y_final


#Calculas os deltas necessarios para a atualizacao dos pesos da camada de saida e camada escondida
def retro_propagation():
    retro_propagation_out_layer()
    retro_propagation_hidden_layer()


def retro_propagation_out_layer():
    global y_final , delta_w , deltinha_k
    for i in range (saida):
        deltinha_k = (tabela_verdade - y_final) * y_ink_deriv
        delta_bias_final[i] = alfa * deltinha_k
        for j in range (camada_escondida):
            delta_w[i][j] = alfa * deltinha_k * z_final[j]
    return delta_w , deltinha_k
            
            

def retro_propagation_hidden_layer():
    for i in range (camada_escondida):
        deltinha_i = deltinha_k * weights_final_layer[0][i]
        deltinha_j[i] = deltinha_i * z_ink_deriv[i]
        delta_bias_hidden[i] = alfa * deltinha_j[i]
        for j in range (entrada):
            delta_h[i][j] = alfa * deltinha_j[i] * tabela_entrada[j]

#atualiza os pesos com base nos deltas obtidos

def weight_update():
    for i in range(saida):
        bias_final_layer[i] = bias_final_layer[i] + delta_bias_final[i] 
        for j in range(camada_escondida):
            weights_final_layer[i][j] = weights_final_layer[i][j] + delta_w[i][j]
    for i in range(camada_escondida):
        bias_hidden_layer[i] = bias_hidden_layer[i] + delta_bias_hidden[i] 
        for j in range(entrada):
            weights_hidden_layer[i][j] = weights_hidden_layer[i][j] + delta_h[i][j]
    return  bias_final_layer , weights_final_layer , bias_hidden_layer , weights_hidden_layer

def read_training():
    for line in testingset:
        floats =[]
        res =[]
        line1= line[:(len(line)-3)]
        numbers=line1.split(",")
        if (len(numbers)>1):
            for number in numbers:
                floats.append(float(number))
            if(len(floats)!=0):
                teste_entrada.append(floats)
        line2= line[len(line)-2:len(line)-1]
        if(line2=='M'):
            teste_saida.append(1.0)
        elif(line2 =='R'):
            teste_saida.append(-1.0)





init_weights()
read_input_values()
training_master()
read_training()
acertos=0
for u in range(len(teste_entrada)):
    for x in range (camada_escondida):
        sum_i = bias_hidden_layer[x]
        for i in range (entrada):
            sum_i = sum_i +  weights_hidden_layer[x][i] * teste_entrada[u][i]
        z_ink_deriv[x] = func_deriv(sum_i)
        z_final[x] = func_activ(sum_i)
    for k in range (saida):
        sum_k = bias_final_layer[k]
        for i in range (camada_escondida):
            sum_k = sum_k + weights_final_layer[k][i] * z_final[i]
        y_ink_deriv = func_deriv(sum_k)
        y_final = func_activ(sum_k)
    print("Target: " + str(saida_valores[u]) +"   Rede Treinada: " + str(y_final))
    if ((saida_valores[u]-y_final)<0.1):
        print("[PASSED]")
        acertos=acertos+1
    else:
        print("[FAIL]")

print("\n\nTAXA DE ACERTO: " + str(acertos) +"/"+ str(len(teste_entrada)))
