import tkinter 
from tkinter import *
from time import ctime,sleep
from os import chmod, listdir,walk
from tkinter import font
#from tkinter import tkFont
#
"""
by CODE-AD1CT 

Sample code: 

    for roots,dirs,files in os.walk([directory]):

        etc. 
    -used to get stuff from directories
"""

#Func body 
def listdir_Func(x,y):
    
    x=listdir(y)
   
    #get_directory(x)
    #print("contents of directory: "+ str(x))
    return x

def TkinterWindow(R,F1,F2): 
    R=Tk()
    R.resizable(False,False)
    R.wm_iconbitmap("default.ico")
    R.title("test")
    #R.geometry("500x500")
    #R.mainloop()
    F1=Frame(R)
    F1.grid(row=1,column=1)
    F2=Frame(R)
    F2.grid(row=2,column=1)
    return R,F1,F2

def retrieve_contents(root_D,Text_d):

    x=Text_d.get("1.0",END)
    filex=open("filex.txt",'w')
    filex.write(x)
    filex.close()
    root_D.destroy()
    #print(x)
def read_File(var,file1):
    filex=open(file1,'r')
    var=filex.readlines()
   # print(x)
    filex.close()
    var=var[0].split("\n")[0]
    return var
def get_directory(x):
   # l=(cmp_to_key(retrieve_contents))
    
    root_D=Tk()
    root_D.wm_iconbitmap("default.ico")
    root_D.geometry("630x350+550+190")
    root_D.title("Directory_Query")
    F1=Frame(root_D)
    Label1=Label(F1,text="Enter a directory:",bg="blue",fg="white")
    Text_d=Text(F1,width=50,height=20,fg="blue",bg="white")
    submitButton=Button(F1,text="SUBMIT",bg="black",fg="white",width="30",height=20, command=lambda : retrieve_contents(root_D,Text_d))
    submitButton.grid(column=2,row=2,sticky="SE")
    Label1.grid(column=1,row=1)
    Text_d.grid(column=1,row=2)
    F1.grid(column=1,row=1)
    root_D.mainloop()
    
   # return x
def apropriate_EndString(x,textF,PDF,ZIPi,i,other,PNG,mp3,wav):
   # print(x,textF,PDF,ZIPi)
    if x==".txt":
    #    print("Text_file")
        textF+=i+"\n"
    elif x==".pdf":
        print("PDF_FILE")
        PDF+=i+"\n"
    elif x==".zip":
     #   print("Zip_file")
      #  print(i)
        ZIPi+=i+"\n"
    elif x==".png":
        PNG+=i+"\n"
    elif x==".mp3":
        mp3+=i+"\n"
    elif x==".wav":
        wav+=i+"\n"

    else:
        other+=i+"\n"
   # print(ZIPi)
    return textF,PDF,ZIPi,other,PNG,mp3,wav
def Text_Areas(F1,x):
    x=Text(F1,bg="black",fg="white",width=30,height=20,cursor="tcross")
    
    return x
def get_new_directory_Func(root_D):
    root_D.destroy()
    var=""
    get_directory(var)
    directory=read_File(var, file1)
    directory_contents=listdir_Func(var,directory)
    Displaycontents=Display_contents(F1,F2,directory_contents,directory)
