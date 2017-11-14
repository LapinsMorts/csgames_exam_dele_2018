#include "marguerite.h"

Marguerite::Marguerite(float prix)
{
	_prix = prix;
	_couleur = "Blanc et Jaune";
	_eau = 100;
	_soleil = 100;
	_temperatureIdeale = 0;
	_vivante = true;
}

bool Marguerite::estEnVie(int temperature)
{
	bool eauOK = _eau > 0 && _eau <= 100;
	bool soleilOK = _soleil > 0 && _soleil <= 100;
	bool temperatureOK = temperature >= _temperatureIdeale - 15 &&
		temperature <= _temperatureIdeale + 15;
	_vivante = _vivante && eauOK && soleilOK && temperatureOK;
	return 	_vivante;
}

void Marguerite::arroser(int seconde)
{
	_eau += seconde * 5;
}

void Marguerite::ensoleiller(float heures)
{
	_tempsSoleil = heures;
}

void Marguerite::exister(int temperature)
{
	_eau -= 8;
	if(_tempsSoleil <= 0)
		_soleil -= 4;
	else
	{
		_soleil += 6;
		_tempsSoleil -= 1;
	}
	estEnVie(temperature);
}

std::string Marguerite::toString()
{
	return std::string("Nom: ") + NOM + " " + Fleur::toString();
}
