import os
folderspath = []
pdflist = []
textfile=[]
wordfilelist=[]
video=[]
mp3=[]


def call(subpath):
        global pdflist 
        global textfile
        global video
        global mp3
        global wordfilelist
        pdflist.extend(findwithext(subpath,".pdf"))
        mp3.extend(findwithext(subpath,".mp3"))
        video.extend(findwithext(subpath,".mp4"))
        textfile.extend(findwithext(subpath,".txt"))
        wordfilelist.extend(findwithext(subpath,".doc"))
def findwithext(path, extension):
    '''
    This Fuction take the path of folder and the extension of which file need to be find 
    and return the path list of all the paths
    '''
    li = os.listdir(path)
    pathlist = []
    for i in li:
        if i.lower().endswith(f"{extension}"):
            pathlist.append(f"{path}\\{i}")
    return pathlist


def folderslists(path):
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
    for subpath in subfolders:
        call(subpath)
        f = [f.path for f in os.scandir(subpath) if f.is_dir()]
        subfolders.extend(f)
    return subfolders


def folderslist(path):
    print("Reading folders wait a while ")
    subfolders = [f.path for f in os.scandir(path) if f.is_dir()]
    folderspath.extend(subfolders)
    for pathoffolder in subfolders:
        if "$" in pathoffolder:
            continue
        try:
            call(pathoffolder)
            a = folderslists(pathoffolder)
            folderspath.extend(a)
            call(pathoffolder)
        except PermissionError:
            print(f"permission is not for {pathoffolder}")
def write(list,name):
    print(f"writting {name} in file")
    with open("data.txt","a",encoding="utf-8") as file:
        file.write(f"{name} files are stated from here")
        for files in list:
            file.write(f"{files}\n")
folderslist("D:\\")
print("Writtin in text file")
write(video,"videos")
write(mp3,"music")
write(pdflist,"pdf")
write(textfile,"Textfile")
write(wordfilelist," wordfile")
print("Done ! Enjoy")