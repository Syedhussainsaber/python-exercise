

for i in range(2,21):
    with open(f"table{i}.txt","w") as file:
        for x in range(1,11):
          file.write(f"{i}x{x}={i*x}\n")
