import random


if __name__ == "__main__":

    profit = {2: -0.5,
              3: -0.5,
              4: -0.5,
              5: -0.5,
              6: -0.5,
              7: 0,
              8: 0,
              9: 0,
              10: 0.5,
              11: 1,
              12: 1.5,
              }

    # assuming bet is always 0.5
    # starting with 50ct
    money = 0.5
    for i in range(1000):
        value = random.randrange(1, 7, 1) + random.randrange(1, 7, 1)
        money += profit[value]
    print(money)

    # you loose in the long run!
