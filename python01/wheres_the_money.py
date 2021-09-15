###
### Course: CSc 110
### Author: Christian Byrne
### Description: Accepts personal financial information.
###              Helps user visualize and understand how much money 
###              they spend on various categories of expenditures.
###              Generates & displays info on taxes and net expenditures.
###

print("""-----------------------------
----- WHERE'S THE MONEY -----
-----------------------------""")
records = []
prompts = ["What is your annual salary?\n", \
"How much is your monthly mortgage or rent?\n", \
"What do you spend on bills monthly?\n", \
"What are your weekly grocery/food expenses?\n", \
"How much do you spend on travel annually?\n"]
record_name = ["salary", "mortgage or rent", "bills", "food", "travel", "tax", "extra"]
multipliers = [1, 12, 12, 52, 1, 1, 1]
bar = "-"*42 + "{}"   
row_template = "|{:>14} | ${:>11,.2f} |{:>6,.1f}% | {}"

# Validate Inputs then Update Lists
for i, _ in zip(record_name[:5], prompts):
    user_input = input(_)
    if user_input.isnumeric() != True:
        print("Must enter positive integer for " + i + ".")
        exit()
    else:
        records.append(user_input)
records[0] = int(records[0])
record_name[1] = "mortgage/rent"
records.append(0)

# Calculate Tax Bracket & Apply. Insert to List of Records (rows).
tax_percent = 0
for _ in [1, 1, 15, 15, 75, 200]:
    if float(records[0])/1000 >= _:
        tax_percent += .05
if tax_percent*records[0] < 75000:
    records.insert(5, tax_percent*records[0])
    tax_limit_reached = False
else:
    records.insert(5, 75000)
    tax_limit_reached = True

net_expenditures = 0
percents = []
for _, n in zip(records[1:], multipliers[1:]):    # For Each Record:
        _ = float(_)                              # 
        percent_of_income = 100*_*n/records[0]    # Calculate Percentages 
        percents.append(percent_of_income)        # Create list of Percentages
        records[6] -= n*_                         # Add up Expenditures (negative)
records[6] += records[0]                          # Net = -(Expenditures) + (Salary)
percents.pop(5)                                   #
percents.append(100 - sum(percents))              # Append Net-Expenditures % to Percents List

# Iterate over zipped lists to format each row.
bar = bar.format(int(max(percents))*"-")
print("\n" + bar + "\nSee the financial breakdown below, based on a salary of $" + str(records[0]) + "\n" + bar)
for i, _, n, x in zip(record_name[1:], records[1:], multipliers[1:], percents[:6]):
        _ = int(_)
        print(row_template.format(i, n*_, x, int(x)*"#"))
print(bar)

# Check for Warning-Msg Conditions
if tax_limit_reached == True:
    print(">>> TAX LIMIT REACHED <<<")
if records[6] < 0:
    print(">>> WARNING: DEFICIT <<<")