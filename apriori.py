import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

store_data = pd.read_csv('shopping_data.csv', header=None)


records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i,j]) for j in range(0, 20) if not str(store_data.values[i,j]) =='nan'] )


association_rules = apriori(records, min_support=0.002, min_confidence=0.5, min_lift=3, min_length=2)
association_results = list(association_rules)

print(len(association_results))

asso = []
for item in association_results:
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("=====================================")
    liste= []
    liste.append(items[0])
    liste.append(items[1])
    asso.append(liste)

print(asso)
file = open("clusters.txt" , "w+")

def chain(asso , prod_nbr , chains) :

    clusters =[]
    for i in range(0,len(asso)) :
        cluster=[]
        cluster.append(asso[i][0])
        cluster.append(asso[i][1])

        for j in range(i , len(asso)):
            if asso[j][0] in cluster and asso[j][1] not in cluster:
                cluster.append(asso[j][1])

            if asso[j][1] in cluster and asso[j][0] not in cluster:
                cluster.append(asso[j][0])          

            if len(cluster) > prod_nbr :
                break

        clusters.append(cluster)

        file.write("Cluster   " + str(len(clusters)) + ": \n")
        for prod in cluster :
            file.write(str(prod) +"___/___")

        file.write("\n \n") 
        if len(clusters) > chains :
            break


chain(asso , 5 , 6) 





    