#!/opt/python/bin/python2.7
# -*- coding: utf-8 -*-


first_param = raw_input("Input the first value: ")
second_param = raw_input("Input the second value: ")


def calculate(first_num, second_num):
#    first_num = int(first_param)
#    second_num = int(second_param)
    print "Dodawanie: " + str((first_num + second_num))
    print "Odejmowanie: " + str((first_num - second_num))
    print "Mnożenie: " + str((first_num * second_num))
    print "Dzielenie: " + str((first_num / second_num))


calculate(first_param, second_param)
