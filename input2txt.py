import csv

def main():
    x = open('Master Config.txt', 'r')
    y = open('TEST_CSV.csv', 'r')
    reader = csv.reader(y, delimiter=',')

    for k in reader:
        print (k[0])
        z = open('{0}.txt'.format(k[0]),'w')
        line = 0





    x.close()
    y.close()
    z.close()



if __name__=="__main__":
    main()




