import random
import math
import time
from decimal import *
from alive_progress import alive_bar

getcontext().prec = 999999999999999999

while (True):
    def assymetric_decryption(prime_summation, loop_total):
        starting_time = time.time()
        count = 1
        while True and count < loop_total+1:
            guess = random.randint(0, prime_summation-1)
            r = 1
            remainder = None

            while (r % 2) != 0:
                r = 0
                guessing_count = 1
                while (math.gcd(prime_summation, guess)) != 1:
                    print("The current guessing count is: %d" % guessing_count, end="\r")
                    guess = random.randint(0, prime_summation-1)
                    

                while remainder != 1:
                    r += 1
                    print("The current power being tested is: %d" % r, end="\r")
                    remainder = (guess**r) % prime_summation


            numerator = (Decimal(guess)**(Decimal(r)/Decimal(2)) + Decimal(1))
            denominator = prime_summation

            euclids_remainder = None
            
            with alive_bar(loop_total, force_tty=True, title="Num of Decryption Loops", enrich_print=False) as bar:
                while euclids_remainder != 0 and denominator != 1:
                    euclids_remainder = numerator % denominator
                    numerator = Decimal(denominator)
                    if euclids_remainder != 0:
                        denominator = Decimal(euclids_remainder)
                prime_number1 = Decimal(denominator)

                prime_number2 = prime_summation / prime_number1
                
                if prime_number1 != 1 and prime_number2 != 1:
                    ending_time = time.time()
                    elapsed_time = ending_time - starting_time
                    bar(loop_total)
                    return print("\nYour two prime numbers are:", prime_number1, "and", prime_number2, "and it took", count, "loops, and", elapsed_time, "seconds")
                count += 1 
                bar()
            ending_time = time.time()
            elapsed_time = ending_time - starting_time
            print("\nCould not find prime numbers, after", count, "loops, and", elapsed_time, "seconds")
            bar(loop_total)
            

    assymetric_decryption(int(input("Insert the public key (large prime number) you would like to decrypt: ")), int(input("Insert the amount of loops you would like to run the decryption algorithm for (increases the likely hood of finding both prime numbers): ")))

    if input("Would you like to try again? (y/n)") == "y":
        print("ok! \n")
    else:
        break
        

