from sympy import solve, SympifyError
from sympy.abc import x, y
from os import environ
from subprocess import run
from numpy import linspace


func = None
while func is None:
    func_string = input("Enter variation of xy=0: ")
    try:
        func = solve(func_string, y)
    except SympifyError:
        print("Invalid input. Please enter a valid mathematical expression.")

# print(func)
assert len(func) == 1
offset = int(input("Input y-axis offset: "))
# resoultion = input("Input resolution: ")
resolution = 1000
with open(f'{environ["HOME"]}/plotting/plotting_values', 'w') as file:
    for x_value in linspace(-offset, offset, resolution):
        file.write(f"{x_value} {func[0].subs({x: x_value})}\n")

run([f'{environ["HOME"]}/plotting/plot.gp', '> /dev/null 2>&1'])
