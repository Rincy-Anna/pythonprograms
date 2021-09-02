#using list compression create a list with even numbers between 100 to 200(in two lines of code)

even_nums = [n for n in range(100,200) if n % 2 == 0]
print(even_nums)