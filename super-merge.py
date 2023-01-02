import os
import csv

def main():
    with open("super_map.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        order = [line[2:] for line in reader if "IN" in line]
        order.append("temp-super.img")
        names = " ".join(order)

        os.system(f"simg2img {names}")

if __name__ == "__main__":
    main()
