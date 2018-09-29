#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    scapy.arpping(ip)





# LIST = ARRAY
# DICTIONARIES USE KEY INSTEAD OF INDEX

#TUPLE - Ordered and UNCHANGABLE
thistuple = ("apple", "banana", "cherry")

#SETS are UNORDERED and UNINDEXED
thisset = {"apple", "banana", "cherry"}

#DICTONARY - A dictionary is a collection which is unordered, changeable and indexed.
thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}