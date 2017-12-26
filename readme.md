Reading Files/Directories and Hashing with Python



Description: Module to calculate the MD5 values of JPEG files within directories and subdirectories



Usage: python.exe MG-Reading-Files-hashing-bytes-of-jpg.py




Notes:
The following files are the main files:



1)   MG-Reading-Files-hashing-bytes-of-jpg.py --- The python (*.py) file you need to run ---

2)   JPG-Results.txt --- The Output text generated after checking files, it contains results ---

3)   Sample-Output.txt  --- Text File with Sample Output ---

4)  .gitignore

5)   readme.md

6)   readme.txt

7)   requirements.txt





- The rest of the files inside directories are for testing purposes, they will be checked in addition to the above files.



- Criteria of checking files:


	If file is jpg or not



		If file is jpg then read the first 4 bytes


	
			If the first 4 bytes match the globally defined header jpgHead = b'\xff\xd8\xff\xe0'
	
	
			Return MD5 Hashing value of the jpg file and store output it in JPG-Results.txt





- Try and Except statements were used to check existence of a file or directory, and to try to open them. 

- The program is supposed to handle all errors associated with checking and opening these files and returning proper messages accordingly.



