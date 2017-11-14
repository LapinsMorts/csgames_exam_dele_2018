#include "fleur.h"

std::string Fleur::toString()
{
	return std::string("Vivante: ") + std::string(_vivante?"True":"False") + " Eau: " + std::to_string(_eau) +
		" Soleil: " + std::to_string(_soleil) + " Temperature Ideale: " +
		std::to_string(_temperatureIdeale) + " Prix: " + std::to_string(_prix);
}

int Fleur::getHydratation()
{
	return _eau;
}

int Fleur::getEnsoleillement()
{
	return _soleil;
}

int Fleur::getTempsSoleil()
{
	return _tempsSoleil;
}
