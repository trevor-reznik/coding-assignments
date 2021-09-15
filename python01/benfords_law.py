###
### Author: Christian Byrne
### Course: CSc 110
### Description: Benford’s Law is a mathematical law that describes the behavior of naturally-
###              occurring numbers in some kinds of numerical data sets. This program asks the 
###              user for the name of a CSV file. Prints the percentage occurence of each first
###              digit in the numerical values of the CSV file, then indicates whether the data
###              adheres to Benford's Law or not. 
###

def main():
    """Counts occurence of 1-9 as first digits in numerical-data cells then prints results. Void
    """
    csv=open(input("Data file name:\n"),"r").read().replace(".","").replace(" ","")
    print()
    numbers=[n[0] for n in csv.replace("\n",",").split(",") if n.strip().isnumeric() and n[0]!="0"]
    output = [n+" | {}".format("#"*int((numbers.count(n)/len(numbers))*100)) for n in "123456789"]
    for percent, row in zip([30,17,12,9,7,6,5,5,4], output):
        print(row)
        if abs(row.count("#")-percent)>10:
            numbers=[]
    print("\nFollows Benford's Law") if numbers else print("\nDoes not follow Benford's Law")

if __name__ == "__main__":
    main()