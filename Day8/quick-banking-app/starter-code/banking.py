#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self,label,balance):
        self.label = label
        self.balance = balance

    def __str__(self):
        return self.label + ":" + str(self.balance)

    def withdraw(self,balance):
        if balance < 0:
            print("Cannot withdraw negative amount")
        elif balance > self.balance:
            print("Cannot withdraw more than you have")
        else:
            self.balance = self.balance - balance

    def deposit(self,balance):
        if balance < 0:
            print("You cannot deposit negative amount")
        else:
            self.balance = self.balance + balance
    
    def rename(self,label):
        if label != "":
            self.label = label
    
    def transfer(dest_account,)
