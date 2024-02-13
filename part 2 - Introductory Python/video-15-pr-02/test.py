ounce = float(input('Ounce:'))
us_dollers = int(input("US dollers:"))

# 4.24927  ÷ (قيمت يك دلار× قيمت يك انس طلا)
sekke = int((ounce * us_dollers ) / 4.24927)
print(f"Sekkeh is {sekke} tomans!!")
