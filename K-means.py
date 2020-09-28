# K-means and K-means++ algorithms developed to iterate over the "Observações.txt" database
# João Barboza Rodrigues
# Computer Engineering student at Federal University of Uberlândia ( Brazil )
# 09-27-2020

from random import uniform
import math
import numpy as np
import matplotlib.pyplot as plt

centroides = (input("Qual o numero de centroides? \n"))

pontos = [] 
cluster_reference = []
centroides_lista = []
counter_master = 1000
stop_cond = 0
x_data = []
y_data = []
error = []


def fill_points_array():   
    f = open("observacoes.txt", "r")
    for line in f:
        split_line = line.strip()
        points_list = split_line.split()
        pontos.append(points_list)
        cluster_reference.append(0)
    f.close()
    
def gerador_centroide_aux():
    result = [uniform(-1.0, 10) , uniform(-1.0, 10)]
    return result

def gerador_centroide():
    for i in range(int(centroides)):
        centroides_lista.append(gerador_centroide_aux())
        
def calculo_cluster():
    for i in range(len(pontos)):
        reference = 100
        for j in range(len(centroides_lista)):
            if(reference > math.sqrt(((float(pontos[i][0]) - float(centroides_lista[j][0])) ** 2) + ((float(pontos[i][1]) - float(centroides_lista[j][1])) ** 2))):
                reference = math.sqrt(((float(pontos[i][0]) - float(centroides_lista[j][0])) ** 2) + ((float(pontos[i][1]) - float(centroides_lista[j][1])) ** 2))
                cluster_reference[i] = j + 1
            
def centroide_nova():
    global stop_cond
    for i in range(int(centroides)):
        valor_medio = [0 , 0 , 0]
        for j in range(len(pontos)):
            referencia = [float(centroides_lista[i][0]) , float(centroides_lista[i][1])]
            if(cluster_reference[j] == i + 1):
                valor_medio[0] = valor_medio[0] + float(pontos[j][0])
                valor_medio[1] = valor_medio[1] + float(pontos[j][1])
                valor_medio[2] = valor_medio[2] + 1
        if(valor_medio[2] > 0):
            centroides_lista[i][0] = valor_medio[0] / valor_medio[2]
            centroides_lista[i][1] = valor_medio[1] / valor_medio[2]
            if((float(centroides_lista[i][0]) == referencia[0] ) and (float(centroides_lista[i][1]) == referencia[1] )):
                stop_cond = stop_cond + 1
        
def plot_points():
    
    x = []
    y = []
    z = []
    color = ['red', 'green' , 'blue', 'orange' , 'black' , 'yellow' , 'purple' , 'pink']
    for i in range(len(pontos)):
        x.append(float(pontos[i][0]))
        y.append(float(pontos[i][1]))
        z.append(color[int(cluster_reference[i])- 1])
    plt.scatter(x, y, c=z)
    plt.show()

def k_means():
    global stop_cond
    list_master = []
    bool_operator = 0
    count = 0
    fill_points_array()
    gerador_centroide()
    while(bool_operator == 0):
        calculo_cluster()
        centroide_nova()
        error_calc()
        count = count + 1
        if((stop_cond == int(centroides)) or (count == counter_master)):
            bool_operator = 1
        stop_cond = 0

def plot_error():
    y = []
    for i in range(len(error)):
        y.append(i)
    plt.scatter(error,y)
    plt.show()
    
def error_calc():
    erro = 0
    for i in range(len(pontos)):
        x = math.sqrt(((float(pontos[i][0]) - float(centroides_lista[int(cluster_reference[i]) - 1][0])) ** 2) + ((float(pontos[i][1]) - float(centroides_lista[int(cluster_reference[i]) - 1][1])) ** 2))
        erro = erro + (x ** 2)
    error.append(erro)
        
        
    
k_means()
plot_points()
plot_error()

