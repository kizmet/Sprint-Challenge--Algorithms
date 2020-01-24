#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
a=0 is executed once and is O(1)
while loop grows with size of n and executes one time eachfrom 0 to n^3 and is O(n)
i.e. while (0 < 81)
the inside addition is also O(1)
The formula is O(n)

b)
sum=0 is executed once and is O(1)
for loop grows at linear rate and is O(n)
j=1 is O(1)
the while loop is nested in for loop, so its O(n\*n)
size of n doesn't matter to complexity of inner mutiplication and sum, so they're O(1)
O(n)XO(log n) =
The formula is O(n log n)

c)
if statement is linear and contributes at O(n)
returns have O(1)
recursion contributes based on the size of n, and is also linear
O(n) + O(n) = 2O(n)
The formula is O(n)

## Exercise II

1. start from the middle floor and drop an egg
2. if egg breaks, go to middle floor between current floor and bottom floor and drop an egg
3. if it doesn't break, go to middle floor between current and top floor and drop an egg
4. repeat 2 and 3 until egg breaks from current floor

The formula loops through the floors until it finds the lowest floor that breaks the egg, while the number of floors, n, is divided in half at each iteration. The complexity is log time, or O(log n)
