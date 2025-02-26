A = {"a", "b", "c", "d", "f", "g"}
B = {"b", "c", "d", "f", "h", "l", "m", "o"}
C = {"c", "d", "f", "h", "i", "j", "k"}

union_A_B = A | B
print("Elements in A and B:", union_A_B, "| Count:", len(union_A_B))

only_in_B = B - (A | C)
print("Elements in B but not in A or C:", only_in_B, "| Count:", len(only_in_B))

print("[h, i, j, k]:", C - (A | B))
print("[c, d, f]:", A & B & C)
print("[b, c, h]:", {"b", "c", "h"} & B)
print("[d, f]:", A & C)
print("[c]:", A & B & C)
print("[l, m, o]:", B - (A | C))