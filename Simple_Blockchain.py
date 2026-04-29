import hashlib

class BitCoin:

    def __init__ (self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

choice = input("Do you want to add a transaction(min 2 if you are adding): ").lower()
if choice == "yes":
    while True:
        t1 = input("Type in the details of the transaction: ")
        t2 = input("Type in the details of the transaction: ")
        initial_block = BitCoin("initial String", [t1, t2])

        print(initial_block.block_data)
        print(initial_block.block_hash)

        choice = input("Do you want to add a transaction(min 2 if you are adding): ").lower()
        if choice == "yes":
            t3 = input("Type in the details of the transaction: ")
            t4 = input("Type in the details of the transaction: ")

            second_block = BitCoin(initial_block.block_hash, [t3, t4])

            print(second_block.block_data)
            print(second_block.block_hash)

            choice = input("Do you want to add a transaction(min 2 if you are adding): ").lower()
            if choice == "yes":
                t5 = input("Type in the details of the transaction: ")
                t6 = input("Type in the details of the transaction: ")

                third_block = BitCoin(second_block.block_hash, [t5,t6])

                print(third_block.block_data)
                print(third_block.block_hash)

else:
    print("Ok Bye!")
    quit()