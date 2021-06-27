
#include <iostream>

#include "mapa_interwalow.h"


void print_mapa_interwalow(mapa_interwalow m) {
    for (const auto& interwal : m.map_) {
        std::cout << interwal.first << ": " << interwal.second << std::endl;
    }
}

void print_sprawdz_wartosc(mapa_interwalow m, int v) {
    std::cout << "sprawdz_wartosc " << v << " -> " << m.sprawdz_wartosc(v) << std::endl;
}

int main()
{
   // try{
        mapa_interwalow mi('A');

        mi.powiaz_interwal(3, 'B');
        mi.powiaz_interwal(5, 'A');
        //mi.print(0, 10);
        print_sprawdz_wartosc(mi, 4);
        print_sprawdz_wartosc(mi, 5);
        print_sprawdz_wartosc(mi, 50);
        print_mapa_interwalow(mi);
        

        mi.powiaz_interwal(2, 4, 'B');
        //mi.print(0, 10);
        print_sprawdz_wartosc(mi, 3);
        print_sprawdz_wartosc(mi, 4);
        print_sprawdz_wartosc(mi, 5);
        print_mapa_interwalow(mi);

  //  } catch(const char* c) {
    //    std::cerr << c <<std::endl;
   //     return 1;
   // }
    

}
