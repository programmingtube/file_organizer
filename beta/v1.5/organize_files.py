import os
import time
import shutil
import argparse
import tempfile
from pathlib import Path
import sys

cur_dir = os.getcwd()
tmpfolder = tempfile.gettempdir()

class ProcessNextFile(Exception):
    pass

ap = argparse.ArgumentParser()

ap.add_argument("-wf", "--workingfolder", default=cur_dir)
ap.add_argument("-of", "--outputfolder", default=tmpfolder+"\\"+"organized_files")
ap.add_argument("-if", "--ignorefolder", default="", type=str)
ap.add_argument("-lf", "--ignorefiles", default="",type=str)
args = vars(ap.parse_args())

input_dir = str(args["workingfolder"])
output_dir = str(args["outputfolder"])
#creating folders and subfolders
print("\nCurrent Working Directory: {}".format(input_dir))
time.sleep(2)
print("\nCreating Temporary Directories")

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

folders = ["DATABASES", "AUDIOS", "ARCHIVES", "DISC AND MEDIA", "PROGRAMS", "FONTS", "IMAGES", "WEB FILES", "PRESENTATIONS", "PROGRAMMING", "SPREADSHEET", "SYSTEM", "VIDEOS", "WORD PROCESSING AND PDF", "OTHER"]
for folder in folders:
    if not os.path.exists(output_dir+"\\"+folder):
        os.mkdir(output_dir+"\\"+folder)

