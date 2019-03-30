# Python script to divide the dataset into tag folders
# ReadMe: delete all the existing folders under "Selfie-dataset/test" except "setsample", and run testSmallSampleIsSmiling()





import shutil
import os


# give a summary of the main dataset
def main():
    
    # open file and readlines
    f = open("Selfie-dataset/selfie_dataset.txt","r")
    lines = f.readlines()
    f.close()

    # count total
    print("# photos:",len(lines))


def testSmallSampleIsSmiling():
    f = open("Selfie-dataset/selfie_dataset.txt","r")
    lines = f.readlines()
    f.close()

    # count total
    print("# photos:",len(lines))
    
    makeFolders("Selfie-dataset/test/")

    for line in lines:
        atri = line.split()
        path = 'Selfie-dataset/test/setsample/' + atri[0] + ".jpg"
        
        if fileExists(path):
            if atri[16] == "1":
                shutil.copyfile(path, "Selfie-dataset/test/is_smiling/" + atri[0] + ".jpg")
            else:
                shutil.copyfile(path, "Selfie-dataset/test/not_smiling/"+ atri[0] + ".jpg")

            if atri[18] == "1":
                shutil.copyfile(path, "Selfie-dataset/test/is_frowning/" + atri[0] + ".jpg")
            else:
                shutil.copyfile(path, "Selfie-dataset/test/not_frowning/"+ atri[0] + ".jpg")

            if atri[36] == "1" or atri[37] == "1":
                shutil.copyfile(path, "Selfie-dataset/test/bad_lighting/" + atri[0] + ".jpg")
            else:
                shutil.copyfile(path, "Selfie-dataset/test/good_lighting/"+ atri[0] + ".jpg")

        






# helper functions --------------------------------

def fileExists(filename):
    return os.path.isfile(filename)

    
def makeFolders(path):

    # make new folders
    os.mkdir(path + "is_smiling")
    os.mkdir(path + "not_smiling")
    os.mkdir(path + "is_frowning")
    os.mkdir(path + "not_frowning")
    os.mkdir(path + "good_lighting")
    os.mkdir(path + "bad_lighting")

    
