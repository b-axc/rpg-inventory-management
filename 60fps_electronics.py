"""
This program allows users to add variouscomputer parts to their cart and purchase them.
By Xander Walton
Note : You may have to run the program more than once for it to start
"""

#declare variables
department = 0
price = 0
cart = []
check_out = 0


#function for directing the user to their chosen computer part section
def section(department):
    if department == 1:
        cpu_page(department)
    if department == 2:
        gpu_page(department)
    if department == 3:
        mboard_page(department)
    if department == 4:
        psu_page(department)
    if department == 5:
        ssd_page(department)
    if department == 6:
        check_out_page(department)

def cpu_page(department):
    global check_out
    global price
    while department == 1:
        cpu = []
        cpu_product = int(input("\n 1. AMD RYZEN 7 5700XR $350 \n \n 2. INTEL i7 $320 \n \n 3. INTEL i9 $500 \n \n " 
                                "4. AMD RYZEN 9 9400 $550 \n \n 5. INTEL i3 $150 \n \n 6. Done shopping.\n"))
        cpu.append(cpu_product)
        print(cpu)
        if 1 in cpu:
            price = price + 350
            cart.append("AMD RYZEN 7 5700XR - $350")
        if 2 in cpu: 
            price = price + 320
            cart.append("INTEL i7 - $320")
        if 3 in cpu:
            price = price + 500
            cart.append("INTEL i9 - $500")
        if 4 in cpu: 
            price = price + 550
            cart.append("AMD RYZEN 9 9400 - $550")
        if 5 in cpu:
            price = price + 150
            cart.append("INTEL i3 - $150")
        if 6 in cpu: 
            department = 0

def gpu_page(department):
    global check_out
    global price
    while department == 2:
        gpu = []
        gpu_product = int(input("\n 1. MSI GeForce RTX 3050 6G $280 \n \n 2. PNY NVIDIA GeForce RTX 5060 8 GB $450 \n \n 3. XFX Swift " \
                                "Radeon RX 9060 XT GDDR6 Gaming $500 \n \n 4. NVIDIA GeForce RTX 3060 Ti Founders Edition 8GB GDDR6 $350\n \n"
                                " 5. NVIDIA Geforce Gtx Titan 6gb Gddr5 384bit $85 \n \n 6. Done shopping.\n"))
        gpu.append(gpu_product)
        print(gpu)
        if 1 in gpu:
            price = price + 280
            cart.append("MSI GeForce RTX 3050 6G - $280")
        if 2 in gpu: 
            price = price + 450
            cart.append("PNY NVIDIA GeForce RTX 5060 8 GB - $450")
        if 3 in gpu:
            price = price + 500
            cart.append("XFX Swift Radeon RX 9060 XT GDDR6 Gaming - $500")
        if 4 in gpu: 
            price = price + 350
            cart.append("NVIDIA GeForce RTX 3060 Ti Founders Edition 8GB GDDR6 - $350")
        if 5 in gpu:
            price = price + 85
            cart.append("NVIDIA Geforce Gtx Titan 6gb Gddr5 384bit - $85")
        if 6 in gpu: 
            department = 0

def mboard_page(department):
    global check_out
    global price
    while department == 3:
        mboard = []
        mboard_product = int(input("\n 1. ASRock B550M Phantom Gaming 4 AM4 AMD B550 Micro ATX $100 \n \n 2. ASUS B850-I ROG Strix Gaming WIFI AMD AM5 "
                                   "Mini-ITX Motherboard $365 \n \n 3. New Msi Z890 Gaming WIFI6E Lga 1851 Atx Intel DDR5 $220 \n \n " 
                                   "4. ASUS TUF GAMING X870 PLUS WIFI ATX Motherboard $245 \n \n 5. MSI MEG X870E GODLIKE MAX x870egodlike max $1300"
                                    "\n \n 6. Done shopping.\n"))
        mboard.append(mboard_product)
        print(mboard)
        if 1 in mboard:
            price = price + 100
            cart.append("ASRock B550M Phantom Gaming 4 AM4 AMD B550 Micro ATX - $100")
        if 2 in mboard: 
            price = price + 365
            cart.append("ASUS B850-I ROG Strix Gaming WIFI AMD AM5 Mini-ITX Motherboard - $365")
        if 3 in mboard:
            price = price + 220
            cart.append("New Msi Z890 Gaming WIFI6E Lga 1851 Atx Intel DDR5 - $220")
        if 4 in mboard: 
            price = price + 245
            cart.append("ASUS TUF GAMING X870 PLUS WIFI ATX Motherboard - $245")
        if 5 in mboard:
            price = price + 1300
            cart.append("MSI MEG X870E GODLIKE MAX x870egodlike max - $1300")
        if 6 in mboard: 
            department = 0    

