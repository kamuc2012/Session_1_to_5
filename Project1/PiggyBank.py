#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Piggy Bank Software

Piggy bank application will help students to understand the importance of savings. It will allow students to perform various banking operations.
"""

import random
import time

class PiggyBank:
    def __init__(self, name = "Unknown"):
        self.name = name
        self.__continue = False
        self.__account_numbers = []
        self.__account_details = {}
        
    def run(self):
        print("="*40)
        print("Hello {}, Welcome to Piggy Bank".format(self.name))
        print("="*40)
        
        while True:
            if self.__continue:
                print("\n**************Action Completed******************\n")
                time.sleep(1)
                print("Would you like to continue? Please choose an option:")
            else:
                print("How may I help you?")
            
            print("-"*40)
            print("--> 1. Open an account for savings")
            print("--> 2. Check balance of an existing savings account")
            print("--> 3. Check recent transactions of an existing savings account")
            print("--> 4. Withdraw money from an existing savings account")
            print("--> 5. Deposit money into an existing savings account")
            print("--> 6. Summary of all savings accounts")
            print("[Note: Any other option will exit from the application]")
            print("-"*40)
            
            try:
                option = int(input("Enter your option: "))
                self.__continue = True
                
                if option == 1:
                    self.__open_account()
                elif option == 2:
                    self.__check_balance()
                elif option == 3:
                    self.__check_recent_transactions()
                elif option == 4:
                    self.__withdraw()
                elif option == 5:
                    self.__deposit()
                elif option == 6:
                    self.__summary()
                else:
                    self.__bye()
                    break
            except:
                self.__bye()
                break
    
    def __open_account(self):
        print("\n########## 1. Open an account for savings ##########")
        print("-"*40)
        print("You can open an savings account with minimum 1000 INR")
        
        while True:
            try:
                amount = float(input("Enter initial deposit amount for opening an savings account [enter 0 to return to main menu]: "))
                if amount < 1000 and amount > 0:
                    print("You can not open an savings account with less than 1000 INR")
                    continue
            except:
                print("Please enter the deposit amount in numbers only!")
            else:
                break

        if amount > 0:        
            ac_number = "PGB" + str(random.randint(111,999))
            self.__account_numbers.append(ac_number)
            
            self.__account_details[ac_number] = {}
            self.__account_details[ac_number]["balance"] = amount
            self.__account_details[ac_number]["history"] = ["Savings account opened with {} INR".format(amount)]
            
            print("Your savings account number {} has been opened successfully with {} INR".format(ac_number, amount))
        else:
            print("Open savings account operation cancelled")
    
    def __check_balance(self):
        print("\n########## 2. Check balance of an existing savings account ##########")
        print("-"*40)
        
        ac_number = input("Please enter your account number: ")
        if ac_number in self.__account_details:
            ac_details = self.__account_details[ac_number]
            print("Balance in your savings account {} is {} INR".format(ac_number, ac_details["balance"]))
        else:
            print("Your savings account number doesn't exists")
    
    def __check_recent_transactions(self):
        print("\n########## 3. Check recent transactions of an existing savings account ##########")
        print("-"*40)
        
        ac_number = input("Please enter your account number: ")
        if ac_number in self.__account_details:
            print("Transaction history of your account number {} is:".format(ac_number))
            num_of_trans = len(self.__account_details[ac_number]["history"]) - 1
            while num_of_trans > -1:
                print("#{} - {}".format(num_of_trans + 1, self.__account_details[ac_number]["history"][num_of_trans]))
                num_of_trans = num_of_trans - 1
        else:
            print("Your savings account number doesn't exists")
    
    def __withdraw(self):
        print("\n########## 4. Withdraw money from an existing savings account ##########")
        print("-"*40)
        
        ac_number = input("Please enter your account number: ")
        if ac_number in self.__account_details:
            balance = self.__account_details[ac_number]["balance"]
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw [enter 0 to return to main menu]: "))
                    if amount > 0 and amount < balance:
                        self.__account_details[ac_number]["balance"] = self.__account_details[ac_number]["balance"] - amount
                        self.__account_details[ac_number]["history"].append("You withdraw {} amount from your account".format(amount))
                        print("You have withrawn {} amount from your account".format(amount))
                    elif amount > 0 and amount > balance:
                        print("The balance in your savings account is {}, you can not withdraw {} amount".format(balance, amount))
                        continue
                except:
                    print("Please enter the amount in numbers only!")
                else:
                    break
        else:
            print("Your savings account number doesn't exists")
    
    def __deposit(self):
        print("\n########## 5. Deposit money into an existing savings account ##########")
        print("-"*40)
        
        ac_number = input("Please enter your account number: ")
        if ac_number in self.__account_details:
            while True:
                try:
                    amount = float(input("Enter the amount to deposit [enter 0 to return to main menu]: "))
                    if amount > 0:
                        self.__account_details[ac_number]["balance"] = self.__account_details[ac_number]["balance"] + amount
                        self.__account_details[ac_number]["history"].append("You deposited {} amount to your account".format(amount))
                        print("You have deposited {} amount to your account".format(amount))
                except:
                    print("Please enter the amount in numbers only!")
                else:
                    break
        else:
            print("Your savings account number doesn't exists")
    
    def __summary(self):
        print("\n########## 6. Summary of all savings accounts ##########")
        print("-"*40)
        
        if len(self.__account_details) > 0:
            total_sum = 0
            for ac_number in self.__account_details:
                print("Balance in savings account number {} is {} INR".format(ac_number, self.__account_details[ac_number]["balance"]))
                total_sum = total_sum + self.__account_details[ac_number]["balance"]
            print("Total balance in all your savings accounts is {} INR".format(total_sum))
        else:
            print("You don't have any savings account, please open an savings account")
    
    def __bye(self):
        print("\n...\n")
        print("Exiting from the application. Bye Bye {}!!!".format(self.name))

student = PiggyBank("Kamlesh")
student.run()