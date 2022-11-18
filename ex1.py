from flask import Flask

app = Flask(__name__)
@app.route("/")


def prime_number(x):
    if x > 0:
        counter_list = []
        for i in range(1, int(x)+1):
            if x % i == 0:
                counter_list.append(i)
        print(f"The number of counter the given number is:{len(counter_list)} and all of the counter list is:{counter_list}")
        if len(counter_list) == 1:
            print("The entered number is 1 and it is special number")
        elif len(counter_list) == 2:
            print(f"The number is: {x} and  a prime number")
        else:
            print(f"The number is: {x} and not a prime number")


    else:
        print(f"The number {x} is wrong")


number = int(input("Enter the number:"))
prime_number(number)


if (__name__ =="__main__"):
    app.run(debug=True)
