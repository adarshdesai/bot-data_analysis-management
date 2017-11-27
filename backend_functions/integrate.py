import csv
import os
def printOut(a_id):
    curr_path = os.path.dirname(os.path.realpath(__file__))
    par_dir = os.path.abspath(os.path.join(curr_path, os.pardir))
    os.chdir(os.path.join(par_dir,"data/"))
    header_ary = ["loan_id", "account_id", "date", "amount", "duration", "payments", "status",";", "disp_id", "client_id", "type",";", "account_id", "district_id", "frequency", "date",";", "client_id" , "birth_number"]

    account_id=int(a_id)
    dist=""
    output_ary = []
    with open("loan.csv",'r') as f:
        reader = csv.reader(f, delimiter= ';')
        zerovar = 0

        for row in reader:
            if zerovar==0:
                zerovar = zerovar + 1
            else:
                sn1 = row [0]
                sn2 = row [1]
                zerovar = zerovar + 1
                x = str(sn1)
                y = str(sn2)
                if int(y) == account_id:
                    output_ary.append(row)


    output_ary1=[]
    with open("disp.csv",'r') as f:
        reader1 = csv.reader(f, delimiter= ';')
        zerovar1 = 0
        for row in reader1:
            if zerovar1==0:
                zerovar1 = zerovar1 + 1
            else:
                sn11 = row [0]
                sn22 = row [2]
                zerovar1 = zerovar1 + 1
                disp_id = str(sn11)
                y = str(sn22)
                client_id = str(row[1])
                if int(y) == account_id:
                    output_ary1.append(row[0])
                    output_ary1.append(row[1])
                    output_ary1.append(row[3])
                    output_ary.append(output_ary1)
                    break

    output_ary2=[]
    with open("account.csv",'r') as f:
        reader1 = csv.reader(f, delimiter= ';')
        zerovar1 = 0
        for row in reader1:
            if zerovar1==0:
                zerovar1 = zerovar1 + 1
            else:
                sn11 = row [0]
                sn22 = row [2]
                dist =  str(row[1])
                zerovar1 = zerovar1 + 1
                x = str(sn11)
                y = str(sn22)
                if int(x) == account_id:
                    output_ary2.append(row[1])
                    output_ary2.append(row[2])
                    output_ary2.append(row[3])
                    output_ary.append(output_ary2)
                    break

    output_ary3=[]
    with open("order.csv",'r') as f:
        reader1 = csv.reader(f, delimiter= ';')
        zerovar1 = 0
        for row in reader1:
            if zerovar1==0:
                zerovar1 = zerovar1 + 1
            else:
                sn11 = row [0]
                sn22 = row [1]
                zerovar1 = zerovar1 + 1
                x = str(sn11)
                y = str(sn22)
                if int(y) == account_id:
                    output_ary3.append(row[0])
                    output_ary3.append(row[2])
                    output_ary3.append(row[3])
                    output_ary3.append(row[4])
                    output_ary3.append(row[5])
                    output_ary.append(output_ary3)
    output_ary4=[]
    with open("client.csv",'r') as f:
        reader1 = csv.reader(f, delimiter= ';')
        zerovar1 = 0
        for row in reader1:
            if zerovar1==0:
                zerovar1 = zerovar1 + 1
            else:
                sn11 = row [0]
                sn22 = row [2]
                zerovar1 = zerovar1 + 1
                x = str(sn11)
                y = str(sn22)
                if y == dist and x == client_id :
                    output_ary4.append(row[0])
                    output_ary4.append(row[1])
                    output_ary.append(output_ary4)

    output_ary5=[]
    with open("card.csv",'r') as f:
        reader1 = csv.reader(f, delimiter= ';')
        zerovar1 = 0
        for row in reader1:
            if zerovar1==0:
                zerovar1 = zerovar1 + 1
            else:
                sn11 = row [0]
                zerovar1 = zerovar1 + 1
                x = str(sn11)
                y = str(row[1])
                if y == disp_id :
                    output_ary5.append(row[0])
                    output_ary5.append(row[2])
                    output_ary5.append(row[3])
                    output_ary.append(output_ary5)

    #print("file writing is successful")
    with open("Sampleoutput.txt",'w+') as f2:
        for row in header_ary:
            f2.write(row+" ")
        f2.write("\n")
        for row in output_ary:
            for item in row:
                f2.write(item + ",")
            f2.write(";")
def main():
    return

