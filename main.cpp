#include <vector>
#include <iostream>
#include <fstream>
#include <cmath>
//#include <bits/stdc++.h>
using namespace std;
ifstream f("input.txt");      // facem fisierele din care urmeaza sa citim / afisam
ofstream g("output.txt");
int i,j,k,nrstarifinale,nrstariinitiale,nrCuv,x,y,nrF,S;
char l;                                                // declaram variabilele
vector <pair<int,char>>vec[1000001];                   // facem pereche de tip ( nod 2 , litera ) pentru a verifica mai usor starea curenta
string cuvinte;
int starifinale[10000001];                        // vectori de stari finale
int talent(string &cuvinte,int curent,int starifinale[],int nrF)                        // subprogramul de dfa care returneaza 1 pt cuv acc / 0 daca nu
{
    int actual=0,lex = cuvinte.size();                                // bfs modificat (luam actual(0 care merge pana la nr de litere din cuvant))
    while(actual<lex)                         // lex reprezinta nr de litere din cuvantul pe care trebuie sa-l modificam
    {
        char litera = cuvinte[actual];                  // retinem in variabila litera ... litera pe care ne aflam
        bool litera_ap = 0;                     //litera_ap verifica daca avem litera respectiva pe muchie (daca putem sa avansam cu verificarea cuv.)
        for(int i=0; i<vec[curent].size(); i++)
        {
            if(vec[curent][i].second == litera)                      //pe vec[][].second se afla litera din perechea facuta anterior (y,litera)
            {
                litera_ap = 1;                                      //ok = 1 daca litera este aceeasi
                curent = vec[curent][i].first;          //retinem starea (pe first avem y)
                break;
            }
        }
        if(litera_ap == 0)          //daca ok = 0 atunci returnam 0
            return 0;
        actual = actual + 1;                  // crestem actual pentru a verifica urmatoarea litera
    }

    for(i=0; i<nrF; i++)
    {
        if(curent == starifinale[i])          // verificam daca ajungem cu st initiala in starea finala ( luam toate starile finale si le verificam )
            return 1;
    }
    return 0;                           //daca nu returnam 0 (nu se accepta cuv)

}
int main()
{
    int N;             //int numarul de stari + citire
    f>>N;
    vector <int> stari(N);      //citire normala (vector) , n ( nr stari ) + starile
    for(int i=0; i<N; i++)
    {
        f>>stari[i];                     //citim starile (ex. 1 2 3 4 5...)
    }
    int M;                                            //M este nr de tranzitii
    f>>M;
    for(int i=0; i<M; i++)
    {
        f>>x>>y>>l;              //citim muchia 1 muchia 2 ( in care trebuie sa facem tranzitia ) si litera de pe muchie prin care facem tranzitia
        vec[x].push_back(make_pair(y,l));                        //construim perechile de tipul (y,litera)
    }
    f>>S;
    f>>nrF;
    vector <int> stariinitiale;                      //citim starea initiala , nr de stari finale + construim vec de stari initiale si vec de stari finale(mai sus)
    for(int i=0; i<nrF; i++)
    {
        f>>starifinale[i];
    }
    f>>nrCuv;
    for(int i=0; i<nrCuv; i++)                                      // citim nr de cuvinte + cuvintele
    {
        f>>cuvinte;
        if(talent(cuvinte,S,starifinale,nrF))                   // apelam functia de bfs pentru a verifica cuv
            g<<"DA"<<endl;                    //daca cuv este acceptat de dfa atunci afisam mesajul da
        else
            g<<"NU"<<endl;                    //daca cuv nu este acceptat de dfa atunci afisam mesajul nu
    }
    return 0;
}
