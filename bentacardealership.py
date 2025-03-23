toyotaCars = ["Vios", "Fortuner", "Innova"]
hondaCars = ["City", "Civic", "CRV"]
aureliosCars = ["GT", "RT", "XT"]
fordCars = ["Ranger", "Mustang", "Explorer"]
MitsubishiCars = ["Mirage", "Montero", "Strada"]
toyotaCarsPrice = [2000000, 2500000, 3000000]
hondaCarsPrice = [1000000, 1500000, 2000000]
aureliosCarsPrice = [3000000, 3500000, 4000000]
fordCarsPrice = [1500000, 2000000, 2500000]
MitsubishiCarsPrice = [1200000, 1800000, 2300000]


checker = 1

while checker == 1:
    if checker == 2:
        break
    try:
        print("   WELCOME TO ABC DEALERSHIP") #welcome message & car brands
        carBrand = int(input("""    CHOOSE CAR BRAND (1-5)
    1. Honda
    2. Toyota
    3. Aurelio
    4. Ford
    5. Mitsubishi
        CHOSEN BRAND: """))
        print(" ")
        if carBrand >= 1 and carBrand <= 5:
        
            if carBrand == 1:
                carChosen = int(input("""    CHOOSE CAR MODEL (1-3)
    1. Honda City
    2. Honda Civic
    3. Honda CRV
        CHOSEN MODEL: """))
                if carChosen >= 1 and carChosen <= 3:
                    pass
            elif carBrand == 2:
                carChosen = int(input("""    CHOOSE CAR MODEL (1-3)
    1. Toyota Vios
    2. Toyota Fortuner
    3. Toyota Innova
        CHOSEN MODEL: """))
                if carChosen >= 1 and carChosen <= 3:
                    pass
            elif carBrand == 3:
                carChosen = int(input("""    CHOOSE CAR MODEL (1-3)
    1. Aurelio GT
    2. Aurelio RT
    3. Aurelio XT
        CHOSEN MODEL: """))
                if carChosen >= 1 and carChosen <= 3:
                    pass
            elif carBrand == 4:
                carChosen = int(input("""    CHOOSE CAR MODEL (1-3)
    1. Ford Ranger
    2. Ford Mustang
    3. Ford Explorer
        CHOSEN MODEL: """))
                if carChosen >= 1 and carChosen <= 3:
                    pass
            elif carBrand == 5:
                carChosen = int(input("""    CHOOSE CAR MODEL (1-3)
    1. Mitsubishi Mirage
    2. Mitsubishi Montero
    3. Mitsubishi Strada
        CHOSEN MODEL: """))
                if carChosen >= 1 and carChosen <= 3:
                    pass
            else:
                print("Invalid input")
                continue
        else:
            print("Invalid input")
            continue
        
        print(" ")
        mop = int(input("""     CHOOSE MODE OF PAYMENT:
    1. Cash (10% Discount)
    2. Installment (5% Interest)
CHOSEN PAYMENT: """))
        if mop != 1 and mop != 2:
            print("\nInvalid input\n")
            continue
        
        try:
            if mop == 1:  # cash payment
                
                if carBrand == 1: # honda
                    print("\n<=====RECEIPT=====>")
                    print("Chosen your car: Honda " + hondaCars[carChosen - 1])
                    priceCalculation = round(hondaCarsPrice[carChosen - 1] * 0.9, 2)
                    tupledPrice = f"{priceCalculation:,}"
                    print(f"Total amount: PHP", tupledPrice)
                    print("<=====RECEIPT=====>\n")
                elif carBrand == 2: #toyota  
                    print("\n<=====RECEIPT=====>")
                    print("Chosen your car: Toyota " + toyotaCars[carChosen - 1])
                    priceCalculation = round(toyotaCarsPrice[carChosen - 1] * 0.9, 2)
                    tupledPrice = f"{priceCalculation:,}"
                    print(f"Total amount: PHP", tupledPrice)
                    print("<=====RECEIPT=====>\n")
                elif carBrand == 3: #aurelio 
                    print("\n<=====RECEIPT=====>")
                    print("Chosen your car: Aurelio " + aureliosCars[carChosen - 1])
                    priceCalculation = round(aureliosCarsPrice[carChosen - 1] * 0.9, 2)
                    tupledPrice = f"{priceCalculation:,}"
                    print(f"Total amount: PHP", tupledPrice)
                    print("<=====RECEIPT=====>\n")
                elif carBrand == 4: #Ford 
                    print("\n<=====RECEIPT=====>")
                    print("Chosen your car: Ford " + fordCars[carChosen - 1])
                    priceCalculation = round(fordCarsPrice[carChosen - 1] * 0.9, 2)
                    tupledPrice = f"{priceCalculation:,}"
                    print(f"Total amount: PHP", tupledPrice)
                    print("<=====RECEIPT=====>\n")
                elif carBrand == 5: #Mitsubishi 
                    print("\n<=====RECEIPT=====>")
                    print("Chosen your car: Mitsubishi " + MitsubishiCars[carChosen - 1])
                    priceCalculation = round(MitsubishiCarsPrice[carChosen - 1] * 0.9, 2)
                    tupledPrice = f"{priceCalculation:,}"
                    print(f"Total amount: PHP", tupledPrice)
                    print("<=====RECEIPT=====>\n")
                
            elif mop == 2:  # installment payment
                raise Exception
        except Exception:
            months = int(input("""CHOOSE HOW MANY MONTHS: 12, 24 OR 36
    CHOSEN MONTHS: """))
            if months == 12 or months == 24 or months == 36:
                if carBrand == 1:
                    print("\n<=====RECEIPT=====>")
                    print("Chosen your car: Honda " + hondaCars[carChosen - 1])
                    priceCalculation = round(hondaCarsPrice[carChosen - 1] * 1.05, 2)
                    tupledPrice = f"{priceCalculation:,}"
                    monthlyPayment = round((hondaCarsPrice[carChosen - 1] * 1.05) / months, 2)
                    tupledMonthlyPayment = f"{monthlyPayment:,}"
                    print(f"Total amount: PHP", tupledPrice)
                    print(f"Monthly payment: PHP", tupledMonthlyPayment)
                    print("<=====RECEIPT=====>\n")
                elif carBrand == 2:
                    print("\n<=====RECEIPT=====>")
                    print("Chosen your car: Toyota " + toyotaCars[carChosen - 1])
                    priceCalculation = round(toyotaCarsPrice[carChosen - 1] * 1.05, 2)
                    tupledPrice = f"{priceCalculation:,}"
                    monthlyPayment = round((toyotaCarsPrice[carChosen - 1] * 1.05) / months, 2)
                    tupledMonthlyPayment = f"{monthlyPayment:,}"
                    print(f"Total amount: PHP", tupledPrice)
                    print(f"Monthly payment: PHP", tupledMonthlyPayment)
                    print("<=====RECEIPT=====>\n")
                elif carBrand == 3:
                    print("\n<=====RECEIPT=====>")
                    print("Chosen your car: Aurelio " + aureliosCars[carChosen - 1])
                    priceCalculation = round(aureliosCarsPrice[carChosen - 1] * 1.05, 2)
                    tupledPrice = f"{priceCalculation:,}"
                    monthlyPayment = round((aureliosCarsPrice[carChosen - 1] * 1.05) / months, 2)
                    tupledMonthlyPayment = f"{monthlyPayment:,}"
                    print(f"Total amount: PHP", tupledPrice)
                    print(f"Monthly payment: PHP", tupledMonthlyPayment)
                    print("<=====RECEIPT=====>\n")
                elif carBrand == 4:
                    print("\n<=====RECEIPT=====>")
                    print("Chosen your car: Ford " + fordCars[carChosen - 1])
                    priceCalculation = round(fordCarsPrice[carChosen - 1] * 1.05, 2)
                    tupledPrice = f"{priceCalculation:,}"
                    monthlyPayment = round((fordCarsPrice[carChosen - 1] * 1.05) / months, 2)
                    tupledMonthlyPayment = f"{monthlyPayment:,}"
                    print(f"Total amount: PHP", tupledPrice)
                    print(f"Monthly payment: PHP", tupledMonthlyPayment)
                    print("<=====RECEIPT=====>\n")
                elif carBrand == 5:
                    print("\n<=====RECEIPT=====>")
                    print("Chosen your car: Mitsubishi " + MitsubishiCars[carChosen - 1])
                    priceCalculation = round(MitsubishiCarsPrice[carChosen - 1] * 1.05, 2)
                    tupledPrice = f"{priceCalculation:,}"
                    monthlyPayment = round((MitsubishiCarsPrice[carChosen - 1] * 1.05) / months, 2)
                    tupledMonthlyPayment = f"{monthlyPayment:,}"
                    print(f"Total amount: PHP", tupledPrice)
                    print(f"Monthly payment: PHP", tupledMonthlyPayment)
                    print("<=====RECEIPT=====>\n")
            else:
                print("Invalid input\n")
                
        checker = int(input("""Make another transaction?
    1. Yes
    2. No

Enter here: """))
    except ValueError:
        print("Invalid input\n")
    finally:
        print("\nThank you for visiting ABC Dealership!!\n")