def Display_contents(F1,F2,x,d):
    #Font
    helv36 = ("helvetica",8,'bold')
    TitleFont=("helvetica",8,'bold')
    #
    y=TkinterWindow(R, F1, F2)
    F1=y[1]
    F2=y[2]
    label_text1="The directory is --> "+d
    Label1=Label(F1,text=label_text1,fg="blue")
    Label1.grid(column=1,row=1,sticky="NE")
    #Label2=Label(F2,text=" ",fg="blue")
    #Label2.grid(column=1,row=1)
    TEMP=""
    #labels
    Text_label=Label(F2,text=".txt files",bg="blue",fg="white",width=34,font=helv36,cursor="tcross")
    pdf_label=Label(F2,text=".pdf files",bg="blue",fg="white",width=34,font=helv36,cursor="tcross")
    zip_label=Label(F2,text=".zip files",bg="blue",fg="white",width=34,font=helv36,cursor="tcross")
    #
    other_label=Label(F2,text="other files",bg="blue",fg="white",width=34,font=helv36,cursor="tcross")
    #
    png_label=Label(F2,text="png files",bg="blue",fg="white",width=34,font=helv36,cursor="tcross")
    mp3_label=Label(F2,text=".mp3 files",bg="blue",fg="white",width=34,font=helv36,cursor="tcross")
    wav_label=Label(F2,text="wav",bg="blue",fg="white",width=34,font=helv36,cursor="tcross")
    #
    vacant2_label=Label(F2,text="VACANT",bg="blue",fg="white",width=34,font=helv36,cursor="tcross")
    vacant3_label=Label(F2,text="VACANT",bg="blue",fg="white",width=34,font=helv36,cursor="tcross")
    vacant4_label=Label(F2,text="VACANT",bg="blue",fg="white",width=34,font=helv36,cursor="tcross")
    #
    other_label.grid(column=5,row=2)
    #
    Text_label.grid(column=1,row=2)
    pdf_label.grid(column=2,row=2)
    zip_label.grid(column=3,row=2)
    png_label.grid(column=4,row=2)
    mp3_label.grid(column=1,row=4)
    wav_label.grid(column=2,row=4)
    #
    vacant2_label.grid(column=3,row=4)
    vacant3_label.grid(column=4,row=4)
    vacant4_label.grid(column=5,row=4)
    #text areas
    Text_label_TXT=Text_Areas(F2,TEMP)
    PDF_LABEL_TXT=Text_Areas(F2, TEMP)
    Zip_LABEL_TXT=Text_Areas(F2, TEMP)
    #
    other_LABEL_TXT=Text_Areas(F2, TEMP)
    #
    PNG_LABEL_TXT=Text_Areas(F2, TEMP)
    MP3_LABEL_TXT=Text_Areas(F2, TEMP)
    wav_TXT=Text_Areas(F2, TEMP)
    #
    Vacant2_TXT=Text_Areas(F2, TEMP)
    Vacant3_TXT=Text_Areas(F2, TEMP)
    Vacant4_TXT=Text_Areas(F2, TEMP)
    #
    get_new_directory=Button(F2,width=20,text="Get new directory",fg="white",bg="blue",command=lambda: get_new_directory_Func(y[0]))
    #
    other_LABEL_TXT.grid(column=5,row=3)
    #
   # get_new_directory.grid(column=4,row=6)
    #
    PDF_LABEL_TXT.grid(column=2,row=3)
    Zip_LABEL_TXT.grid(column=3,row=3)
    PNG_LABEL_TXT.grid(column=4, row=3)
    Text_label_TXT.grid(column=1, row=3)
    MP3_LABEL_TXT.grid(column=1,row=5)
    wav_TXT.grid(column=2,row=5)
    #
    Vacant2_TXT.grid(column=3,row=5)
    Vacant3_TXT.grid(column=4,row=5)
    Vacant4_TXT.grid(column=5,row=5)
    #
    PNG=""
    c=""
    textF=""
    PDF=""
    wav=""
    ZIPi=""
    other=""
    mp3=""
    for i in x:
        End_string=i[-4:]
        b=apropriate_EndString(End_string, textF, PDF, ZIPi,i,other,PNG,mp3,wav)
        #
        textF=b[0]
        PDF=b[1]
        ZIPi=b[2]
        other=b[3]
        PNG=b[4]
        mp3=b[5]
        wav=b[6]
        
    if PDF=="":
        PDF="""No pdf files were detected!
        sorry"""
    
    if ZIPi=="":
        ZIPi="""No zip files were detected!
sorry"""
    if textF=="":
        textF="""No text files were detected!
sorry"""
    if PNG=="":
        textF="""No text files were detected!
sorry"""
    if mp3=="":
        mp3="""No text files were detected!
sorry"""
    #print("\n"+textF)
        #print(b)
                
    Zip_LABEL_TXT.insert(1.0,ZIPi)
    Text_label_TXT.insert(1.0,textF)
    PDF_LABEL_TXT.insert(1.0,PDF)
    other_LABEL_TXT.insert(1.0,other)
    PNG_LABEL_TXT.insert(1.0, PNG)
    MP3_LABEL_TXT.insert(1.0,mp3)
    wav_TXT.insert(1.0,wav)
    Zip_LABEL_TXT.configure(state="disabled")
    PDF_LABEL_TXT.configure(state="disabled")
    other_LABEL_TXT.configure(state="disabled")
    Text_label_TXT.configure(state="disabled")
    PNG_LABEL_TXT.configure(state="disabled")
    #MP3_LABEL_TXT.configure(state="disabled")
    r=y[0]
    #Scrollbar_x=Scrollbar(r,)
    
    
    r.mainloop()
#variable body
var=""
file1='filex.txt'
temp=""
R=""
F1=""
F2=""
count = 0
Loop = True;
DFound = False; 
while ( DFound == False and Loop == True):
    print ('Cycle Number : {',count,end = ' }\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
    try:
        if (count == 0):
            get_directory(temp)
        directory=read_File(var, file1)
        directory_contents=listdir_Func(temp,directory)
        Displaycontents=Display_contents(F1,F2,directory_contents,directory)
        UsrReq = input("Enter Y to Exit:")
        if (UsrReq.upper() ==  "Y"):
            Loop = False
        else :
            print ("You chose to continue...",end = "| Resetting variables ...\n" )
            Loop = True
            DFound = False
            directory_read = ''
            directory_contents = ''
            UsrReq = ''
            Displaycontents = '' 
        count+=1
    except Exception as Exc:
        print(Exc)
        UsrReq = input("Enter Y to Exit:")
        if (UsrReq.upper() ==  "Y"):
            Loop = False
        else :
            print ("You chose to continue...",end = "\tResetting variables ...\n" )
            Loop = True
            DFound = False
            directory_read = ''
            directory_contents = ''
            UsrReq = ''
            Displaycontents = '' 
        pass

#main body 