time.sleep(2)
print("\nTemporary Folders Created Successfully!")
#declaring extension
audio = [".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl", ".m4a"]
archive = [".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z", ".zip"]
disc_media = [".bin", ".dmg", ".toast", ".iso", ".vcd"]
database = [".csv", ".dat", ".db", ".dbf", ".log", ".mdb", ".sav", ".sql", ".tar", ".xml"]
program = [".apk", ".bat", ".bin", ".cgi", ".pl", ".com", ".exe", ".hta", ".htma",".gadget", ".jar", ".py", ".wsf"]
font = [".fnt", ".fon", ".otf", ".ttf"]
image = [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tif", ".tiff", ".webp"]
web = [".asp", ".aspx", ".cer", ".cfm", ".css", ".html", ".htm", ".js", ".jsp", ".json", ".part", ".crdownload", ".php", ".rss", ".xhtml"]
presentation = [".key", ".odp", ".pps", ".ppt", ".pptx"]
programming = [".c", ".class", ".cpp", ".cs", ".h", ".java", ".sh", ".swift", ".vb"]
spreadsheet = [".ods", ".xlr", ".xls", ".xlsx"]
system = [".bak", ".cab", ".cfg", ".cpl", ".cur", ".dll", ".dmp", ".drv", ".icns", ".ico", ".ini", ".lnk", ".msi", ".sys", ".tmp"]
video = [".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob",".wmv"]
word = [".docx", ".doc", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wks", ".wps", ".md", ".wpd"]
known_extensions = audio + archive + disc_media + database + program + font + image + web + presentation + programming + spreadsheet + system + video + word
excluded_folders = [args["ignorefolder"].split(",")]
excluded_files = [os.path.basename(__file__)]
if args["ignorefiles"] != "":
    for f in args["ignorefiles"].split(","):
        excluded_files.append(f)
#storing file names
audios = []
databases = []
archives = []
disc_medias = []
programs = []
fonts = []
images = []
webs = []
presentations = []
programmings = []
spreadsheets = []
systems = []
videos = []
words = []
others = []
total_files = []
file_dir = ""
files_not_processed = []
for foldername, subfolders, filenames in os.walk(input_dir):
    try:
        for excluded_folder in excluded_folders:
            if foldername == excluded_folder:
                raise ProcessNextFile()
            else:
                pass
    print('\nThe current folder is ' + foldername)
    time.sleep(2)
    for subfolder in subfolders:
        print('\nSUBFOLDER OF ' + foldername + ': ' + subfolder)
        time.sleep(2)
    print("\nOrganzing Files!")
    time.sleep(1)
    print("\nThis can take some time to complete...")
    time.sleep(1)
    for filename in filenames:
        file_extension = Path(filename).suffix
        try:
            for excluded_file in excluded_files:
                if filename == excluded_file:
                    raise ProcessNextFile()
                else:
                    if file_extension in known_extensions:
                        if file_extension in audio:
                            file_dir = "AUDIOS"
                            audios.append(filename)
                        elif file_extension in archive:
                            file_dir = "ARCHIVES"
                            archives.append(filename)
                        elif file_extension in disc_media:
                            file_dir = "DISC AND MEDIA"
                            disc_medias.append(filename)
                        elif file_extension in database:
                            file_dir = "DATABASES"
                            databases.append(filename)
                        elif file_extension in program:
                            file_dir = "PROGRAMS"
                            programs.append(filename)
                        elif file_extension in font:
                            file_dir = "FONTS"
                            fonts.append(filename)
                        elif file_extension in image:
                            file_dir = "IMAGES"
                            images.append(filename)
                        elif file_extension in web:
                            file_dir = "WEB FILES"
                            webs.append(filename)
                        elif file_extension in presentation:
                            file_dir = "PRESENTATIONS"
                            presentations.append(filename)
                        elif file_extension in programming:
                            file_dir = "PROGRAMMING"
                            programmings.append(filename)
                        elif file_extension in spreadsheet:
                            file_dir = "SPREADSHEET"
                            spreadsheets.append(filename)
                        elif file_extension in system:
                            file_dir = "SYSTEM"
                            systems.append(filename)
                        elif file_extension in video:
                            file_dir = "VIDEOS"
                            videos.append(filename)
                        elif file_extension in word:
                            file_dir = "WORD PROCESSING AND PDF"
                            words.append(filename)
                    else:
                        file_dir = "OTHER"
                        others.append(filename)
                    try:
                        shutil.move(foldername+"\\"+filename, output_dir+"\\"+file_dir)
                    except:

                        print("\nProcessing of file {} not done due to internal errors! Skiping to Next File.".format(foldername+"\\"+filename))

                        files_not_processed.append(foldername+"\\"+filename)
                        raise ProcessNextFile()
        except ProcessNextFile:
            continue
        time.sleep(2)
total_files = programs + audios + archives + disc_medias + databases + fonts + images + webs + presentations + programmings + spreadsheets + systems + videos + words + others

#delete empty Folders
x = 0
for root, dirs, files in os.walk(output_dir):
    for name in dirs:
        try:
            if len(os.listdir(os.path.join(root, name))) == 0:
                time.sleep(2)
                if x == 0:
                    print("\nDeleting Empty Folders...")
                else:
                    pass
                try:
                    os.rmdir(os.path.join(root, name))
                except:
                    print("FAILED :", os.path.join(root, name))
                    pass
            x +=1
        except:
            pass

if output_dir == tmpfolder+"\\"+"organized_files":
    shutil.move(output_dir, input_dir)
    copied_output = input_dir + "\\" + "organized_files"
else:
    copied_output = output_dir
print("\nFile Processing Completed!")
print("\n---------- Generating Summary ----------")
time.sleep(2)
if len(total_files) == 0:
    print("\nThe selected Directory doesn't contain any Files!")
    time.sleep(2)
    print("\nExiting Software....")
    time.sleep(3)
    sys.exit()
else:
    time.sleep(2)
    print("\nTotal Audios Processed = {}".format(str(len(audios))))
    time.sleep(2)
    print("\nTotal Archives Processed = {}".format(str(len(archives))))
    time.sleep(2)
    print("\nTotal Programs Processed = {}".format(str(len(programs))))
    time.sleep(2)
    print("\nTotal DISC and MEDIA Files Processed = {}".format(str(len(disc_medias))))
    time.sleep(2)
    print("\nTotal Databases Processed = {}".format(str(len(databases))))
    time.sleep(2)
    print("\nTotal Fonts Processed = {}".format(str(len(fonts))))
    time.sleep(2)
    print("\nTotal Images Processed = {}".format(str(len(images))))
    time.sleep(2)
    print("\nTotal Web Files Processed = {}".format(str(len(webs))))
    time.sleep(2)
    print("\nTotal Presentations Processed = {}".format(str(len(presentations))))
    time.sleep(2)
    print("\nTotal Programming Files Processed = {}".format(str(len(programmings))))
    time.sleep(2)
    print("\nTotal Spreadsheets Processed = {}".format(str(len(spreadsheets))))
    time.sleep(2)
    print("\nTotal System Files Processed = {}".format(str(len(systems))))
    time.sleep(2)
    print("\nTotal Video Files Processed = {}".format(str(len(videos))))
    time.sleep(2)
    print("\nTotal Word and PDF Files Processed = {}".format(str(len(words))))
    time.sleep(2)
    print("\nTotal Other Files Processed = {}".format(str(len(others))))
    time.sleep(2)
    print("\nTotal Files Processed = {}".format(str(len(total_files))))
    time.sleep(2)
    legal_choice = False
    legal_choice_for_errors = False
    show_files = False
    while legal_choice == False:
        see_files = str(input("\nDo you want to see the files? (y/n): ")).upper()
        if see_files == "Y":
            legal_choice = True
            show_files = True
            break
        elif see_files == "N":
            legal_choice = True
            break
        else:
            legal_choice = False
            print("\nWrong Selection! Please Try Again!")
            continue
    if legal_choice == True and show_files == True:
        n = 1
        for file in total_files:
            print("\n"+str(n)+". "+file)
            n +=1

    time.sleep(2)

    if not len(files_not_processed) == 0:
        while legal_choice_for_errors == False:
            see_errors = str(input("\nSome Files were not Processed! Do you want to see the files? (y/n): ")).upper()
            if see_errors == "Y":
                legal_choice_for_errors = True
                break
            elif see_errors == "N":
                legal_choice_for_errors = False
                break
            else:
                legal_choice_for_errors = False
                print("\nWrong Selection! Please Try Again!")
                continue
        if legal_choice_for_errors == True:
            l = 1
            for errors in files_not_processed:
                print(str(l)+". "+errors)
                l+=1

    print("\nOutput Folder = {}".format(copied_output))
    time.sleep(2)
    print("\nExiting System in 3 seconds!")
    time.sleep(3)
    sys.exit()
