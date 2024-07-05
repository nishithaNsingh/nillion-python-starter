#>>>>>>Privacy-Preserving Aggregate Financial Data Calculation<<<<<<<<<<<<<<<<<<
from nada_dsl import *

def nada_main(): 

    # Number of account holders 
    nr_account_holders = 5

    # Number of account types 
    nr_account_types = 3

    # Parties initialization (account holders)
    account_holders = []
    for i in range(nr_account_holders):
        account_holders.append(Party(name="AccountHolder_" + str(i)))
    outparty = Party(name="OutParty")

    # Inputs initialization (deposits per account type per account holder)
    deposits_per_account_type = []
    for a in range(nr_account_types):
        deposits_per_account_type.append([])
        for h in range(nr_account_holders):
            deposits_per_account_type[a].append(
                SecretUnsignedInteger(
                    Input(name="deposit_type_" + str(a) + "_holder_" + str(h), party=account_holders[h])
                )
            )

    # Computation (calculate total deposits per account type)
    total_deposits_per_type = []
    for a in range(nr_account_types):
        total_deposit = deposits_per_account_type[a][0]
        for h in range(1, nr_account_holders):
            total_deposit += deposits_per_account_type[a][h]
        # Output the total deposit for each account type
        total_deposits_per_type.append(Output(total_deposit, "total_deposit_type_" + str(a), outparty))

    return total_deposits_per_type


if __name__ == "__main__":
    results = nada_main()  
    print("Generated program:")
    for result in results:
        print(result)
