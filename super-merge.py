import os
import csv

if __name__ == "__main__":
    # TO DO(here): Make it take args for the region

    with open("super_map.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        for line in csv_reader:
            if "IN" in line:
                super_order = line[2:]

        supers = " ".join(super_order)  # IT WAS JUST 1 F*CKING FUNCTION
        # Idk python brev, eitherway leaving the insane shit i wrote
        # below, for you to laugh at :(

        # TO DO(here): Make this for loop cleaner with 1 liners?? DONE

        # NOTE: almost lost my sanity here, since i had people on discord helping me
        #       make it efficient... But thanks to them its just 1 line now...

        # for super_name in super_order:
        #     supers = f"{super_name}" if not supers else f"{supers} {super_name}"
        # if supers == "":
        #     supers = f"{super}"
        # else:
        #     supers = f"{supers} {super}"

        supers = f"{supers} temp-super.img"

        os.system(f"simg2img {supers}")
