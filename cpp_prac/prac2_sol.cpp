#include <iostream>
#include <iomanip>
#include <string>

// 1) Vehicle (Abstract Base Class)
class Vehicle {
public:
    virtual void start() = 0;               // pure virtual
    virtual ~Vehicle() = default;           // virtual destructor
};

// 2) Car (protected virtual inheritance)
class Car : protected virtual Vehicle {
protected:
    double fuelEfficiency; // km per liter

public:
    explicit Car(double fuelEfficiency)
        : fuelEfficiency(fuelEfficiency) {}

    void start() override {
        std::cout << "Car started." << std::endl;
    }

protected:
    // HybridVehicle에서 사용하도록 protected
    double computeFuelNeeded(double distance) const {
        // 거리 / (km/L) = L
        return distance / fuelEfficiency;
    }

    double getFuelEfficiency() const { return fuelEfficiency; }
};

// 3) Bike (public virtual inheritance)
class Bike : public virtual Vehicle {
protected:
    double energyEfficiency; // km per kWh

public:
    explicit Bike(double energyEfficiency)
        : energyEfficiency(energyEfficiency) {}

    void start() override {
        std::cout << "Bike started." << std::endl;
    }

    // 굳이 숨길 필요 없으니 public
    double computeEnergyNeeded(double distance) const {
        // 거리 / (km/kWh) = kWh
        return distance / energyEfficiency;
    }

protected:
    double getEnergyEfficiency() const { return energyEfficiency; }
};

// 4) HybridVehicle (Car + Bike)
class HybridVehicle : public Car, public Bike {
    bool useCarMode; // true: car mode, false: bike mode

public:
    HybridVehicle(double fuelEfficiency,
                  double energyEfficiency,
                  bool useCarMode)
        : Vehicle()
        , Car(fuelEfficiency)
        , Bike(energyEfficiency)
        , useCarMode(useCarMode)
    {}

    void start() override {
        if (useCarMode) {
            std::cout << "Hybrid vehicle started in car mode." << std::endl;
        } else {
            std::cout << "Hybrid vehicle started in bike mode." << std::endl;
        }
    }

    void displaySpecs() const {
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "[Hybrid Specs]\n"
                  << " - Fuel efficiency: " << getFuelEfficiency() << " km/L\n"
                  << " - Energy efficiency: " << getEnergyEfficiency() << " km/kWh\n";
    }

    // mode에 따라 총 소비량(L 또는 kWh)을 계산
    double computeTotalConsumption(double distance) const {
        if (useCarMode) {
            return computeFuelNeeded(distance);      // liters
        } else {
            return computeEnergyNeeded(distance);    // kWh
        }
    }

    // 옵션: 모드 전환/조회
    void setUseCarMode(bool on) { useCarMode = on; }
    bool isCarMode() const { return useCarMode; }
};

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