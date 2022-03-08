#include <vector>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;
ifstream f("input.txt");
ofstream g("output.txt");
int i,j,k,nrstarifinale,nrstariinitiale,nrCuv,x,y,nrF,S;
char l;
vector <pair<int,char>>vec[1000001];
string cuvinte;
int starifinale[10000001];
int talent(string &cuvinte,int curent,int starifinale[],int nrF)
{
    int actual=0,lex = cuvinte.size();
    while(actual<lex)
    {
        char lera = cuvinte[actual];
        bool lera_ap = 0;
        for(int i=0; i<vec[curent].size(); i++)
        {
            if(vec[curent][i].second == lera)
            {
                lera_ap = 1;
                curent = vec[curent][i].first;
                break;
            }
        }
        if(lera_ap == 0)
            return 0;
        actual = actual + 1;
    }

    for(i=0; i<nrF; i++)
    {
        if(curent == starifinale[i])
            return 1;
    }
    return 0;

}
int main()
{
    int N;
    f>>N;
    vector <int> stari(N);
    for(int i=0; i<N; i++)
    {
        f>>stari[i];
    }
    int M;
    f>>M;
    for(int i=0; i<M; i++)
    {
        f>>x>>y>>l;
        vec[x].push_back(make_pair(y,l));
    }
    f>>S;
    f>>nrF;
    vector <int> stariinitiale;
    for(int i=0; i<nrF; i++)
    {
        f>>starifinale[i];
    }
    f>>nrCuv;
    for(int i=0; i<nrCuv; i++)
    {
        f>>cuvinte;
        if(talent(cuvinte,S,starifinale,nrF))
            g<<"DA"<<endl;
        else
            g<<"NU"<<endl;
    }
    return 0;
}
