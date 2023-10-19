# net-charge.py

# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

# Create a dictionary with pK values for specific amino acids
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}
# Initialize pH
pH = 0

# While loop to calculate net charge at different pH levels
while pH <= 14:
    seqCount = {x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}
    netCharge = (
        +(sum({x: ((seqCount[x] * (10 ** pKR[x])) / ((10 ** pH) + (10 ** pKR[x])))
            for x in ['k', 'h', 'r']}.values()))
        - (sum({x: ((seqCount[x] * (10 ** pH)) / ((10 ** pH) + (10 ** pKR[x])))
            for x in ['y', 'c', 'd', 'e']}.values()))
    )
    print('{0:.2f}'.format(pH), netCharge)
    pH += 1