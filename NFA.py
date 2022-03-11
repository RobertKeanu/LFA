import sys
def AFN(stare,cuvant):
    if not cuvant and stare in Final:            #daca cuvantul s-a terminat si a ajuns intr-o stare finala, cuvantul este acceptat
        global ok
        ok=1
    elif cuvant and ok==0:                         #altfel ma plimb prin noduri
        for x in L:
            if x[2] == cuvant[:1] and x[0] == stare:    #daca starea curenta are arc cu litera din cuvantul curent apelez recursiv functia
                AFN(x[1],cuvant[1:])


f=open("input.txt")           #deschidem fisierul
nrstari = f.readline().strip('\n')
starile = [int(y) for y in f.readline().split()]            #citire date
# print(starile)
nrmuchii = f.readline().strip('\n')
# print(nrmuchii)
L=[]                                 #lista initial goala in care urmeaza sa punem perechiile de tranzitii (x,y,litera)
for i in range(int(nrmuchii)):
    a,b,c = f.readline().split()      #citesc tranzitiile sub forma: din starea 1 merge in starea 2 cu litera a
    # print(a,b,c)
    a=int(a)
    b=int(b)                    #daca fac int(a,b) nu mai merge ... dc?
    L.append((a,b,c))
# print(L)
# L=[(line.split()[0],line.split()[1],line.split()[2]) for line in f.readlines()]
Initial = int(f.readline().strip('\n'))           # citesc starea initiala
# print(Initial)
nr_stari_finale = int(f.readline().strip('\n') )     # citesc starile finale
Final = [int(x) for x in f.readline().split()]        #Final este lista cu starile finale
nrcuvinte = int(f.readline().strip('\n'))         #numar cuvinte
cuv=[]   # citesc cuvantele ce trebuie verificate de automat
for i in range(int(nrcuvinte)):
     cuv.append(f.readline().strip('\n'))      #cuv este lista in care punem cuvintele ce urmeaza a fi verificate de nfa
#S = []
#S.append(Initial)
#stiva, lambda
f.close()          #inchidem fisierul
# sus=open("output.txt")
for cuvant in cuv:                        #citim mai sus nr de cuvinte si parcurgem apoi cuvintele verificand daca ok ajunge sa fie 1
    ok=0             #pt fiecare cuvant presupunem la inceput ca nu este acceptat de automat
    #ok = 1
    for x in L:             #parcurgem cu un x lista in care avem tranzitiile de genul [x,y,litera]
        if  x[2]==cuvant[:1]:                          #verificam daca avem muchie cu litera din cuvantul nostru pe care o verificam
             #x.append(cuvant)
             #S.append(x[1])                            #verificam care sunt starile
             #print(S)
             AFN(x[1],cuvant[1:])                       #apelam functia AFN (din starea curenta in care ne aflam si cuvantul actual(literele))
             #S=S[:-1]
        elif cuvant == 'lambda' and Final.count(Initial) == 1:    #***optional*** verificam daca cuvantul este lambda + are o singura stare atunci starea initiala este si finala si rezulta automat ca ok devine 1
            ok=1
    if ok==1:                                            #daca ok este 1 atunci afisam mesajul da altfel nu
        # sus=open('output.txt','w')
        # sus.write("Da")
        # sus.close()
        print("Da")                                          #afisam da pt ok 1
    else:
        # sus=open('output.txt','w')
        # sus.write("Nu")                                 #cod pentru afisarea in fisier pe care am uitat sa-l scot din comentariu cand am trimis tema :(
        # sus.close()
        print("Nu")               #afisam nu pt ok 0

#  #bbabaaa ex de cuvant
