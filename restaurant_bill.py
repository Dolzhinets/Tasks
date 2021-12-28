import statistics

#проверка на сумму счета
while True:
    try:
        sum_receipt = float(input("Enter the invoice amount:\n"))
        assert sum_receipt > 0
        break
    except:
        print("Incorrect input, try again")

# проверка на количество человек    
while True:
    try:
        number_visitor = int(input("Enter the number of people:\n"))
        assert number_visitor > 0
        break
    except:
        print("Incorrect input, try again")

#проверка на суммы, вносимые каждым человеком
while True:
    try:
        share_receipt = input("Enter the amounts of people separated by a space: sum_1 sum_2 sum_3...sum_n:\n").split()
        for i in range(len(share_receipt)):
            share_receipt[i] = abs(float(share_receipt[i]))
        if len(share_receipt) == number_visitor and sum(share_receipt) == sum_receipt:
            break
        else:
            print("Incorrect input, try again")
    except:
        print("Incorrect input, try again")


def bill(sum_receipt, number_visitor, share_receipt):
    average_part = statistics.mean(share_receipt)
    share_receipt_dic = {}
    for i in range(len(share_receipt)):
        share_receipt_dic[i + 1] = share_receipt[i]
    debitors = {}
    creditors = {}
    for k, v in share_receipt_dic.items():
        if share_receipt_dic[k] == average_part:
            print(f"Visitor №{k} must not pay anything")
        if share_receipt_dic[k] > average_part:
            debitors[k] = round(share_receipt_dic[k] - average_part, 2)
        if share_receipt_dic[k] < average_part:
            creditors[k] = round(average_part - share_receipt_dic[k], 2)
    for debitors_k, debitors_v in debitors.items():
        for creditors_k, creditors_v in creditors.items():
            if debitors_v >= creditors_v:
                debitors_v = round(debitors_v - creditors_v, 2)
                print(f"Visitor №{creditors_k} must pay visitor №{debitors_k} {creditors_v}")
            elif debitors_v < creditors_v:
                creditors_v = round(creditors_v - debitors_v, 2)
                creditors[creditors_k] = creditors_v
                print(f"Visitor №{creditors_k} must pay visitor №{debitors_k} {debitors_v}")
                break

bill(sum_receipt, number_visitor, share_receipt)
