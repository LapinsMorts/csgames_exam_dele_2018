#ifndef MARGUERITE_H
#define MARGUERITE_H

#include "fleur.h"
#include <string>

class Marguerite: Fleur
{
	const std::string NOM = "Marguerite";
public:
	Marguerite(float prix);
	bool estEnVie(int temperature);
	void arroser(int secondes);
	void ensoleiller(float heures);
	void exister(int temperature);
	std::string toString();
};

#endif
