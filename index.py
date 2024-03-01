slr_bruto = int(input("Informe o salário bruto: "))
slr_liquido = 0
ttl_dscnts = 0

rgps_valor = 0

teto_rgps = 1500
rgps_slr_maior = 11/100
rgps_slr_menor = 7/100

va_valor = 0

teto_va = 1000
va_slr_maior = 4.5/100
va_slr_menor = 0

am_valor = 0

teto_am = 2500
am_slr_maior = 8/100
am_slr_menor = 3/100

if slr_bruto >= teto_rgps: 
    rgps_valor = slr_bruto * rgps_slr_maior
else :
    rgps_valor = slr_bruto * rgps_slr_menor

if slr_bruto >= teto_va: 
    va_valor = slr_bruto * va_slr_maior
else :
    va_valor = slr_bruto * va_slr_menor

if slr_bruto >= teto_am: 
    am_valor = slr_bruto * am_slr_maior
else :
    am_valor = slr_bruto * am_slr_menor

ttl_dscnts = (rgps_valor + va_valor + am_valor)
slr_liquido = slr_bruto - ttl_dscnts

print(f"Seu salário bruto é de {slr_bruto}, com os descontos seu salário ficou em: {slr_liquido}")