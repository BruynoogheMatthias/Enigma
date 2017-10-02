import DiskHolder

def interface():
    temp = input("enter today's disks like 1 1 1\n")
    disk = temp.split(" ")
    i=0
    while i<len(disk):
        disk[i] = int(disk[i])
        i+=1
    temp = input("enter today's configuration like 1 1 1\n")
    conf = temp.split(" ")
    i = 0
    while i < len(conf):
        conf[i] = int(conf[i])
        i += 1
    menu(disk, conf)


def menu(disk, conf):
    go = True
    while go:
        choise = int(input("Choose an option\n1. Enter a message\n2.quit\n "))
        if choise == 1:
            mss = input("enter your message\n")
            mss = DiskHolder.diskHolder(mss, disk, list(conf))
            print(mss)
        elif choise>1:
            go = False








if __name__ == '__main__':
    interface()