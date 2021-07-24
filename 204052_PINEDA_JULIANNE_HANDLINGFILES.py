products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# CODE CELL
# PROBLEM 1

def get_product(code):
    return  products[code] 


# CODE CELL
# PROBLEM 2

def get_property(code, property):
    return products[code][property]

def main():
    
    session = ""
    receipt = """"""
    total = 0
    pdict = {}
    
    with open("receipt.txt", "w") as summary:
        summary.write('''==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n''')
    
    while session != "/":
        
        session = input("{product_code},{quantity}")
        
        if session != "/":  
            co_qu = session.split(",")
            
            code = co_qu[0]
            quantity = int(co_qu[1])
            
            if code not in pdict:
                pdict[code] = quantity
                
            else:
                pdict[code] += quantity 
         
        elif session == "/":
            break
    for i in sorted(pdict):
            name = get_property(i,"name")
            subtotal = get_property(i,"price")*pdict[i]
            with open("receipt.txt", "a+") as summary:
                summary.write(f'''{i}\t\t{name}\t\t{pdict[i]}\t\t\t\t\t{subtotal}\n''')
            total += subtotal
    with open("receipt.txt","a+") as summary:       
        summary.write(f'''\nTotal:\t\t\t\t\t\t\t\t\t\t\t\t{total}
==''')
    
main()
