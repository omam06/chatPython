def make_discount(discount):
    def apply_discount(price):
        return price - discount

    return apply_discount

ten_off = make_discount(10)
twenty_off = make_discount(20)

print(ten_off(100))
print(twenty_off(200))

print()
