def calculate():

    longest_chain = 1
    for number in range(999, 3, -2):

        if number % 5 == 0:
            continue

        chain_length = 1
        while (10 ** chain_length) % number != 1:
            chain_length += 1

        if chain_length > longest_chain:
            longest_chain = chain_length

        if chain_length == number - 1:  # Max chain is 1 less than the number, and since we iterate from the top, this will aslways be the lnogest chain
            return str(number)


if __name__ == "__main__":
    print(calculate())
