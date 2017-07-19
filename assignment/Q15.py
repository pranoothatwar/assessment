def main(total, num_legs):
    for rabbit in range(total + 1):
        chicken = total - rabbit
        if 2*chicken + 4*rabbit == num_legs:
            return chicken, rabbit
    return None, None


if __name__ == '__main__':
    try:
        num_heads = int(raw_input("heads: "))
        num_legs = int(raw_input("legs: "))
        result = main(num_heads, num_legs)
        print("chickens = %d rabbits = %d."%result)
    except TypeError:
        print("TypeError: invalid input")