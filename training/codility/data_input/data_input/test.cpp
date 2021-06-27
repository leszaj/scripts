

#include "data_input.h"
#include <iostream>
#include <string>


int main() {
    string line;
    bool is_data_collected = false;

    while (getline(cin, line)) {
        if (line.empty()) break;
        decode_data_int(line);
        cout << line << endl;
    }

    cout << data_int[0][0] << endl; cout << data_int[0][1] << endl;
}