#ifndef FLEUR_H
#define FLEUR_H

#include <string>
#include "magasin.h"

class Fleur
{
protected:
	float _prix;
	std::string _couleur;
	int _eau;
	int _soleil;
	int _temperatureIdeale;
	bool _vivante;
	float _tempsSoleil;

public:
	virtual	bool estEnVie(int temperature);
	virtual void arroser(int secondes);
	virtual void ensoleiller(float heures);
	virtual void exister(int temperature);
	std::string toString();
	int getHydratation();
	int getEnsoleillement();
	int getTempsSoleil();
};

#endif
