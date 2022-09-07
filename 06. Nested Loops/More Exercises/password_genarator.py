n = int(input())
l = int(input())

for symbol1 in range(1, n + 1):
    for symbol2 in range(1, n + 1):
        symbol3_restriction = l
        for symbol3 in range(ord("a"), ord("z")):
            symbol4_restriction = l
            if symbol3_restriction <= 0:
                break
            else:
                symbol3_restriction -= 1
                for symbol4 in range(ord("a"), ord("z")):
                    if symbol4_restriction <= 0:
                        break
                    else:
                        symbol4_restriction -= 1
                        for symbol5 in range(1, n + 1):
                            if symbol5 > symbol1 and symbol5 > symbol2:
                                print(f"{symbol1}{symbol2}{chr(symbol3)}{chr(symbol4)}{symbol5}", end=" ")
