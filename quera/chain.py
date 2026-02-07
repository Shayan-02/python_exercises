class Chain:
    def __init__(self, *args):
        self.value = args

    def __call__(self, *args):
        self.value += args
        return self

    def __eq__(self, other):
        return self.value[0] == other

# مثال‌های ارائه شده:
result1 = Chain(2, 5)(2)(2.5)
result2 = Chain(3)(1.5)(2)(3)
result3 = Chain(64) == 64

print(f"Result 1: {result1}")  # خروجی: 9
print(f"Result 2: {result2}")  # خروجی: 9.5
print(f"Result 3: {result3}")  # خروجی: True

# اتصال رشته‌ها:
concatenated_str1 = Chain('Ali')('Safina')('is')('the')('best.')
concatenated_str2 = Chain('abc')('defg')

print(f"Concatenated String 1: {concatenated_str1}")  # خروجی: 'Ali Safina is the best.'
print(f"Concatenated String 2: {concatenated_str2}")  # خروجی: 'abc defg'
