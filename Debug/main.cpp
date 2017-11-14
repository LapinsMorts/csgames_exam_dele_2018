#include "magasin.h"
#include <string>
#include <iostream>

int main()
{
    std::cout << "Creation du magasin\n";
    Magasin* magasin = new Magasin(5,5);
    std::string temp;

    while(!magasin->estVide())
    {
        magasin->arroser();
        magasin->ensoleiller();
        magasin->nettoyer(20);
        magasin->exister(20);
        std::cout << magasin->allToString();
        std::cin.get();
    }
    delete(magasin);
}
