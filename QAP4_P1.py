# QAP 4-1: ONE STOP INSURANCE COMPANY
# Description: Program for entering and calculating new
#              insurance policy info for its customers.
# Author: Steven V. Squires
# Date written: July 16 - 26, 2023

# Libraries
import datetime
import time
from tqdm import tqdm
import FormatValues as FV

# Constants

# Open the defaults file and read the values into the variables.
f = open('OSICDef.dat', 'r')
POLICY_NUM = int(f.readline())
BASE_PREM = float(f.readline())
ADD_CAR_DISC = float(f.readline())
XTRA_LIAB_COST = float(f.readline())
GLASS_COV_COST = float(f.readline())
LOANCAR_COV_COST = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())
f.close()


# Define Functions
def validate_province(Prov):
    valid_provinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
    return Prov.upper() in valid_provinces


def validate_payment_method(payment_method):
    PayMethod_list = ['F', 'M']
    return payment_method.title() in PayMethod_list


# Main Program
while True:
    print(POLICY_NUM)
    while True:
        CustFName = (input("Enter customer's first name: ")).title()
        if CustFName.strip() == "":
            print("ERROR - Customer's first name cannot be blank.")
        else:
            break

    while True:
        CustLName = (input("Enter customer's last name: ")).title()
        if CustLName.strip() == "":
            print("ERROR - Customer's last name cannot be blank.")
        else:
            break

    while True:
        StAdd = input("Enter the customer's street address (ex. 1025 Fake Street): ").title()
        if StAdd.strip() == "":
            print("ERROR - Customer's street address cannot be blank.")
        else:
            break

    while True:
        City = input("Enter the customer's City (ex. St. John's): ").title()
        if City.strip() == "":
            print("ERROR - Customer's city cannot be blank.")
        else:
            break

    while True:
        Prov = input("Enter province (two-letter abbreviation ex. NL): ").upper()
        if Prov.strip() == "":
            print("ERROR - Province abbreviation cannot be blank.")
        while not validate_province(Prov):
            print("Invalid province abbreviation. Please enter a valid two-letter abbreviation.")
            Prov = input("Enter province (two-letter abbreviation ex. NL): ").upper()
        else:
            break

    while True:
        allowed_char_B = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        PostalCode = input("Enter the postal code (ex. A1B2C3): ").upper()
        if PostalCode.strip() == "":
            print("ERROR - Postal code cannot be blank.")
        elif len(PostalCode) != 6:
            print("ERROR - Postal code must be 6 characters long.")
        elif not set(PostalCode).issubset(allowed_char_B):
            print("ERROR - Postal code contains invalid characters.")
        else:
            break

    while True:
        PhoneNum = input("Enter the customer's phone number (ex. 7095551234): ")
        if PhoneNum.strip() == "":
            print("ERROR - Customer phone number cannot be blank.")
        elif len(PhoneNum) != 10:
            print("ERROR - Customer phone number must be 10 digits long. (ex. 7095551234)")
        elif not PhoneNum.isdigit():
            print("ERROR - Customer phone number must consist of numerical digits only. (ex. 7095551234)")
        else:
            break

    while True:
        CarsNumInput = input("Enter the number of cars being insured: ")
        if CarsNumInput.strip() == "":
            print("ERROR - Number of cars cannot be blank.")
        elif not CarsNumInput.isdigit():
            print("ERROR - Number of cars must consist of numerical digits only. (ex. 12)")
        else:
            CarsNum = int(CarsNumInput)
            break

    while True:
        TotExtraCost = 0
        XtraLiabTotal = XTRA_LIAB_COST * CarsNum
        LiabDsp = ""
        ExtraLiab = (input("Extra liability coverage up to $1,000,000? (Y/N): ")).upper()
        if ExtraLiab != "Y" and ExtraLiab != "N":
            print("ERROR - Invalid input. Claim type must be Y or N.")
        else:
            if ExtraLiab == "Y":
                LiabDsp = FV.FDollar2(XtraLiabTotal)
                TotExtraCost += XTRA_LIAB_COST * CarsNum
            elif ExtraLiab == "N":
                LiabDsp = "None"
            break

    while True:
        GlassCovTotal = GLASS_COV_COST * CarsNum
        GlassDsp = ""
        GlassCoverage = (input("Glass coverage included? (Y/N): ")).upper()
        if GlassCoverage != "Y" and GlassCoverage != "N":
            print("ERROR - Invalid input. Glass coverage must be Y or N.")
        else:
            if GlassCoverage == "Y":
                GlassDsp = FV.FDollar2(GlassCovTotal)
                TotExtraCost += GlassCovTotal
            elif GlassCoverage == "N":
                GlassDsp = "None"
            break

    while True:
        LoanCarCost = LOANCAR_COV_COST * CarsNum
        LoanerDsp = ""
        LoanerCar = (input("Loaner car coverage included? (Y/N): ")).upper()
        if LoanerCar != "Y" and LoanerCar != "N":
            print("ERROR - Invalid input. Loaner car must be Y or N.")
        else:
            if LoanerCar == "Y":
                LoanerDsp = FV.FDollar2(LoanCarCost)
                TotExtraCost += LoanCarCost
            elif LoanerCar == "N":
                LoanerDsp = "None"
            break

    while True:
        PayMethodDsp = ""
        PayMethod = input("Choose payment method (F for Full or M for Monthly): ").upper()
        if PayMethod == "F":
            PayMethodDsp = "Paid in Full"
        elif PayMethod == "M":
            PayMethodDsp = "Monthly Payments"
        if PayMethod == "":
            print("Error - Payment method cannot be blank.")
        while not validate_payment_method(PayMethod):
            print("Error - Payment method must be entered as F or M.")
            PayMethod = input("Choose payment method (F for Full or M for Monthly): ").upper()
        else:
            break

    # Calculations
    Premium = BASE_PREM + ((BASE_PREM * (CarsNum - 1)) * (1 - ADD_CAR_DISC))
    TotalPrem = Premium + TotExtraCost

    HST = TotalPrem * HST_RATE
    TotalCost = TotalPrem + HST

    MonthPay = (TotalCost + PROCESS_FEE) / 8
    Payment = ""
    if PayMethod == 'M':
        Payment = MonthPay
    else:
        PayMethod = 'F'
        Payment = TotalCost

    # Date adjustment
    InvDate = datetime.datetime.now()
    InvDateDsp = InvDate.strftime("%Y-%m-%d")
    NextPayDate = (datetime.date(InvDate.year, InvDate.month + 1, 1))

    # Concatenations
    CustFullName = CustFName + " " + CustLName
    PostalCodeConc = PostalCode[0:3] + " " + PostalCode[3:6]
    AddConc = City + ", " + Prov + ", " + PostalCodeConc
    PhoneNumDsp = f"({PhoneNum[:3]}) {PhoneNum[3:6]}-{PhoneNum[6:]}"

    # Receipt printed outputs
    print()
    print()
    print("            One Stop Insurance Company")
    print("           Customer Policy Info Receipt")
    print()
    print(f"Policy #: {POLICY_NUM:<5d}          Invoice Date: {InvDateDsp:>10} ")
    print("-------------------------------------------------")
    print("Customer Contact Information:")
    print()
    print(f"{CustFullName:<40}")
    print(f"{StAdd:<40s}")
    print(f"{AddConc:<40s}")
    print(f"Phone #: {PhoneNumDsp:<15s}")
    print("-------------------------------------------------")
    print("Insurance Policy Charges:")
    print()
    print(f"# of vehicles insured: {CarsNum:<3d}  Premium rate: {FV.FDollar2(BASE_PREM):<8s}")
    print()
    print("25% off premium rate for each additional vehicle!")
    print()
    print(f"                    Extra liability:   {LiabDsp :>10s}")
    print(f"                    Glass coverage:    {GlassDsp:>10s}")
    print(f"                    Loaner car:        {LoanerDsp:>10s}")
    print()
    print(f"                    Total extra costs: {FV.FDollar2(TotExtraCost):>10s}")
    print(f"                    Insurance premium: {FV.FDollar2(Premium):>10s}")
    print("                    -----------------------------")
    print(f"              Total insurance premium: {FV.FDollar2(TotalPrem):>10s}")
    print()
    print(f"                                  HST: {FV.FDollar2(HST):>10s}")
    print(f"                           Total cost: {FV.FDollar2(TotalCost):>10s}")
    print("-------------------------------------------------")
    print("Payment Details:")
    print()
    print(f"Payment type: {PayMethodDsp}")
    print()
    if PayMethod == 'M':
        print(f"               Monthly processing fee: {FV.FDollar2(PROCESS_FEE):>10s}")
        print(f"               8 monthly payments of:  {FV.FDollar2(Payment):>10s}")
        print(f"               Next payment date:      {FV.FDateS(NextPayDate):>10s}")
    else:
        print(f"                Completed payment of:  {FV.FDollar2(Payment):>10s}")
        print()
        print("           Thank you for all the monies!")
    print("-------------------------------------------------")

    print()
    print()
    # Processing bar

    print("Saving data - please wait")
    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)
    print("Policy information processed and saved.")
    time.sleep(1)

    # Writes the policy number, all input values, and total insurance premium to Policies.dat
    f = open('Policies.dat', 'a')
    f.write(f"{POLICY_NUM},")
    f.write(f"{InvDateDsp},")
    f.write(f"{CustFName},")
    f.write(f"{CustLName},")
    f.write(f"{StAdd},")
    f.write(f"{City},")
    f.write(f"{Prov},")
    f.write(f"{PostalCode},")
    f.write(f"{PhoneNumDsp},")
    f.write(f"{CarsNum},")
    f.write(f"{LiabDsp},")
    f.write(f"{GlassDsp},")
    f.write(f"{LoanerDsp},")
    f.write(f"{PayMethodDsp},")
    f.write(f"{TotalPrem}\n")
    f.close()

    # Create new policy number or end and increases policy number by 1.
    Continue = input("Would you like to create a new insurance policy? (Y/N): ").upper()
    if Continue == "Y":
        POLICY_NUM += 1
    elif Continue == "N":
        print("Thank you for using our program. May your enemies crumble.")
        print()
    # Write the current values back to the defaults file.
    f = open('OSICDef.dat', 'w')
    f.write(f"{POLICY_NUM}\n")
    f.write(f"{BASE_PREM}\n")
    f.write(f"{ADD_CAR_DISC}\n")
    f.write(f"{XTRA_LIAB_COST}\n")
    f.write(f"{GLASS_COV_COST}\n")
    f.write(f"{LOANCAR_COV_COST}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{PROCESS_FEE}\n")
    f.close()

