#include "magasin.h"


Magasin::Magasin(int nbTulipes, int nbMarguerites)
{
    _nbFleurs = 0;
    for(int i = 0; i < nbTulipes; ++i)
        _fleurs[++_nbFleurs] = new Tulipe(12.50, "Rouge");

    for(int i = 0; i < nbMarguerites; ++i)
        _fleurs[++_nbFleurs] = new Marguerite(10.00);

}

void Magasin::addTulipe(float prix, std::string couleur)
{
    _fleurs[++_nbFleurs] = new Tulipe(prix, couleur);
}

void Magasin::addMarguerite(float prix)
{
    _fleurs[++_nbFleurs] = new Marguerite(prix);
}

void Magasin::nettoyer(int temperature)
{
    for(int i = 0; i < _nbFleurs; ++i)
    {
        if(!_fleurs[i]->estEnVie(temperature))
        {
            _fleurs[i] = _fleurs[_nbFleurs - 1];
            --i;
            --_nbFleurs;
        }
    }
}

void Magasin::arroser()
{
    for(int i = 0; i < _nbFleurs; ++i)
    {
        if(typeid(*_fleurs[i]).name() == "6Tulipe")
            _fleurs[i]->arroser((100-_fleurs[i]->getHydratation())/2.0);
        else
            _fleurs[i]->arroser((100-_fleurs[i]->getHydratation())/5.0);
    }
}

void Magasin::ensoleiller()
{
    for(int i = 0; i < _nbFleurs; ++i)
    {
        if(!_fleurs[i]->getTempsSoleil() > 0)
            if(typeid(*_fleurs[i]).name() == "6Tulipe")
                _fleurs[i]->ensoleiller((100-_fleurs[i]->getEnsoleillement())/3.0);
            else
                _fleurs[i]->ensoleiller((100-_fleurs[i]->getEnsoleillement())/6.0);
    }
}

std::string Magasin::allToString()
{
    std::string a = "";
    for(int i = 0; i < _nbFleurs; ++i)
        a += _fleurs[i]->toString() + "\n";
    return a;
}

bool Magasin::estVide()
{
    return _nbFleurs > 0;
}

void Magasin::exister(int temperature)
{
    for(int i = 0; i < _nbFleurs; ++i)
        _fleurs[i]->exister(temperature);
}

Magasin::~Magasin()
{
    for(int i = 0; i < _nbFleurs; ++i)
        delete(_fleurs[i]);
}
