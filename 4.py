import re

pwcount = 0
# first part
#consecutivesame = "(11|22|33|44|55|66|77|88|99|00)"
# second part
consecutivesame = "(([^1]|^)11([^1]|$)|([^2]|^)22([^2]|$)|([^3]|^)33([^3]|$)|([^4]|^)44([^4]|$)|([^5]|^)55([^5]|$)|([^6]|^)66([^6]|$)|([^7]|^)77([^7]|$)|([^8]|^)88([^8]|$)|([^9]|^)99([^9]|$)|([^0]|^)00([^0]|$))"

for i in range(246540, 787420):
    istr = str(i)
    iparts = [s for s in istr]
    sortstr = ''.join(sorted(iparts))
    if (sortstr == istr and re.search(consecutivesame, istr)):
        pwcount += 1

print(pwcount)
