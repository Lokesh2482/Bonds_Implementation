

This repository provides a Python implementation of basic bond pricing models using object-oriented programming. The project includes two types of bonds:

* **Zero-Coupon Bonds**: Bonds that do not pay periodic coupons and are valued at a discount.
* **Coupon Bonds**: Bonds that provide annual coupon payments along with repayment of principal at maturity.

---

## Features

* Object-oriented design with reusable classes
* Supports both zero-coupon and coupon bond pricing
* Flexible parameters for principal, coupon rate, maturity, and interest rate
* Clean and readable implementation

---

## Project Structure

```
Bonds_Implementation/
│
├── main.py        # Contains implementations of ZeroCouponBonds and CouponBond
├── README.md      # Project documentation
```

---

## Usage

### Zero-Coupon Bond Example

```python
from main import ZeroCouponBonds

bond = ZeroCouponBonds(1000, 2, 4)  # principal=1000, maturity=2 years, rate=4%
print(bond.calculate_price())
```

### Coupon Bond Example

```python
from main import CouponBond

bond = CouponBond(1000, 4, 2, 4)  # principal=1000, coupon=4%, maturity=2 years, rate=4%
print(bond.total_value())
```

---

## Installation

Clone the repository and run the script:

```bash
git clone https://github.com/your-username/Bonds_Implementation.git
cd Bonds_Implementation
python main.py
```

