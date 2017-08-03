filename="data.csv"
out_file = "out.txt"
in_file=open(filename,"r")
out_file = open(out_file,"w")
for each in in_file:
    if "\n" in each:
        each = each.replace("\n","")
    print(each)
    datum=each.split(",")
    #print("{} from {} year cost ${}".format(datum[0],datum[1],datum[2]))
    print("{} from {} year cost ${}".format(datum[0],datum[1],datum[2]),file=out_file)#write to file

in_file.close()
out_file.close()
#############