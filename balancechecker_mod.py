import blockcypher
from moneywagon import AddressBalance

def balance(addr):
    try:
        total = blockcypher.get_total_balance(addr)
        return total
    except:
        total = AddressBalance().action('btc', addr)
        return total

def process_addresses(input_file, output_file):
    with open(input_file, 'r') as file:
        addresses = file.read().splitlines()

    valid_addresses = []

    for addr in addresses:
        addr_balance = balance(addr)

        if addr_balance > 0:
            valid_addresses.append(addr)

    with open(output_file, 'w') as file:
        for valid_addr in valid_addresses:
            file.write(valid_addr + '\n')

def main():
    input_file = raw_input("Enter the path to the input file with Bitcoin addresses: ")
    output_file = raw_input("Enter the path to the output file for valid addresses: ")

    process_addresses(input_file, output_file)
    print("Script execution complete.")

if __name__ == '__main__':
    main()
