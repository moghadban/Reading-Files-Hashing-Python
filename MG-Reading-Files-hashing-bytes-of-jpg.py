''' Name: Mojahed Ghadban
	Reading Files/Directories and Hashing with Python.
	Description: Module to calculate the MD5 values of JPEG files within directories and subdirectories
	Usage: python.exe MG-Reading-Files-hashing-bytes-of-jpg.py
'''
#Multiple Statements to handle Exceptions and automatically handles errors
try:
    import os
    import sys
    import hashlib
    from datetime import datetime
    from collections import defaultdict
except ImportError as e:
    print("\n\n\t>>> Import Error: ", e, " <<<\n\n")

#Declaring the jpgHead to be checked with other files heads
jpgHead = b'\xff\xd8\xff\xe0'

#Function that will try to open a file, and return it if true, exception will raise a file Not found error
def FileCheck(fn):
    try:
        open(fn, "rb")
        return fn
    except:
        raise FileNotFoundError
        

#Function calcHashfunc will return the hash values of passed jpg files 
def calcHashfunc(fileName):
    hash_md5 = hashlib.md5()#Declare and call hash library
    with open(fileName, "rb") as f: #For every file passed
        for chunk in iter(lambda: f.read(4096), b""): #get chunks and iterate
            hash_md5.update(chunk)#Update md5 hash values
    return hash_md5.hexdigest()#Return hex me5 values


