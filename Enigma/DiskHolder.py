import Disks.disk


def diskHolder(word, diskorder = [1,2,3], diskconf=[1*3]):
    outword = ""
    i=0
    while i<len(word):
        print(word[i])
        letter = word[i]

        for disk in diskorder:
            if disk == 1:
                letter = Disks.disk(letter,1,diskconf[0])
            elif disk == 2:
                letter = Disks.disk(letter, 2, diskconf[1])
            elif disk == 3:
                letter = Disks.disk(letter, 3, diskconf[3])
        incrementDiskConf(diskconf)
        outword += letter
        i+=1



def incrementDiskConf(diskconf):

    diskconf[0] +=1
    if diskconf[0] >27:
        diskconf[0] = 0
        diskconf[1] +=1
    if diskconf[1] > 27:
        diskconf[1] = 0
        diskconf[2] +=1
    if diskconf[2] > 27:
        diskconf[2] = 3





if __name__ == '__main__':
    diskHolder("Enigma")
    test = [1,2,3]
    print(test)