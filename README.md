# Bonds Implementation in Python

This repository provides a Python implementation of fundamental bond pricing models using object-oriented programming principles. The models implemented include:

1. **Zero-Coupon Bond**
2. **Coupon Bond**

---

## Zero-Coupon Bond

A zero-coupon bond does not pay periodic coupon payments. Instead, it is issued at a discount and redeemed at face value upon maturity.

### Formula

$$
PV = \frac{FV}{(1+r)^n}
$$

Where:

* $PV$ = Present Value (bond price)
* $FV$ = Face Value (principal)
* $r$ = Interest rate (decimal form)
* $n$ = Time to maturity (years)

### Example

```python
from main import ZeroCouponBonds

bond = ZeroCouponBonds(1000, 2, 4)  # principal=1000, maturity=2 years, rate=4%
print(f"Price of the zero coupon bond is : {round(bond.calculate_price(), 2)}")
```

**Output:**

```
Price of the zero coupon bond is : 924.56
```

---

## Coupon Bond

A coupon bond provides periodic coupon payments in addition to repayment of the principal at maturity.

### Formula

$$
Price = \sum_{t=1}^{n} \frac{C}{(1+r)^t} + \frac{FV}{(1+r)^n}
$$

Where:

* $C$ = Annual coupon payment $(Principal \times \text{Coupon Rate})$
* $FV$ = Face Value (principal)
* $r$ = Interest rate (decimal form)
* $n$ = Time to maturity (years)

### Example

```python
from main import CouponBond

bond = CouponBond(1000, 4, 2, 4)  # principal=1000, coupon=4%, maturity=2 years, rate=4%
print(f"Price of the coupon bond is : {round(bond.total_value(), 2)}")
```

**Output:**

```
Price of the coupon bond is : 1000.0
```

---

## Project Structure

```
Bonds_Implementation/
│
├── main.py        # Contains class implementations for ZeroCouponBonds and CouponBond
├── README.md      # Documentation file
```

---

## Installation & Execution

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Bonds_Implementation.git
   cd Bonds_Implementation
   ```

2. Run the script:

   ```bash
   python main.py
   ```

---

## Features

* Object-oriented implementation of bond pricing models
* Supports both **zero-coupon** and **coupon bonds**
* Accurate valuation using present value formulas
* Flexible parameterization (principal, coupon, maturity, interest rate)

---

## Applications

* Financial modeling and valuation
* Academic research in finance and economics
* Educational purposes to understand bond pricing fundamentals

---

