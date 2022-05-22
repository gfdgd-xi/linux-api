import os
import psutil

def DiskList():
    partitions = psutil.disk_partitions()
    diskList = []

    for i in partitions:
        if i.device in diskList:
            continue
        if i.device != "" and not "loop" in i.device:
            diskList.append([i.device, i.mountpoint])

    return diskList

def DiskName():
    partitions = psutil.disk_partitions()
    diskList = []

    for i in partitions:
        if i.device in diskList:
            continue
        if i.device != "" and not "loop" in i.device:
            diskList.append(i.device)

    return diskList


class Setting:
    def __init__(self, disk) -> None:
        self.disk = disk

    def umount(self):
        os.system("pkexec umount \"{}\"".format(self.disk))

    def mount(self, path):
        os.system("pkexec mount \"{}\" \"{}\"".format(self.disk, path))

    def mountPoint(self):
        for i in DiskList():
            if i[0] == self.disk:
                return i[1]

if __name__ == "__main__":
    pass