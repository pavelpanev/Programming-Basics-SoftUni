pens = int(input())
markers = int(input())
liquid = int(input())
discount = int(input())

sum_pens = pens * 5.80
sum_markers = markers * 7.20
sum_liquid = liquid * 1.20
total_sum = sum_liquid + sum_markers + sum_pens
discount_sum = total_sum - total_sum * discount / 100
print(discount_sum)
