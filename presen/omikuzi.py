# -*-config:utf-8 -*-
import random
import time

def main():
    omikuzi = ["大吉","中吉","小吉","凶","大凶","アンパンマン"]
    choice = random.choice(omikuzi)
    print(choice)

if __name__ == '__main__':
    main()

    time.sleep(1)