def psu_page(department):
    global check_out
    global price
    while department == 4:
        psu = []
        psu_product = int(input("\n 1. Corsair RMx Series RM850x Fully Modular Power Supply $200 \n \n 2. MSI MAG PCIE5 Power Supply $130 \n \n "
                                "3. Rosewill VNW 650W 80+ White Certified Non-Modular Active PFC Design $170 \n \n "
                                "4. Be quiet! Dark Power Pro 13 Power supply unit 20+4 pin ATX ATX $432 \n \n"
                                " 5. Phanteks Revolt 1200W 80PLUS Platinum ATX 3.0 $250 \n \n 6. Done shopping.\n"))
        psu.append(psu_product)
        print(psu)
        if 1 in psu:
            price = price + 350
            cart.append("AMD RYZEN 7 5700XR - $350")
        if 2 in psu: 
            price = price + 320
            cart.append("INTEL i7 - $320")
        if 3 in psu:
            price = price + 500
            cart.append("INTEL i9 - $500")
        if 4 in psu: 
            price = price + 550
            cart.append("AMD RYZEN 9 9400 - $550")
        if 5 in psu:
            price = price + 150
            cart.append("INTEL i3 - $150")
        if 6 in psu: 
            department = 0

def ssd_page(department):
    global check_out
    global price
    while department == 5:
        ssd = []
        ssd_product = int(input("\n 1. Samsung 870 EVO SATA $350 \n \n 2. PNY CS900 Solid State Drive $120 \n \n 3. Samsung 990 Solid State Drive $230 \n \n " 
                                "4. SanDisk Optimus 5100 $290 \n \n 5. Samsung 990 PRO 2 SSD $640 \n \n 6. Done shopping.\n"))
        ssd.append(ssd_product)
        print(ssd)
        if 1 in ssd:
            price = price + 350
            cart.append("Samsung 870 EVO SATA - $350")
        if 2 in ssd: 
            price = price + 120
            cart.append("PNY CS900 Solid State Drive - $120")
        if 3 in ssd:
            price = price + 230
            cart.append("Samsung 990 Solid State Drive - $230")
        if 4 in ssd: 
            price = price + 290
            cart.append("SanDisk Optimus 5100 - $290")
        if 5 in ssd:
            price = price + 640
            cart.append("Samsung 990 PRO 2 SSD - $640")
        if 6 in ssd: 
            department = 0

def check_out_page(department):
    global check_out
    global price
    while department == 6:
        print("Cart:\n" + '\n'.join(cart) + "\n")
        print("Total: $" + str(price))
        check_out = int(input("Are you ready to check out? \n 1. Yes \n \n 2. No \n"))
        if check_out == 1:
            print("Thank you for stopping by!")
            exit()
        if check_out == 2:
            department = 0
            front_page()
            check_out = 0
        break
    
# function to guide the user to each department
def front_page():
    print("Hello! Welcome to 60FPS Electronics! \nWhat can we get you? \n \nPlease note that you must restart the program if you want to remove an item.\n")
    department = int(input("Which section you looking for? \n 1. CPU \n \n 2. GPU \n \n 3. Motherboard \n \n 4. Power Supply \n \n 5. SSD \n \n"
    " 6. Check Out \n \n Please type the desired number for the rest of the website. "))
    section(department)

# function to run the program
def main():
    global check_out
    while check_out != 1:
        front_page()
        while department == True:
            if department == 0:
                front_page()
            elif check_out == 1:
                break
    
main()
