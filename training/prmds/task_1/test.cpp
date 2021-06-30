
#include <iostream>
#include "lamana.h"


int main()
{
	Punkt pkt;
	std::vector<Punkt> test_in; 
	std::vector<Punkt> test_out;
	

	for (int i=0; i<10; i++)
	{
		pkt.x = rand() % 100; 
		pkt.y = rand() % 100;
		test_in.push_back(pkt);
	}
	
	test_out = lamana(test_in);
	
	std::cout << "test_in  : ";
	for (const Punkt& i : test_in) {	// const zeby nie kopiowac zawartosci za kazda petla
		std::cout << "(" << i.x << "," << i.y << ") ";
	}
	std::cout << std::endl;

	std::cout << "test_out : ";
	for (const Punkt& i : test_out) {	// const zeby nie kopiowac zawartosci za kazda petla
		std::cout << "(" << i.x << "," << i.y << ") ";
	}
	std::cout << std::endl;
}