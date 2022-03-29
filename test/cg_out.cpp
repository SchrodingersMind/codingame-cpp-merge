/////////     File: main.cpp     /////////
#include <iostream>
/////////     File: base_import.h     /////////


class BaseStruct {
public:
    char* test = "String from base_import";
    int test2 = 10;
}
/////////     End: base_import.h     /////////


using namespace std;


int main() {
    cout << "Main Test" << endl;
    return 1;
}
/////////     End: main.cpp     /////////

/////////     File: base_import.cpp     /////////

/////////     End: base_import.cpp     /////////

