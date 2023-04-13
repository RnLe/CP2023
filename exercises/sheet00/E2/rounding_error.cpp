#include <iostream>
#include <fstream>  // Only used to write a file to plot the data in python externally
#include <string>
// .hpps are used to organize the code
#include "a.hpp"
#include "b.hpp"
#include "c.hpp"

using namespace std;

// Only used to plot the data in python
void write_to_file(float* values, int steps, string filename) {
    // Open a file for writing
    std::ofstream outfile(filename);

    // Check if the file is opened successfully
    if (!outfile.is_open()) {
        std::cerr << "Error: Unable to open the output file." << std::endl;
        return;
    }

    // Write the array values to the file
    for (int i = 0; i < steps; i++) {
        outfile << values[i] << std::endl;
    }

    // Close the file
    outfile.close();

    return;
}

int main() {
    int steps = 1000;
    float* a = a_func(2e7, steps);  // 2e7 is a good value, because cancellation is happening right before reaching the limit
    float* a_stable = a_func_stable(2e37, steps);   // ~1.175e38 is the upper limit for floats

    for (int i = 0; i < steps; i++)
    {
        cout << a[i] << ", ";
    }

    cout << endl << "Stable calculation: " << endl;

    for (int i = 0; i < steps; i++)
    {
        cout << a_stable[i] << ", ";
    }

    write_to_file(a, steps, "a.txt");
    write_to_file(a_stable, steps, "a_stable.txt");
    
    delete[] a;
    delete[] a_stable;
    return 0;
}