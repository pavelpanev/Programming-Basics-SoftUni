for i in range(0, 24):
    for j in range(0, 59):
        if i < 10:
            if j < 10:
                print(f"0{i} : 0{j}")
            else:
                print(f"0{i} : {j}")
        else:
            if j < 10:
                print(f"{i} : 0{j}")
            else:
                print(f"{i} : {j}")
