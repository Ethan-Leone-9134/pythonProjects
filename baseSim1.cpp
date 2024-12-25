#include <iostream>
#include <cmath>
#include <vector>

// Define Constants
const double Msun = 2e30;
const double AU = 1.5e11;
const double G = 6.674e-11;
int scene = 888;
int Ymax = 10000;         // Maximum year
int calPDay = 1;          // Loop iterations per sim day
double dt = 60 * 60 * 24 / calPDay;  // Time Per iteration
double day = 0;            // Starting Date
int numBodies = 3;
std::vector<std::vector<int>> cobos;
std::vector<std::vector<double>> NewtVect;

// Function Declarations
double gravForce(double m1, double m2, double d);
std::vector<double> orbiter(std::vector<double>& BodyVector, double An, std::vector<double>& CM, double dt);
std::vector<double> centMass(double m1, double m2, std::vector<double>& BV1, std::vector<double>& BV2);
std::vector<double> centMassMult(std::vector<double>& mass, std::vector<std::vector<double>>& Newtonian);




int main() {
    // Your main function logic here

    // Generate Combinations
    for (int i = 1; i <= numBodies; ++i) {
        for (int j = i + 1; j <= numBodies; ++j) {
            cobos.push_back({i, j});
        }
    }
    int numCombos = cobos.size();    // Number of combinations

    //      Year Check         
    while (day<=Ymax*365) {
      day = (day + 1/calPDay);
      for (int n = 0; n < numCombos; ++n) {
          int v1 = cobos[n][0];
          int v2 = cobos[n][1];
      }
    }


    return 0;
}

// Function Definitions
double gravForce(double m1, double m2, double d) {
    return G * m1 * m2 / (d * d);
}

std::vector<double> orbiter(std::vector<double>& BodyVector, double An, std::vector<double>& CM, double dt) {
    double phi = atan2(BodyVector[1] - CM[1], BodyVector[0] - CM[0]);
    double Ax = cos(phi) * An;
    double Ay = sin(phi) * An;

    BodyVector[2] += Ax * dt;
    BodyVector[3] += Ay * dt;

    return BodyVector;
}

std::vector<double> centMass(double m1, double m2, std::vector<double>& BV1, std::vector<double>& BV2) {
    double x = (m1 * BV1[0] + m2 * BV2[0]) / (m1 + m2);
    double y = (m1 * BV1[1] + m2 * BV2[1]) / (m1 + m2);
    return {x, y};
}

std::vector<double> centMassMult(std::vector<double>& mass, std::vector<std::vector<double>>& Newtonian) {
    double x = 0, y = 0;
    double totalMass = 0;

    for (size_t i = 0; i < mass.size(); ++i) {
        x += mass[i] * Newtonian[i][0];
        y += mass[i] * Newtonian[i][1];
        totalMass += mass[i];
    }

    return {x / totalMass, y / totalMass};
}
