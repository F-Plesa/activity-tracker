import time
import pickle
import datetime

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

#input("Press Enter to start")
#start_time = time.time()

#input("Press Enter to stop")
#end_time = time.time()

#time_lapsed = end_time - start_time
#time_convert(time_lapsed)

def progress_bar(perc):
    print("Completion: [", end="")
    for i in range(perc // 10):
        print("##", end="")
    for i in range(10 - (perc // 10)):
        print("__", end="")
    print("]", end="")
    print()

start_date = datetime.date(2021,2,22)
exam_date = datetime.date(2021,7,5)
ready_date = datetime.date(2021,4,15)
today = datetime.date.today()

until_ready = (ready_date - today).days
until_exam = (exam_date - today).days
until_ready_total = (ready_date - start_date).days
until_exam_total = (exam_date - start_date).days
until_ready_perc = (until_ready_total - until_ready)*100 // until_ready_total
until_exam_perc = (until_exam_total - until_exam)*100 // until_exam_total

filename = "save"

categories = ["ucenje", "sklekovi"]
subjects = ["APR", "NASP", "Strojno"]
settings = ["work", "studies"]

APR_parts = 6
NASP_parts = 6
Strojno_parts = 10

infile = open(filename, 'rb')
subject_status_loaded = pickle.load(infile)
#print(subject_status_loaded)

sklekovi = 0

def tracker():

    print("\n\t\t ***** ACTIVITY TRACKER *****\n\n\n")
    #setting = input("Choose setting (work or studies):  ")
    #print(setting)

    APR_done = subject_status_loaded["APR"]
    NASP_done = subject_status_loaded["NASP"]
    Strojno_done = subject_status_loaded["Strojno"]

    APR_perc = APR_done*100 // APR_parts
    NASP_perc = NASP_done*100 // NASP_parts
    Strojno_perc = Strojno_done*100 // Strojno_parts

    print("Subject completion status:")
    print("APR:       " + str(APR_done) + "/" + str(APR_parts) + "   " + str(APR_perc) + "%" + "   ", end="")
    progress_bar(APR_perc)

    print("NASP:      " + str(NASP_done) + "/" + str(NASP_parts) + "   " + str(NASP_perc) + "%" + "   ", end="")
    progress_bar(NASP_perc)

    print("Strojno:   " + str(Strojno_done) + "/" + str(Strojno_parts) + "  " + str(Strojno_perc) + "%" + "   ", end="")
    progress_bar(Strojno_perc)

    print("\nDays left until you must be 75% ready: " + str(until_ready) + "   ", end="")
    progress_bar(until_ready_perc)
    print("Days left until exams:                " + str(until_exam) + "   ", end="")
    progress_bar(until_exam_perc)


    print("\n\n\nSklekovi: " + str(sklekovi))

def update(subject, com, number):
    subjects_status = subject_status_loaded
    if(com == "add"):
        subjects_status[subject] = subjects_status[subject] + number
    if(com == "sub"):
        subjects_status[subject] = subjects_status[subject] - number
    outfile = open(filename, 'wb')
    pickle.dump(subjects_status, outfile)
    outfile.close


#subjects_status = {'APR' : 0, 'NASP' : 0, 'Strojno' : 0}
#filename = "save"
#outfile = open(filename, 'wb')
#pickle.dump(subjects_status, outfile)
#outfile.close 

print("\n\nCommands: refresh = 'r', Update = 'update APR add 1' or 'update APR sub 1', exit = 'exit'")
command = ""

tracker()

print("\n\n\n\n\n")

while(command != "exit"):
    command = input(">>")
    
    if(command == "r"):
        for i in range(5):
            print("\n")
        tracker()
        for i in range(4):
            print("\n")

    if(command == "update"):
        subject = input("Select subject to update (APR, NASP, Strojno): ")
        com = input("Select if you want to add or sub: ")
        number = int(input("Select how much you would like to add or sub: "))
        update(subject, com, number)
        print("Subject updated!")

    if(command == "sklek"):
        sklekovi = sklekovi + 10
        for i in range(5):
            print("\n")
        tracker()
        for i in range(4):
            print("\n")

    if(command == "help"):
        print("Available commands: [r, update, sklek, exit]")



