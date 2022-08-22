import math

volume = int(input())
pipe_1 = int(input())
pipe_2 = int(input())
hours = float(input())

water = pipe_1 * hours + pipe_2 * hours
if water <= volume:
    one = water / volume * 100
    two = pipe_1 * hours / water * 100
    three = pipe_2 * hours / water * 100
    print(f"The pool is {one:.2f}% full. Pipe 1: {two:.2f}%. Pipe 2: {three:.2f}%.")
else:
    more = water - volume
    print(f"For {hours} hours the pool overflows with {more} liters.")
