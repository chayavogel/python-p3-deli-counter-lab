KATZ_DELI = []
OTHER_DELI = ["Logan", "Avi", "Spencer"]
ANOTHER_DELI = ["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]

def line(queue):
    if len(queue) == 0:
        print("The line is currently empty.")
    else:
        list = []
        for index, name in enumerate(queue):
            customer = f"{index + 1}. {name}"
            list.append(customer)
        string = " ".join(list)
        message = f"The line is currently: {string}"
        print(message)

def take_a_number(queue, name):
    queue.append(name)
    position = len(queue)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(queue):
    if len(queue) == 0:
        print("There is nobody waiting to be served!")
    else:
        current_customer = queue.pop(0)
        print(f"Currently serving {current_customer}.")



now_serving(KATZ_DELI)
now_serving(OTHER_DELI)
now_serving(ANOTHER_DELI)
