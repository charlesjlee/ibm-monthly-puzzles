import gmpy2
gmpy2.get_context().precision=100 # in bits

min_delta = 1e-20

# this implementation assumes the signs for a and b and sometimes fails
print(f"Finding n s.t. (√2-1)^n < min_delta")
n = 0
while (gmpy2.sqrt(2) - 1)**n > min_delta: n += 1
print(f"n: {n}")
print((gmpy2.sqrt(2) - 1)**n)
print(50*'-')

print(f"Simplifying (√2-1)^n to a√2 - b")
simplified = sympy.expand((sympy.sqrt(2)-1)**n)
a, b = simplified.args[1].args[0], -1*simplified.args[0]
print(f"a={a}, b={b}")
print(50*'-')

print("Factoring a and b into their binary representations")
def two_powers(num): return [i for i, bit in enumerate(bin(num)[:1:-1]) if bit == "1"]
a_powers, b_powers = two_powers(a), two_powers(b)
print(f'''a: {a} = {' + '.join([f"2^{x}" for x in a_powers])}''')
print(f'''b: {b} = {' + '.join([f"2^{x}" for x in b_powers])}''')
print(50*'-')

print("Forming and outputting the smooth sets A and B")
A = [2**(2*x+1) for x in a_powers]
B = [2**(2*x) for x in b_powers]
print(f'''A: {', '.join([f"2^{2*x+1}" for x in a_powers])}''')
print(f'''B: {', '.join([f"2^{2*x}" for x in b_powers])}''')
print()
print(f"A: {A}")
print(f"B: {B}")
print(50*'-')

print("Calculating set differences to double-check")
def smooth_sum(nums): return sum(gmpy2.sqrt(x) for x in nums)
print(smooth_sum(A) - smooth_sum(B))