#Main function will test files, directories, sub directories, and once a file is caught, a check of first 4 bytes will examine if they are equal to header image given
if __name__ == '__main__':
    '''main function will test files, directories, sub directories, and once a file is caught, a check of first 4 bytes will examine if they are equal to header image given'''
    print("\n\n\t\t\t ======PROGRAME INFORMATION======\n")
    print("\t\t\t\t Name: Mojahed Ghadban")
    print("\t Reading Files/Directories and Hashing with Python.")
    print("Description: Module to calculate the MD5 values of JPEG files within directories and subdirectories")
    print("\t\t\t     Usage: python.exe MG-Reading-Files-hashing-bytes-of-jpg.py\n\n")
    fileObj = os.getcwd()#get current directory
    os.path #declare os path
    os.path.basename(fileObj)#declare base name of file object
    os.path.dirname(fileObj)#declare directory name of file object
    currentFile = os.path.realpath(sys.argv[0])#Saving root and file of opened python script
    fileDict={}#Declare Dictionary to catch the hex values returned by hashcalcfunc
    hashes = defaultdict(list)#hashes is a list declared that will parse Dictionaries
    dirFile = ''#declaring object to store root and file
    currentDirFile=''#declaring object to store current opened python file with its directory
    c=0#Counter to count all files found
    c2=0#Counter to count all files matching criteria of First 4 bytes and JPG head
    fileList=[]#List that will store all files found and scanned
    fileMatched=[]#List that will store all files matching criteria of First 4 bytes and JPG head
    for root, dirs, files in os.walk(fileObj):#Walk through directories, subs, and files
        for file in files:#for each file
            dFile = os.path.join(root, file)#Save roots and files for all files in dFile
            c+=1#Increment Counter that a file has been found
            fileList.append(dFile)#Add the file and directory of files that are found
            try:#Try to open the current python open file/script
                r = FileCheck(currentFile)#Call Function FileCheck and see if file can be opened
                currentDirFile=os.path.join(root,r)#Join returned opened file with root and save it in currentDirFile
                if currentDirFile!=dFile:#if the current opened python file doesn't equal other found files then..
                    dirFile=os.path.join(root,file) #Save root and other files in dirFile
                    try:#Try is the next check of opening all other files beside opened python script
                        with open(dirFile,'rb') as f:#Open each file in directory and continue checking
                            try:#Try to save the first four bytes of files
                                checkJPG = f.read(4)#Save first four bytes of a file in checkJPG
                                if checkJPG == jpgHead:#Check if the first four bytes of a file equal Globally defined jpgHead
                                    c2+=1#Increment Counter that a file matches criteria
                                    fileMatched.append(dFile)#Add the matched file to filematched list
                                    print ("\n The file: ",file, " Matches criteria:\n File first 4 byes header = ",checkJPG,"\n Globally Defined jpgHead = ",jpgHead,"\n In directory:",dirFile,"\n Are eaqual")
                                    md5Value = calcHashfunc(dirFile)#Finally after finding match of jpg and jpgHead = to first four bytes, call calcHashfucn
                                    fileDict[str(dirFile)] = md5Value#The returning hash information along with matching files are stored in Dictionary
                                    hashes[md5Value] += [dirFile]#Thus we have the key (file) and (value) MD4 value saved in Dictionary
                                    with open("JPG-Results.txt",'w+') as outFile:#Open Output file, display JPG file that has equal four bytes to jpgHead, with MD5 Values
                                        outFile.write("\n===================================================PROGRAME FILE OUTPUT===================================================\n")
                                        outFile.write("\n\t**********************************************************************************************************")
                                        outFile.write("\n\t**                                Date & Time:"+ str(datetime.now())+"                                **")
                                        outFile.write("\n\t**                                         Name: Mojahed Ghadban                                        **")
                                        outFile.write("\n\t**                             Reading Files/Directories and Hashing with Python.                          **")
                                        outFile.write("\n\t**     Module to calculate the MD5 values of JPEG files within directories and subdirectories          **")
                                        outFile.write("\n\t**********************************************************************************************************\n\n")
                                        i = 0#this counter is for counting the number of successful files with their md5 values
                                        for entry in fileDict:#Loop in each entry or item in Dictionary
                                            FileName = os.path.basename(entry)#Get the name of that file
                                            i+=1#Start with 1 and Increment, Also write out all the passed jpg files and their md5 values
                                            outFile.write("\n\n\n-----------------------------------JPG HEADER FILE NUMBER ("+str(i)+") " + FileName + " MATCH WITH MD5 HASHING ANALYSIS-----------------------------------")
                                            outFile.write("\n--\t The file:- " + FileName + " with 4 byte header:- ( "+ str(checkJPG)+" ) == jpgHead ( "+str(jpgHead)+" ) ")
                                            outFile.write("\n--\t File Name:- " + FileName + "\n--\t Directory:- " + entry + "\n--\t MD5(value):- [ "+ str(fileDict[entry])+" ] \n")
                                            outFile.write("-------------------------------------------------------------------------------------------------------------------------------------------------------\n\n\n")
                                        outFile.write("\n=================================================END OF PROGRAME FILE OUTPUT=================================================\n")
                                        outFile.close()#Declare the closing of output file that was named JPG-Results.txt
                                        print("\n More Information with MD5 Value is printed in an Output file\n Located at directory: \n ", os.getcwd()," and named: ",str(outFile.name), '\n')#Show output to user that passed information are saved in txt file
                                else:#If the header of a file doesn't equal globally defined jpgHead
                                    raise FileNotFoundError#Raise an error that a file has been found, but criteria doesn't match with more explanation
                            except FileNotFoundError:#Except if file header didn't read, acknowledge Error
                                  print("\n\n The following file: ",file,"Exists, but either:\n\t1) Could be JPG file but globally defined jpgHead and file header don't match")
                                  print("\t2) File is not jpg file\n\t3) File doesn't match criteria\n\t")
                            finally:#finally clause to to close all opened files
                                f.close()#Close the looped files once process is done.
                    except:#If no other files opened besides the opened python script, raise Error
                        raise FileNotFoundError#Raise Error that files didn't open
                else:#Else if no other file exists besides the open python file
                    raise FileNotFoundError#Raise Error that no other file besides the open script exists
            except FileNotFoundError:#Except that will show Error of no other files exists and it doesn't match criteria
                print("\n\n The Current Opened Python script named: ",file,"Exists, but doesn't match criteria\n\n")
            
            
    #Printing all files that were found and scanned        
    print ("\n\n Total Files Found and Scanned = ", c, " files.")#Print all file/dir found
    print (" The following files were found and scanned: ")
    x=0#Set counter x to show how many files are there
    for value in fileList:#Loop in file list, and with that value
        allfiles = value#declare and assign that file in object allfiles
        x+=1#Increment Counter
        print (" ",x,") ", str(allfiles))#Print each file with its directory
    #Printing files that matched criteria, showing that they were saved in text file
    print ("\n\n\n Total Files Matched Criteria = ", c2, " files out of " ,c, "total files.")#Print all files matching criteria
    if c2>0:#If files were found, and the increment is more than 0
        print (" Below are files which matched criteria: ")#Display to user matched files
        print(" More information found on : ", str(outFile.name), "\n Located in Directory:",os.getcwd(), )#Inform user where text files is saved with more information
        print (" Files are:- ")
        y=0#Set counter x to show how many files are there
        for value in fileMatched:#Loop in matched file list, and with that value
            matchedfiles = value#declare and assign that file in object matchedfiles
            y+=1#Increment counter
            print (" ",y,") ", str(matchedfiles))#Print each file with its directory
    else:#if the only file existing is the open python file, and it doesn't match criteria
        print ("  Since, ",c2, " file matches criteria, program will exit")#Inform user that file doesn't match criteria and will exit
        
    
    
    print ("\n\n\n\tExiting Program.....")#Program will exit