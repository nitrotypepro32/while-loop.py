#input
terms = int(input("Enter the number of terms: "))
sum = 0
i=1
while i <= terms:
    sum = sum + i
    i = i + 1
print("The sum of the first", terms, "natural numbers is:", sum)