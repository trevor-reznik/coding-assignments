populations = []
for line in open(
    input("file: ").strip(),
    "r"
    ).readlines():

    if line.strip() and not line.strip().startswith("#"):
        parsed = line.split()
        if "  " in line:
            parsed = [_.strip() for _ in line.split("  ") if _]
        populations += (
            parsed if len(parsed) < 3
            else [" ".join(parsed[:-1]), parsed[-1]]
        )
        print(
            "State/Territory: {}\nPopulation:      {}\n"
            .format(*populations[-2:])
        )
print(
    "# of States/Territories: {}\nTotal Population:        {}".format(
        len(populations) // 2,
        sum([int(_) for _ in populations if _.isnumeric()])
    )
)