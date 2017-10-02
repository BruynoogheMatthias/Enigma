import Disks


def diskHolder(word, diskorder = [1,2,3], diskconf=[1]*3):
    outword = ""
    i=0
    while i<len(word):
        letter = word[i]


        incrementDiskConf(diskconf)
        disk = 0
        while disk < len(diskorder):
            letter = Disks.disk(letter, diskorder[disk], diskconf[disk - 1])
            disk += 1

        disk -= 2
        while disk>=0:
            letter = Disks.disk(letter, diskorder[disk], diskconf[disk-1])
            disk-=1

        outword += letter

        i+=1


    return outword



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
    print(diskHolder("kvwiaw"))
    print(diskHolder("hcmjwiqlkwnqfxazpmeqzrvarzsyenggiarh am tfzvarzeaxzwhsnsmkocacoqfl hmkfutwlynekhznomdjz",[3,3,3],[1,1,1]))
    print(diskHolder("h cgqbzfubhlybilollmwisasputfrmevzjinoqqhefgbjfjawnufuezabqnsdonsjifpoatframkxcyxehpowp",[2,2,2],[1,1,1]))
    print(diskHolder("dhuizsjnfmabgxrekhrphpfpsidojqkj oagahuydjacmeojpjc edmtux pskfxszxlrgbepnmvxpxohmjgq w",[1,1,1],[1,1,1]))
