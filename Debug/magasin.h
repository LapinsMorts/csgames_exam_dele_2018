#ifndef MAGASIN_H
#define MAGASIN_H

#include <string>
#include <math.h>
#include <typeinfo>
#include "fleur.h"
#include "marguerite.h"
#include "tulipe.h"

class Magasin
{
	Fleur* _fleurs[10];
    int _nbFleurs;
public:
    const int CAPACITE = 15;
	Magasin(int nbTulipes, int nbMarguerites);
    ~Magasin();
    void addTulipe(float prix, std::string couleur);
    void addMarguerite(float prix);
    void nettoyer(int temperature);
    void arroser();
    void ensoleiller();
    std::string allToString();
    void exister(int temperature);
    bool estVide();
};

#endif
