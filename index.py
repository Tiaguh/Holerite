slr_bruto = float(input("Informe o salário bruto: "))

rgps_valor = slr_bruto * (11/100) if slr_bruto >= 1500 else slr_bruto * (7/100)
va_valor = slr_bruto * (4.5/100) if slr_bruto >= 1000 else 0
am_valor = slr_bruto * (8/100) if slr_bruto >= 2500 else slr_bruto * (3/100)

ttl_dscnts = rgps_valor + va_valor + am_valor
slr_liquido = slr_bruto - ttl_dscnts

print(f"Seu salário bruto é de R${slr_bruto:.2f}. Com os descontos, seu salário líquido é de R${slr_liquido:.2f}.")