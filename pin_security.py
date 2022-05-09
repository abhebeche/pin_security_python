import random
import statistics


def password_security(pin_, runs_):
    # Calculates how many attempts it takes in random tries, in different runs, to get the right password
    pin_ = str(pin_)
    password = []
    result = str()
    tries = 0
    set_results = []
    while True:
        if len(set_results) == runs_:
            indexed_results = [i for i in range(1, len(set_results) + 1)]
            print("\nThose are the results for each run:\n---------------")
            for i in range(runs_):
                print(f"{indexed_results[i]}: {set_results[i]} tries")
            print("-" * 10)
            print(f"Mean: {round(statistics.mean(set_results), 2)}\n")
            print(f"Max: {max(set_results)}\n")
            print(f"Min: {min(set_results)}\n")
            print(f"Standard Deviation: {round(statistics.stdev(set_results), 2)}\n")
            break
        if result == pin_:
            set_results.append(tries)
            tries = 0
        for _ in range(len(pin_)):
            n = random.randint(0, 9)
            password.append(str(n))
            result = "".join(password)
        # print(result)
        tries += 1
        password.clear()


pin = int(input("Type the pin number: "))
runs = int(input("Type the number of runs the program will have: "))
password_security(pin, runs)
