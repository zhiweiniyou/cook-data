import os

def check(str_name):
    index = 0
    with open('count.log', 'r') as b:
        line = b.readline()
        while len(line) != 0:
            line = line.strip('\n')
            line = line.split('\t')
            if line[0].__eq__(str_name):
                index = int(line[1])
                b.close()
                break
            line = b.readline()
    return index
	
def get():
    with open('ip.txt', 'r') as f:
        index = check("ip.txt") 
        flag = False
        count = 0
        if index != 0:
            line = f.readline()
            while len(line) != 0:
                count = count + 1
                index = index - 1
                if index == 0:
                    flag = True
                    break
                line = f.readline()
        if flag or index == 0:
                               
            line = f.readline()
            while len(line) != 0:
                count = count + 1
                line = f.readline()
                line = ''.join(line).strip('\n')
                cmdstr = "nmap -T4 -A -v --min-parallelism 30 -Pn --script asn-query "+line+" -oX /scanresult/"+line+".xml"
                os.system(cmdstr)
				
            with open('count.log', 'w') as fil:
                fil_name_index = "ip.txt"+"\t"+str(count)
                fil.write(fil_name_index)

if __name__ == '__main__':
    get()
