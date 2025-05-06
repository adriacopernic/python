precio = float(input("cuenta sin IVA:"))
IVA = precio * 0.21
propina = precio * 0.5
total = precio + IVA + propina
total_persona = total / 2
print("cada persona tiene que pagar", total_persona)