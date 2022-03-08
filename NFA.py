import sys
def AFN(stare,cuvant):
    if not cuvant and stare in Final:            #daca cuvantul s-a terminat si a ajuns intr-o stare finala, cuvantul este acceptat
        global ok
        ok=1
    elif cuvant and ok==0:                         #altfel ma plimb prin noduri
        for x in L:
            if x[2] == cuvant[:1] and x[0] == stare:    #daca starea curenta are arc cu litera din cuvantul curent apelez recursiv functia
                AFN(x[1],cuvant[1:])


f=open("input.txt")
nrstari = f.readline().strip('\n')
starile = [int(y) for y in f.readline().split()]
# print(starile)
nrmuchii = f.readline().strip('\n')
# print(nrmuchii)
L=[]
for i in range (int(nrmuchii)):
    a,b,c = f.readline().split()      #citesc tranzitiile sub forma: din starea 1 merge in starea 2 cu litera a
    # print(a,b,c)
    # a=int(a)
    # b=int(b)
    L.append((a,b,c))
# print(L)
# L=[(line.split()[0],line.split()[1],line.split()[2]) for line in f.readlines()]
Initial = int(f.readline().strip('\n'))           # citesc starea initiala
# print(Initial)
nr_stari_finale = f.readline().strip('\n')      # citesc starile finale
Final = [x for x in f.readline().split()]
nrcuvinte = int(f.readline().strip('\n'))
cuv=[]   # citesc cuvantele ce trebuie verificate de automat
for i in range(int(nrcuvinte)):
     cuv.append(f.readline().strip('\n'))
#S = []
#S.append(Initial)
#stiva, lambda
f.close()
# sus=open("output.txt")
for cuvant in cuv:
    ok=0
    #ok = 1
    for x in L:
        if  x[2]==cuvant[:1]:
             #x.append(cuvant)
             #S.append(x[1])
             AFN(x[1],cuvant[1:])
             #S=S[:-1]
        elif cuvant == 'lambda' and Final.count(Initial) == 1:
            ok=1
    if ok==1:
        # sus=open('output.txt','w')
        # sus.write("Da")
        # sus.close()
        print("Da")
    else:
        # sus=open('output.txt','w')
        # sus.write("Nu")
        # sus.close()
        print("Nu")

#  #bbabaaa