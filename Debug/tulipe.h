#ifndef TULIPE_H
#define TULIPE_H

#include "fleur.h"
#include <string>

class Tulipe: Fleur
{
	const std::string NOM = "Tulipe";
public:
	Tulipe(float prix, std::string couleur);
	bool estEnVie(int temperature);
	void arroser(int secondes);
	void ensoleiller(float heures);
	void exister(int temperature);
	int getHydratation();
	std::string toString();
};

#endif
