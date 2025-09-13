class ZeroCouponBonds:

    def __init__(self, principal, maturity, interest_rate):
        self.principal = principal
        self.maturity = maturity
        self.interest_rate = interest_rate / 100  # convert % to decimal

    def present_value(self, x, n):
        return x / (1 + self.interest_rate) ** n

    def calculate_price(self):
        return self.present_value(self.principal, self.maturity)


if __name__ == '__main__':
    bond = ZeroCouponBonds(1000, 2, 4)  # principal=1000, maturity=2 years, rate=4%
    print(f"Price of the zero coupon bond is : {(round(bond.calculate_price(), 2))}")


class CouponBond:

    def __init__(self,principal,coupon,maturity,interest_rate):
        self.principal = principal
        self.coupon = coupon
        self.maturity = maturity
        self.interest_rate = interest_rate/100

    def present_coupon_value(self,c,n):
        sum = 0
        for i in range(0,n):
            coupon_value = self.principal*c/(100*(1+self.interest_rate)**(i+1))
            sum+=coupon_value
        
        return sum
    
    def present_value(self, x, n):
        return x / (1 + self.interest_rate) ** n
    
    def total_value(self):
        return self.present_coupon_value(self.coupon,self.maturity)+self.present_value(self.principal,self.maturity)
    
if __name__ == '__main__':
        bond = CouponBond(1000, 10, 3, 4)  # principal=1000,coupon = 10% maturity=3 years, rate=4%
        print(f"Price of the coupon bond is : {(round(bond.total_value(), 2))}")

    
#continuous model for discounting
from math import exp

class ContinuousZeroCouponBonds:
    def __init__(self, principal, maturity, interest_rate):
        self.principal = principal
        self.maturity = maturity
        self.interest_rate = interest_rate / 100  # convert % to decimal

    def present_value(self, x, n):
        return x*exp(-self.interest_rate*n)

    def calculate_price(self):
        return self.present_value(self.principal, self.maturity)
    

if __name__ == '__main__':
        bond = ContinuousZeroCouponBonds(1000,2, 4)  # principal=1000, maturity=2 years, rate=4%
        print(f"Price of the continuous zero coupon bond is : {(round(bond.calculate_price(), 2))}")






