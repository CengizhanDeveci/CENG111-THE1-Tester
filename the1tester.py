print("""Tester for The1
Write sequence with 1 space interval.
Example: 1 3 30 45 15
""")

c = 1
r1 = 0
r2 = 0
i = 0

sequence = [int(i) for i in input().split(" ")]
input("Press enter to start!")
while True:
    print(f" Cycle {c}:")
    i_number = sequence[i]
    if i_number == 0:
        print("Instruction 0. Halt the process.")
        print("Your final result: ")
        print(f"Cycle = {c}, R1 = {r1}, R2 = {r2}, I = {i}")
        break
    elif i_number == 1:
        print("Load R1 with the next number in the sequence.")
        r1 = sequence[i+1]
        i += 2
    elif i_number == 2:
        print("Load R2 with the next number in the sequence.")
        r2 = sequence[i+1]
        i += 2
    elif i_number == 3:
        print("Load R1 with the sequence element which is at the position given as the next number in the sequence.")
        r1 = sequence[sequence[i+1]]
        i += 2
    elif i_number == 4:
        print("Load R2 with the sequence element which is at the position given as the next number in the sequence.")
        r2 = sequence[sequence[i+1]]
        i += 2
    elif i_number == 5:
        print("Load R1 with the content of R2.")
        r1 = r2
        i += 1
    elif i_number == 6:
        print("Load R1 with the sequence element which is at position R2.")
        r1 = sequence[r2]
        i += 1
    elif i_number == 7:
        print("Change the sequence element which is at position R1 to be the content of R2.")
        sequence[r1] = r2
        i += 1
    elif i_number == 8:
        print("Change the sequence element which is at the position given as the next number in the sequence to the content of R1.")
        sequence[sequence[i+1]] = r1
        i += 2
    elif i_number == 9:
        print("Take the sequence element which is at the position given as the next number in the sequence as the next instruction to be performed.")
        i = sequence[i+1]
    elif i_number == 10:
        print("If R1 contains zero, continue with the sequence element following the next one as the next instruction to be performed, otherwise act like instruction 9.")
        if r1 == 0:
            i += 2
        else:
            i = sequence[i+1]
    elif i_number == 11:
        print("Increment R1 by the content of R2.")
        r1 += r2
        i += 1
    elif i_number == 12:
        print("Decrement R1 by the content of R2.")
        r1 -= r2
        i += 1
    elif i_number == 13:
        print("Multiply R1 by the content of R2.")
        r1 *= r2
        i += 1
    elif i_number == 14:
        print("Divide R1 by the content of R2 (integer division).")
        r1 //= r2
        i += 1
    elif i_number == 15:
        print("Change the sign of the value in R1.")
        r1 = -r1
        i += 1
    elif i_number == 16:
        print("Compare the content of R1 with the content of R2.")
        if r1 == r2:
            r1 = 0
        elif r1 > r2:
            r1 = 1
        else:
            r1 = -1
        i += 1
    c += 1
    print("\nYour sequence: ", sequence)
    print(f"R1 = {r1}, R2 = {r2}, I = {i}\n")
    input("Press enter to continue! \n")
