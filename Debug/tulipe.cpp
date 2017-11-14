#include "tulipe.h"

Tulipe::Tulipe(float prix, std::string couleur)
{
	_prix = prix;
	_couleur = couleur;
	_eau = 100;
	_soleil = 100;
	_temperatureIdeale = 25;
	_vivante = true;
}

bool Tulipe::estEnVie(int temperature)
{
	bool eauOK = _eau > 0 && _eau <= 100;
	bool soleilOK = _soleil > 0 && _soleil <= 100;
	bool temperatureOK = temperature >= _temperatureIdeale - 10 &&
		temperature <= _temperatureIdeale + 10;
	_vivante = _vivante && eauOK && soleilOK && temperatureOK;
	return _vivante;
}

void Tulipe::arroser(int seconde)
{
	_eau += seconde * 2;
}

void Tulipe::ensoleiller(float heures)
{
	_tempsSoleil = heures;
}

void Tulipe::exister(int temperature)
{
	_eau -= 17;
	if(_tempsSoleil <= 0)
		_soleil -= 10;
	else
	{
		_soleil += 3;
		_tempsSoleil -= 1;
	}
	estEnVie(temperature);
}

std::string Tulipe::toString()
{
	return std::string("Nom: ") + NOM + " " + Fleur::toString();
}
