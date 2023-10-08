N = int (input("Veuillez saisir le nombre de copies:" ))
if N < 10:
   F = N* 0.3
elif N < 30:
     F = 10 * 0.3 + (N-10) *0.25
else :
     F = 10 *0.3 + 20 * 0.25 + (N-30) * 0.2
print ("Le montant de facture à payer est: ", F)