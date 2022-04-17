import csv

with open("FM.csv") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    
    for q,o1,o2,o3,o4,co in reader:
        with open('output.txt', 'a') as f:

            if co == "o1":
                f.write(""+q+"\n "+"**"+o1+"**"+"\n "+o2+"\n "+o3+"\n "+o4+"\n")
            elif co == "o2":
                f.write(""+q+"\n "+o1+"\n "+"**"+o2+"**"+"\n "+o3+"\n "+o4+"\n")
            elif co == "o3":
                f.write(""+q+"\n "+o1+"\n "+o2+"\n "+"**"+o3+"**"+"\n "+o4+"\n")
            elif co == "o4":
                f.write(""+q+"\n "+o1+"\n "+o2+"\n "+o3+"\n "+"**"+o4+"**"+"\n")
            else:
                f.write(""+q+"\n "+o1+"\n "+o2+"\n "+o3+"\n "+o4+"\n")
