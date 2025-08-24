/*
=============================================
   Problem: PaymentProcessor Hierarchy Design
=============================================

Design and implement the following class hierarchy in C++ using OOP principles.

1) PaymentProcessor (Abstract Base Class)
   - Declare start() as a pure virtual function.
   - Define a virtual destructor.

2) CardProcessor (Card-based Payment)
   - Inherit from PaymentProcessor using protected virtual inheritance.
   - Constructor should take feeRatePercent (transaction fee rate in %) as argument.
   - Override start() to print:
       "Card processor ready."
   - Add a function computeFee(double amount) that returns:
       amount * feeRatePercent / 100.0

3) MobileWallet (Mobile Wallet Payment)
   - Inherit from PaymentProcessor using public virtual inheritance.
   - Constructor should take cashbackRatePercent (cashback rate in %) as argument.
   - Override start() to print:
       "Mobile wallet ready."
   - Add a function computeCashback(double amount) that returns:
       amount * cashbackRatePercent / 100.0

4) HybridCheckout (Hybrid Payment: Card + Wallet)
   - Inherit from both CardProcessor and MobileWallet (multiple inheritance).
   - Constructor should take (feeRatePercent, cashbackRatePercent, useCard).
   - Override start():
       - If useCard == true:
            print "Hybrid checkout started in card mode."
       - Else:
            print "Hybrid checkout started in wallet mode."
   - Add displaySpecs() to print:
       - Card fee rate (%)
       - Wallet cashback rate (%)
   - Add computeNetCharge(double amount):
       - If useCard == true:
            Net charge = amount + computeFee(amount)
       - Else:
            Net charge = amount - computeCashback(amount)

Notes:
- Both CardProcessor and MobileWallet inherit PaymentProcessor, so use virtual inheritance
  to avoid the diamond problem.
- Use protected inheritance for CardProcessor so that its internal details are not exposed
  directly to external users.
=============================================
*/
#include <iostream>
#include <iomanip>
#include <string>



int main() {
    HybridCheckout checkout(/*feeRatePercent=*/2.5,
                            /*cashbackRatePercent=*/1.0,
                            /*useCard=*/true);

    // 각 경로의 start()는 필요시 호출 가능
    // (하위 클래스 start()와는 별개로, Hybrid의 모드 메시지 출력)
    checkout.start();
    checkout.displaySpecs();

    double amount = 100.0;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Amount: " << amount << "\n";
    std::cout << "Net charge (card mode): "
              << checkout.computeNetCharge(amount) << "\n\n";

    // 모드 전환: 지갑 모드
    checkout.setUseCard(false);
    checkout.start();
    checkout.displaySpecs();
    std::cout << "Net charge (wallet mode): "
              << checkout.computeNetCharge(amount) << "\n";

    return 0;
}