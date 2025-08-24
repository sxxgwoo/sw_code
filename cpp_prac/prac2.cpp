/*
=============================================
   Problem: Vehicle Hierarchy Design
=============================================

Design and implement the following class hierarchy in C++ using OOP principles.

1) Vehicle (Abstract Base Class)
   - Declare start() as a pure virtual function.
   - Define a virtual destructor.

2) Car (Car Vehicle)
   - Inherit from Vehicle using protected virtual inheritance.
   - Constructor should take fuelEfficiency (km per liter) as an argument.
   - Override start() to print:
       "Car started."
   - Add computeFuelNeeded(double distance) function that returns:
       distance / fuelEfficiency

3) Bike (Bike Vehicle)
   - Inherit from Vehicle using public virtual inheritance.
   - Constructor should take energyEfficiency (km per kWh) as an argument.
   - Override start() to print:
       "Bike started."
   - Add computeEnergyNeeded(double distance) function that returns:
       distance / energyEfficiency

4) HybridVehicle (Combination of Car + Bike)
   - Inherit from both Car and Bike (multiple inheritance).
   - Constructor should take (fuelEfficiency, energyEfficiency, useCarMode).
   - Override start():
       - If useCarMode == true:
            print "Hybrid vehicle started in car mode."
       - Else:
            print "Hybrid vehicle started in bike mode."
   - Add displaySpecs() to print:
       - Fuel efficiency (km/L)
       - Energy efficiency (km/kWh)
   - Add computeTotalConsumption(double distance):
       - If useCarMode == true:
            Consumption = computeFuelNeeded(distance) liters
       - Else:
            Consumption = computeEnergyNeeded(distance) kWh

Notes:
- Both Car and Bike inherit Vehicle, so use virtual inheritance
  to avoid the diamond problem.
- Use protected inheritance for Car so that car-specific details
  are encapsulated and only accessible via HybridVehicle.
=============================================
*/
#include <iostream>
#include <iomanip>
#include <string>

// ---- Demo ----
int main() {
    // 연비: 15 km/L, 전비: 7 km/kWh, 초기 모드: car
    HybridVehicle hv(/*fuelEfficiency=*/15.0,
                     /*energyEfficiency=*/7.0,
                     /*useCarMode=*/true);

    hv.start();
    hv.displaySpecs();

    double distance = 140.0; // km
    std::cout << std::fixed << std::setprecision(2);

    std::cout << "Distance: " << distance << " km\n";
    std::cout << "Total consumption (car mode, liters): "
              << hv.computeTotalConsumption(distance) << "\n\n";

    // 모드 전환: bike
    hv.setUseCarMode(false);
    hv.start();
    hv.displaySpecs();
    std::cout << "Total consumption (bike mode, kWh): "
              << hv.computeTotalConsumption(distance) << "\n";

    return 0;
}