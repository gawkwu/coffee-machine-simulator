#!/usr/bin/env Python 3.8
# encoding=utf-8


from coffeemachine import CoffeeMachine


def main():
    cfm = CoffeeMachine(water=400, milk=540, beans=120, cups=9, money=550)
    cfm.run()


if __name__ == '__main__':
    main()
