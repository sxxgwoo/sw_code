#include <iostream>
#include <iomanip>
#include <string>

// 1) PaymentProcessor (추상 클래스)
class PaymentProcessor {
public:
    virtual void start() = 0;               // 순수 가상 함수
    virtual ~PaymentProcessor() = default;  // 가상 소멸자
};

// 2) CardProcessor (protected 가상 상속)
class CardProcessor : protected virtual PaymentProcessor {
protected:
    double feeRatePercent; // 수수료율 (%)

public:
    explicit CardProcessor(double feeRatePercent)
        : feeRatePercent(feeRatePercent) {}

    void start() override {
        std::cout << "Card processor ready." << std::endl;
    }

protected:
    // HybridCheckout에서 사용할 수 있도록 protected로 둔다.
    double computeFee(double amount) const {
        return amount * (feeRatePercent / 100.0);
    }

    // 하위 클래스에서 스펙 출력 시 접근용 헬퍼
    double getFeeRate() const { return feeRatePercent; }
};

// 3) MobileWallet (public 가상 상속)
class MobileWallet : public virtual PaymentProcessor {
protected:
    double cashbackRatePercent; // 캐시백율 (%)

public:
    explicit MobileWallet(double cashbackRatePercent)
        : cashbackRatePercent(cashbackRatePercent) {}

    void start() override {
        std::cout << "Mobile wallet ready." << std::endl;
    }

    double computeCashback(double amount) const {
        return amount * (cashbackRatePercent / 100.0);
    }

protected:
    double getCashbackRate() const { return cashbackRatePercent; }
};

// 4) HybridCheckout (다중 상속)
class HybridCheckout : public CardProcessor, public MobileWallet {
    bool useCard; // true: 카드 모드, false: 지갑 모드

public:
    HybridCheckout(double feeRatePercent,
                   double cashbackRatePercent,
                   bool useCard)
        : PaymentProcessor()        // 가상 기반 초기화(선택적 표기)
        , CardProcessor(feeRatePercent)
        , MobileWallet(cashbackRatePercent)
        , useCard(useCard)
    {}

    // 모드에 따라 다른 시작 메시지
    void start() override {
        if (useCard) {
            std::cout << "Hybrid checkout started in card mode." << std::endl;
        } else {
            std::cout << "Hybrid checkout started in wallet mode." << std::endl;
        }
    }

    // 스펙 출력
    void displaySpecs() const {
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "[Hybrid Specs]\n"
                  << " - Card fee rate: " << getFeeRate() << "%\n"
                  << " - Wallet cashback rate: " << getCashbackRate() << "%\n";
    }

    // 총 청구액 계산
    double computeNetCharge(double amount) const {
        if (useCard) {
            return amount + computeFee(amount);              // 카드 경로
        } else {
            return amount - computeCashback(amount);         // 지갑 경로
        }
    }

    // 모드 전환(옵션)
    void setUseCard(bool on) { useCard = on; }
    bool isCardMode() const { return useCard; }
};

// ---- 간단 데모 ----
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