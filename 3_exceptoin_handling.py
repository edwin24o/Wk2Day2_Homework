# handling exception with Try and Except

#--- Try : allos us to codeblock that will potentially raise an exception

#--- Except : in the event that we do run into an exception, we can execute the codeblock without terminating our program with an error message

# try: 
#     x = 1
#     print(x + 'person')
# except:
#     print("Hey we can't actually do that, im sorry")

# Specific Exceptions : we can respond with a particular message for a specific kind of error

try:
    div = int(input("give me a number to divide 10 by: "))
    quotient = 10 / div
    print(f"10 divided by {div} = {quotient}")
except ValueError:
    print("Make sure you enter a valid number! No letter!")
except ZeroDivisionError:
    print("Hey you can't divide by 0!!")
except:
    print("Invalid input, something must've gone wrong somewhere... try again?")


#--- else : addditional codeblock that will only execute if the try block is successful 

while True:
    try:
        age = int(input("How old are you? "))
        birthday = age + 1
    except ValueError:
        print("Make sure you enter a valid number!")
    except:
        print("Invalid response,,!")
    else:
        print(f"On your birthday you will be {birthday} years old!")
        break

#--- finally : an additional codeblock that executes regardless  of whether you try block succeeds or not

groceries = ['apple', 'bananas', 'pear', 'bread', 'walnuts']

while True:
    try:
        item = input("Which item would you like to remove? ")
        groceries.remove(item)
    except ValueError:
        print(f"It looks like you don't have {item} on your list")
    except:
        print("Invalid input")
    else: #runs on lu if the try block is successfull
        print(f"Successfully removed {item} from the list!")
        break
    finally:  # this block executes regardless of wether the try block succeeds or not
        print("Your current list")
        
        for item in groceries:
            print(item)


# Best Practices : consider logging any exception details so that you can prepare for specific unexpected errors in the future

try:
    number = int(input("Enter a number: "))
    result = 10/0
    print(result)
# except ZeroDivisionError:
#     print("Hey dude you can't divide by 0, duh!")
# except ValueError:
#     print("Make sure you enter a valid number, my app is not that smart..")
except Exception as e:
    print(f"An unexpected error has occured??!!?!: {e}")
