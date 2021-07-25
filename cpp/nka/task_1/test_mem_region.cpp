/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

/*****************
 * Least Recently Used
 * Najdawniej u¿ywany region jest zastêpowany w przypadku nie znalezienia szukanego regionu
 *
 * find(10) -> 10 -1 -1 -1 -1
 * find(11) -> 10 11 -1 -1 -1
 * find(12) -> 10 11 12 -1 -1
 * find(13) -> 10 11 12 13 -1
 * find(14) -> 10 11 12 13 14
 *
 * find(10) -> 10 11 12 13 14
 *
 * find(50) -> 10 50 12 13 14
*/

struct MemoryRegion
{
    int num = -1;
    int order = 0;
};

MemoryRegion regions[5];

MemoryRegion* find(int memory_region_id)
{
    int order_max = 0, idx_order_max = 0, idx = 0;
    bool is_found_not_initialised = false;

    // UNTIL TABLE IS FULLY INITED
    for (idx = 0; idx < (int)(sizeof(regions) / sizeof(regions[0])); idx++) {
        if (-1 == regions[idx].num) {
            regions[idx].num = memory_region_id;
            regions[idx].order = 0;
            is_found_not_initialised = true;
            break;
        }
        else {
            if (order_max < regions[idx].order) {
                order_max = regions[idx].order;
                idx_order_max = idx;
            }
            regions[idx].order++; // increase order of all elements
        }
    }

    if (false == is_found_not_initialised) {    //else was entered all the time
        regions[idx_order_max].num = memory_region_id;
        regions[idx_order_max].order = 0;       // push to beginning
    }

    return regions;
}

void print_regions()
{
    for (int idx = 0; idx < (int)(sizeof(regions) / sizeof(regions[0])); idx++)
        cout << "element: " << regions[idx].num << " order: " << regions[idx].order << endl;

    cout << endl;
}


int main()
{
    find(10);
    print_regions();
    find(11);
    print_regions();
    find(12);
    print_regions();
    find(13);
    print_regions();
    find(14);
    print_regions();
    find(10);
    print_regions();
    find(50);
    print_regions();

    return 0;
}


