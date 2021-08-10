import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#from PIL import ImageTk,Image
import tkinter.messagebox
import csv
import os
import sqlite3


breed_list = ["","GERMAN SHEPHERD", "POODLE","LABRADOR RETRIEVERS","GOLDEN RETRIEVERS","FRENCH BULLDOG","SIBERIAN HUSKY","BEAGLES","ROTTWIELERS","GERMAN SHORTHAIRED POINTERS","PEMBROKE WELSH CORGIS"
            
            ,"RAGDOLL","EXOTIC","MAINE COON","PERSIAN","BRITISH SHORTHAIR","DEVON REX","ABYSSINIAN","AMERICAN SHORTHAIR","SCOTTISH FOLD","SPHYNX"
            
            ,"HOLLAND LOP","MINI LOP","DUTCH","LION HEAD","FRENCH LOP","CALIFORNIAN","DWARF PAPILION","NETHERLAND DWARF","MINI REX","FLEMISH GIANT"
            
            ,"PARAKET","COCKATIEL","FINCH","LOVEBIRD","MONK PARAKET","DOVE","PARROTLET","AFRICAN GRAY PARROT"

            ,"SYRIAN HAMSTER","CHINISE HAMSTER","DWARF CAMPBELL RUSSIAN HAMSTER","DWARF WINTER WHITE RUSSIAN HAMSTER","DWARF ROBOROVSKI HAMSTER"

            ,"AMRECICAN GUINEA PIG","CRESTED GUINEA PIG","CORONET GUINEA PIG","PERUVIAN GUINEA PIG","HIMALAYAN GUINEA PIG","SILKIE GUINEA PIG","TEDDY GUINEA PIG","TEXEL GUINEA PIG","REX GUINEA PIG","SHEBA GUINEA PIG","ALPACA GUINEA PIG"
         
            ,"BETTA","GOLD FISH","ANGEL FISH","CATFISH","GUPPIES","MOLLIES","NEON TETRAS","PLATIES","SWORD TAILS","ZEBRA DANIOS" ]

type_list = ["","DOG","CAT","RABBIT","BIRDS","HAMSTER","GUINEA PIG","FISH"]

date_list = ["", "07/01/2021","07/02/2021","07/03/2021","07/04/2021","07/05/2021","07/06/2021","07/07/2021","07/08/2021","07/09/2021","07/10/2021",
             "07/11/2021","07/12/2021","07/13/2021","07/14/2021","07/15/2021","07/16/2021","07/17/2021","07/18/2021","07/19/2021","07/20/2021",
             "07/21/2021","07/22/2021","07/23/2021","07/24/2021","07/25/2021","07/26/2021","07/27/2021","07/28/2021","07/29/2021","07/30/2021",
             "07/31/2021",

             "08/01/2021","08/02/2021","08/03/2021","08/04/2021","08/05/2021","08/06/2021","08/07/2021","08/08/2021","08/09/2021","08/10/2021",
             "08/11/2021","08/12/2021","08/13/2021","08/14/2021","08/15/2021","08/16/2021","08/17/2021","08/18/2021","08/19/2021","08/20/2021",
             "08/21/2021","08/22/2021","08/23/2021","08/24/2021","08/25/2021","08/26/2021","08/27/2021","08/28/2021","08/29/2021","08/30/2021",
             "08/31/2021",

             "09/01/2021","09/02/2021","09/03/2021","09/04/2021","09/05/2021","09/06/2021","09/07/2021","09/08/2021","09/09/2021","09/10/2021",
             "09/11/2021","09/12/2021","09/13/2021","09/14/2021","09/15/2021","09/16/2021","09/17/2021","09/18/2021","09/19/2021","09/20/2021",
             "09/21/2021","09/22/2021","09/23/2021","09/24/2021","09/25/2021","09/26/2021","09/27/2021","09/28/2021","09/29/2021","09/30/2021",

             "10/01/2021","10/02/2021","10/03/2021","10/04/2021","10/05/2021","10/06/2021","10/07/2021","10/08/2021","10/09/2021","10/10/2021",
             "10/11/2021","10/12/2021","10/13/2021","10/14/2021","10/15/2021","10/16/2021","10/17/2021","10/18/2021","10/19/2021","10/20/2021",
             "10/21/2021","10/22/2021","10/23/2021","10/24/2021","10/25/2021","10/26/2021","10/27/2021","10/28/2021","10/29/2021","10/30/2021",
             "10/31/2021",

             "11/01/2021","11/02/2021","11/03/2021","11/04/2021","11/05/2021","11/06/2021","11/07/2021","11/08/2021","11/09/2021","11/10/2021",
             "11/11/2021","11/12/2021","11/13/2021","11/14/2021","11/15/2021","11/16/2021","11/17/2021","11/18/2021","11/19/2021","11/20/2021",
             "11/21/2021","11/22/2021","11/23/2021","11/24/2021","11/25/2021","11/26/2021","11/27/2021","11/28/2021","11/29/2021","11/30/2021",

             "12/01/2021","12/02/2021","12/03/2021","12/04/2021","12/05/2021","12/06/2021","12/07/2021","12/08/2021","12/09/2021","12/10/2021",
             "12/11/2021","12/12/2021","12/13/2021","12/14/2021","12/15/2021","12/16/2021","12/17/2021","12/18/2021","12/19/2021","12/20/2021",
             "12/21/2021","12/22/2021","12/23/2021","12/24/2021","12/25/2021","12/26/2021","12/27/2021","12/28/2021","12/29/2021","12/30/2021",
             "12/31/2021"]

def PSMS_UserDatabase():
    conn = sqlite3.connect("PSMS.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user (username VARCHAR PRIMARY KEY, password VARCHAR NOT NULL, role VARCHAR NOT NULL,company_name VARCHAR NOT NULL,login VARCHAR NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS online_users (username VARCHAR PRIMARY KEY, password VARCHAR NOT NULL, role VARCHAR NOT NULL,company_name VARCHAR NOT NULL)")
    conn.commit() 
    conn.close()
PSMS_UserDatabase()
def connectCustomer():
    conn=sqlite3.connect("PSMS.db")
    cur=conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("""CREATE TABLE IF NOT EXISTS Customer(
        Customer_id VARCHAR(7) PRIMARY KEY,
        Customer_name VARCHAR(30),
        Mobile_no VARCHAR(11)
        )""")
    conn.commit()
connectCustomer()

def connectPET():
    conn=sqlite3.connect("PSMS.db")
    cur=conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("""CREATE TABLE IF NOT EXISTS PET(
        Pet_id VARCHAR(5) PRIMARY KEY,
        Breed VARCHAR,
        type VARCHAR,
        Customer_id VARCHAR(7),
        FOREIGN KEY(Customer_id) 
            REFERENCES Customer(Customer_id)
                ON DELETE CASCADE
            )""")
    conn.commit()
connectPET()

def connectAppointment():
    conn=sqlite3.connect("PSMS.db")
    cur=conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    cur.execute("""CREATE TABLE IF NOT EXISTS Appointment(
        Appointment_ID VARCHAR(5) PRIMARY KEY,
        Appointment_details VARCHAR,
        appointment_date DATE,
        Status VARCHAR(10),
        Customer_id VARCHAR (7),
        company_name VARCHAR,
        username VARCHAR,
        FOREIGN KEY(Customer_id) 
            REFERENCES Customer(Customer_id)
                ON DELETE CASCADE
            )""")
    conn.commit()
connectAppointment()
def connectHistory():
    conn=sqlite3.connect('PSMS.db')
    cur=conn.cursor()
    cur.execute("""CREATE TABLE  IF NOT EXISTS History(
        Appointment_id    VARCHAR(5) PRIMARY KEY,
        Appointment_details   VARCHAR,
        Status    VARCHAR(10),
        appointment_date  DATE,
        Customer_id   VARCHAR(7),
        Pet_id    VARCHAR(5),
        company_name  VARCHAR,
        FOREIGN KEY(Pet_id) 
            REFERENCES PET(Pet_id)
                ON DELETE CASCADE
                )""")
connectHistory()


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #create window
        window = tk.Frame(self)
        window.pack()
        
        window.grid_rowconfigure(0, minsize=800)
        window.grid_columnconfigure(0, minsize=1300)
        
        self.frames = {}
        for F in (FirstPage,LoginPage,SignupPage,HomePage,AddPage,history):
            frame = F(window,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0, sticky="nsew")
    
        self.show_frame(FirstPage)
        
    def show_frame(self,page):
        frame = self.frames[page]
        frame.configure(background="white")
        frame.tkraise()

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #self.toplevel = tk.Toplevel(parent)
        self.controller = controller
        self.controller.title("Pet Shop Management System")
        
        
        self.first = PhotoImage(file="a.png", master=self) 
        
        appfirst = tk.Label(self, image = self.first, bd=0)
        appfirst.place(x=0,y=0, relwidth=1,relheight=1)
        
        welcome = tk.Label(self, text= "Welcome to Pet Shop Management System", font=("Impact", 25), bg="white", bd=0, fg="grey17")
        welcome.place(x=380,y=100)
        
        welcome1 = tk.Label(self, text= "Managing your shop has never been so easy!", font=("Courier", 15), bg="white", bd=0, fg="grey17")
        welcome1.place(x=420,y=165)
        
        Button = tk.Button(self, text="Log in", bg="gray50", fg="white", width=15, font=("Palatino Linotype", 20), command= lambda: controller.show_frame(LoginPage))
        Button.place(x=390,y=270)
        
        Button = tk.Button(self, text="Sign up", bg="white", fg="gray50", width=15, font=("Palatino Linotype", 20), command= lambda: controller.show_frame(SignupPage))
        Button.place(x=690,y=270)
        
        
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Pet Shop Management System")
        
        
        ##Variables
        
        Username = StringVar()
        Password= StringVar()
        
        ##Pics
        self.logpic = PhotoImage(file="p19a.png", master=self) 
        
        applogpic = tk.Label(self, image = self.logpic, bd=0)
        applogpic.place(x=880,y=80)
        
        self.logpic1 = PhotoImage(file="p20a.png", master=self) 
        
        applogpic1 = tk.Label(self, image = self.logpic1, bd=0)
        applogpic1.place(x=50,y=400)

        #self.logpic2 = PhotoImage(file="p21ab.png", master=self)
        #applogpic2 = tk.Button(self,image=self.logpic,bd=0 ,command=back)
        #applogpic2.place(x=10,y=20) 

        
        ##Functions
        


        #def selectrow():

        conn=sqlite3.connect("PSMS.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM user WHERE username = ?",(Username.get(),))
        row = cur.fetchall()
        for i in row:
            cname =i[3]
        def loginuser():

            #cur_user()
            #print(current_user)
            current_user = user_name1.get()
            conn=sqlite3.connect("PSMS.db")
            cur=conn.cursor()
            cur.execute("SELECT * FROM user WHERE username = ?",(Username.get(),))
            row = cur.fetchall()
            for i in row:
                cname =i[3]
            conn=sqlite3.connect("PSMS.db")
            cur=conn.cursor()
            #current_user = user_name1.get()
            cur.execute("SELECT *FROM Appointment")
            records =cur.fetchall()
            for record in records:
                if record[0].startswith(cname):
                    user1 = record[0]
                    if user1 == record[0]:
                        cur.execute("UPDATE Appointment SET company_name= ? ,username = ?  WHERE Appointment_id = ?",(cname,current_user,user1,))
                        cur.execute("UPDATE History SET company_name= ? WHERE Appointment_id = ?",(cname,user1,))
                        #cur.execute("UPDATE Appointment SET username = ?  WHERE Appointment_id = ?",(current_user,user1,))

                else: 
                    user1 = record[0]
                    if user1==record[0]:
                        cur.execute("UPDATE Appointment SET company_name = '-' ,username = '-' WHERE Appointment_id = ?",(user1,))
                        #cur.execute("UPDATE Appointment SET username = '-'  WHERE Appointment_id = ?",(user1,))
                conn.commit()

            #conn.commit()
        def onlineuser():
            conn=sqlite3.connect("PSMS.db")
            cur=conn.cursor()           
            cur.execute("UPDATE user SET login = 'Online' WHERE username = ?",(Username.get(),))
            cur.execute("UPDATE user SET login = '***' WHERE username != ?",(Username.get(),))
            conn.commit()
        
     
#                    
        def Login():
            #cur_user()
            #PSMS_UserDatabase()
            conn = sqlite3.connect("PSMS.db")
            cur = conn.cursor()
            if Username.get() == "" or Password.get() == "":
                tkinter.messagebox.showerror("Pet Shop Management System", "Please require the completed field")
            else:
                cur.execute("SELECT * FROM user WHERE username = ? and password = ?", (Username.get(), Password.get()))
                if cur.fetchone() is not None:
                    tkinter.messagebox.showinfo("Pet Shop Management System", "Login Successfully")
                    loginuser()
                    onlineuser()
                    controller.show_frame(HomePage)
                    Username.set('')
                    Password.set('')
                else:
                    tkinter.messagebox.showerror("Pet Shop Management System", "Invalid password or username")  
            conn.commit()
            conn.close()
        #def Loginevent(event):
            #login()            

            #########################################


##################################################################################


        
        ##Labels&Buttons
        welcome = tk.Label(self, text= "Log in to your account", font=("Arial Bold", 30), bg="white", bd=0, fg="grey23")
        welcome.place(x=205,y=140)
        
        welcome1 = tk.Label(self, text= "Do not have an account?", font=("Courier", 15), bg="white", bd=0, fg="grey23")
        welcome1.place(x=215,y=200)
        
        login_form = tk.LabelFrame(self, font= ("Helvetica",20), labelanchor="nw", text="Log in", bg="white")
        login_form.pack(fill="both", expand="yes",padx=490,pady=250) 
    
        
        user_name = tk.Label(login_form, font=("Poppins", 12), text="Username:", padx=5, pady=5, bg="white")
        user_name.place(x=20,y=10)
        user_name1 = tk.Entry(login_form, font=("Poppins", 13), textvariable=Username, width=30, bg="white")
        user_name1.place(x=20,y=50)
        
        password = tk.Label(login_form, font=("Poppins", 12), text="Password:", padx=5, pady=5, bg="white")
        password.place(x=20,y=100)
        password = tk.Entry(login_form, font=("Poppins", 13), textvariable=Password, width=30, bg="white",show="*")
        password.place(x=20,y=140)
        
        
        Button = tk.Button(self, text="Create it!", font=("Courier", 15, "bold"), bd=0, fg="gray30", bg="white", command= lambda: controller.show_frame(SignupPage))
        Button.place(x=500,y=195)
        
        Button = tk.Button(login_form, bg="gray50", fg="white", text="Log in", width=15, font=("Arial Bold", 16), command=Login)
        #Button.bind("<Return>",Loginevent)
        Button.place(x=60,y=190)

        


    #    backbut= tk.Button(self, bg="gray50", fg="white", text="Back", width=15, font=("Arial Bold", 16),command=back)
    #    backbut.place(x=10, y=10)
        
class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Pet Shop Management System")
        
        ##Variables
        Username = StringVar()
        Password= StringVar()
        role= StringVar()
        Company_Name = StringVar()
        
        ##Pics
        self.uppic = PhotoImage(file="p14a.png", master=self) 
        
        appuppic = tk.Label(self, image = self.uppic, bd=0)
        appuppic.place(x=50,y=400)
        
        self.uppic1 = PhotoImage(file="p8a.png", master=self) 
        
        appuppic1 = tk.Label(self, image = self.uppic1, bd=0)
        appuppic1.place(x=800,y=100)

        ##Functions
        
        def PSMS_RegDatabase():
            conn = sqlite3.connect("PSMS.db")
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS user (username VARCHAR PRIMARY KEY, password VARCHAR NOT NULL, role VARCHAR NOT NULL,company_name VARCHAR NOT NULL)")
            conn.commit() 
            conn.close()
        

        


        def register():

            #PSMS_RegDatabase()
            login = StringVar('')  
            conn = sqlite3.connect("PSMS.db")
            cur = conn.cursor()
            if  Username.get() == "" or Password.get() == "" or role.get() == "" or Company_Name.get()=="":
                tkinter.messagebox.showerror("Pet Shop Management System", "Please require the completed field")
            else:
                cur.execute("SELECT * FROM user WHERE username = ?", (Username.get(),))
                if cur.fetchone() is not None:
                    tkinter.messagebox.showerror("Pet Shop Management System", "Username is already taken")
                else:
                    cur.execute("INSERT INTO user (username,password,role,Company_Name,login) VALUES(?, ?, ?, ?,?)", \
                               (Username.get(), Password.get(), role.get(),Company_Name.get(),login.get()))
                    cur.execute("UPDATE user SET login = 'Online' WHERE username = ?",(Username.get(),))
                    conn.commit()
                    #conn.close()
                    controller.show_frame(LoginPage)
                    Username.set("")
                    Password.set("")
                    Company_Name.set("")
                    role.set("")
                    tkinter.messagebox.showinfo("Pet Shop Management System", "Successfully created")        
            #conn.close()
        
        ##Labels,Entries and Buttons
        welcome = tk.Label(self, text= "Create your free account", font=("Arial Bold", 30), bd=0, bg="white", fg="grey23")
        welcome.place(x=205,y=100)
        
        welcome1 = tk.Label(self, text= "Already have an account?", font=("Courier", 15), bd=0, bg="white", fg="grey23")
        welcome1.place(x=215,y=145)
        
        signup_form = tk.LabelFrame(self, font= ("Poppins",20), text="Sign up", bg="white")
        signup_form.pack(fill="both",expand="yes", padx=480,pady=170)
        
        user_name = tk.Label(signup_form, font=("Poppins", 12), text="Username:", bg="white", padx=5, pady=5)
        user_name.place(x=20,y=10)
        user_name = tk.Entry(signup_form, font=("Poppins", 13), textvariable=Username, width=30)
        user_name.place(x=20,y=40)
        
        password = tk.Label(signup_form, font=("Poppins", 12), text="Password:", bg="white", padx=5, pady=5)
        password.place(x=20,y=80)
        password = tk.Entry(signup_form, font=("Poppins", 13), textvariable=Password, width=30)
        password.place(x=20,y=130)

        companyname = tk.Label(signup_form, font=("Poppins", 12), text="Company Name:", bg="white", padx=5, pady=5)
        companyname.place(x=20,y=170)
        companyname = tk.Entry(signup_form, font=("Poppins", 13), textvariable=Company_Name, width=30)
        companyname.place(x=20,y=220)
        
        role = tk.Label(signup_form, font=("Poppins", 12), text="Role:", bg="white", padx=5, pady=5)
        role.place(x=20,y=260)
        role = ttk.Combobox(signup_form, value=["Admin","Staff"],font=("Poppins", 12), state="readonly", textvariable=role, width=28)
        role.place(x=20,y=310)
        
        Button = tk.Button(self, text="Log in!", font=("Courier", 15, "bold"), bd=0, fg="gray30", bg="white", command= lambda: controller.show_frame(LoginPage))
        Button.place(x=510,y=140)
        
        Button = tk.Button(signup_form, text="Submit", width=15, font=("Arial Bold", 16), bg="gray50", fg="white", command=register )
        Button.place(x=65,y=350)
        
        PSMS_RegDatabase()
        
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Pet Shop Management System")
        
        tapps = StringVar()
        c_user = StringVar()
        company = StringVar()
        capps = StringVar()
        
        ##Pics
        self.pic = PhotoImage(file="p16.png", master=self) 
        self.picgo = PhotoImage(file="go2.png", master=self) 
        self.picbg = PhotoImage(file="bg.png", master=self) 
        
        app_pic = tk.Label(self, image = self.pic, bd=0)
        app_pic.place(x=50,y=450)
        
        app_picgo = tk.Label(self, image = self.picgo, bd=0)
        app_picgo.place(x=800,y=170)
        
        app_picbg = tk.Label(self, image = self.picbg, bd=0)
        app_picbg.place(x=470,y=0) 
        
        ##Labels
        
        
        ##Functions
        def setoffline():
            conn=sqlite3.connect("PSMS.db")
            cur=conn.cursor()
            cur.execute("SELECT username FROM user WHERE login ='Online'")
            username = cur.fetchone()
            cur.execute("UPDATE user SET login = '***' WHERE username = ?",(username,))
            conn.commit()
        def logout():
            iExit = tkinter.messagebox.askyesno("Pet Shop Management Sysytem","Do you want to log-out?")
            if iExit > 0:
                conn=sqlite3.connect("PSMS.db")
                cur=conn.cursor()
                cur.execute("UPDATE Appointment SET company_name = '***', username = '***'")
                
                #setoffline()
                conn.commit()
                conn.close()
                controller.show_frame(FirstPage)

                
        def ExitApplication():
            MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
            if MsgBox == 'yes':
                logout()
                app.destroy()
            else:
                tk.messagebox.showinfo('Return','You will now return to the application screen')
        
        def appointments():
            conn = sqlite3.connect("PSMS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM Appointment WHERE username != '-'")
            rows1 = cur.fetchall()
            tapps.set(len(rows1))
            self.ttlappointments = Label(self, font=("Helvetica", 40),textvariable = tapps, bg ="white", fg = "gray50")
            self.ttlappointments.place(x=610,y=540)
            self.after(1000,appointments)
            conn.commit()            
            conn.close()

        def completedappointments():
            conn=sqlite3.connect('PSMS.db')
            cur=conn.cursor()
            cur.execute("SELECT * FROM user WHERE login = 'Online'")
            item=cur.fetchall()
            for m in item:
                c_name = m[3]
            conn = sqlite3.connect("PSMS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM History WHERE Status = 'Completed' AND Company_Name = ?", (c_name,))
            rows = cur.fetchall()
            capps.set(len(rows))
            self.compappointments = Label(self, font=("Helvetica", 40),textvariable = capps, bg ="white", fg = "gray50")
            self.compappointments.place(x=610,y=620)
            self.after(1000,completedappointments)
            conn.commit()            
            conn.close()


        def Current_User():
            conn = sqlite3.connect("PSMS.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM user WHERE login = 'Online'")
            row = cur.fetchall()
            for i in row:
                #print(i)
                c_user.set(i[0])
            self.user = Label(self, font=("Helvetica", 60),textvariable = c_user, bg ="white", fg = "black")
            self.user.place(x=500,y=190)
            self.after(1000,Current_User)
            conn.commit()            
            conn.close()
         
         
        homelabel1 = tk.Label(self, text= "Hey there! ", font=("Helvetica", 60), bg="white", fg="grey23", anchor=CENTER)
        homelabel1.place(x=80,y=190)
        
        homelabel2 = tk.Label(self, text= "Got treats? We do.", font=("Courier", 40), bg="white", fg="grey23")
        homelabel2.place(x=40,y=330)
        
        homelabel3 = tk.Label(self, text= "Appointments", font=("Courier", 30), bg="white", fg="grey23")
        homelabel3.place(x=670,y=550)
        
        homelabel4 = tk.Label(self, text= "Get a few more barks for your bucks!", font=("Courier", 15), bg="white", fg="grey23")
        homelabel4.place(x=750,y=710)

        homelabel5 = tk.Label(self, text= "Completed Appointments", font=("Courier", 30), bg="white", fg="grey23")
        homelabel5.place(x=670,y=630)
        
        ##Buttons

        Button2 = tk.Button(self, text="HISTORY", font=("Courier", 12), bd=0, bg="white", fg="gray50",command= lambda: controller.show_frame(history))
        Button2.place(x=50,y=70)

        Button1 = tk.Button(self, text="APPOINTMENTS", font=("Courier", 12), bd=0, bg="white", fg="gray50", command= lambda: controller.show_frame(AddPage))
        Button1.place(x=150,y=70)
        
        Button1 = tk.Button(self, text="LOG OUT", font=("Courier", 12), bd=0, bg="white", fg="gray50", command= logout)
        Button1.place(x=300,y=70)
        
        Button1 = tk.Button(self, text="EXIT", font=("Courier", 12), bd=0, bg="white", fg="gray50", command=ExitApplication)
        Button1.place(x=400,y=70)        

        #Button1 = tk.Button(self, text="APPOINTMENTS", font=("Courier", 12), bd=0, bg="white", fg="gray50", command= lambda: controller.show_frame(AddPage))
        #Button1.place(x=50,y=70)
        
        #Button1 = tk.Button(self, text="LOG OUT", font=("Courier", 12), bd=0, bg="white", fg="gray50", command= logout)
        #Button1.place(x=200,y=70)
        
        #Button1 = tk.Button(self, text="EXIT", font=("Courier", 12), bd=0, bg="white", fg="gray50", command=ExitApplication)
        #Button1.place(x=300,y=70)
        appointments()
        Current_User()
        completedappointments()
        

class AddPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Pet Shop Management System")
        
        CustomerID= StringVar()
        Customer_name = StringVar()
        Customer_mno = StringVar()
        PetID= StringVar()
        Breed = StringVar()
        Pet_type = StringVar()
        AppointmentID = StringVar()
        Appointment_details = StringVar()
        Status = StringVar()
        Appointment_Date = StringVar()
        SearchBar_Var = StringVar()
        role = []
        
        ##Pics
        self.pica = PhotoImage(file="g1.png", master=self) 
        self.picb = PhotoImage(file="h1.png", master=self) 
        self.picc = PhotoImage(file="bi.png", master=self)
        self.picd = PhotoImage(file="bi1.png", master=self)
        self.pice = PhotoImage(file="bi2.png", master=self)
        self.picf = PhotoImage(file="appo2.png",master=self)
        self.btna = PhotoImage(file="j.png", master=self) 
        self.btnb = PhotoImage(file="p2.png", master=self) 
        self.btnc = PhotoImage(file="p3.png", master=self)
        self.btnd = PhotoImage(file="ap5.png",master=self)
        self.btne = PhotoImage(file="house1.png",master=self)
        self.btnf = PhotoImage(file="histo.png",master=self)
        
        
        app_pica = tk.Label(self, image = self.pica, bd=0)
        app_pica.place(x=30,y=25)
        
        app_picb = tk.Label(self, image = self.picb, bd=0)
        app_picb.place(x=800,y=0)
        
        app_picc = tk.Label(self, image = self.picc, bd=0)
        app_picc.place(x=560,y=30)
        
        app_picd = tk.Label(self, image = self.picd, bd=0)
        app_picd.place(x=440,y=30)
        
        app_pice = tk.Label(self, image = self.pice, bd=0)
        app_pice.place(x=500,y=30)
        
        app_picf = tk.Label(self, image = self.picf, bd=0)
        app_picf.place(x=50,y=770)

        def ondoubleclick(event):
            #update()
            x = self.tree.selection()[0]
            values = self.tree.item(x,"values")
            CustomerID.set(values[0])
            Customer_name.set(values[1])
            Customer_mno.set(values[2])
            PetID.set(values[3])
            Breed.set(values[4])
            Pet_type.set(values[5])
            AppointmentID.set(values[6])
            Appointment_details.set(values[7])
            Status.set(values[8])
            Appointment_Date.set(values[9])
            update()
        def onrightclick(event):
            x = self.tree.selection()
            values = self.tree.item(x,"values")
            CustomerID.set(values[0])
            Customer_name.set(values[1])
            Customer_mno.set(values[2])
            PetID.set(values[3])
            Breed.set(values[4])
            Pet_type.set(values[5])
            AppointmentID.set(values[6])
            Appointment_details.set(values[7])
            Status.set(values[8])
            Appointment_Date.set(values[9])
            updatestat()

        def clear():
            CustomerID.set('')
            Customer_name.set('')
            Customer_mno.set('')
            PetID.set('')
            Breed.set('')
            Pet_type.set('')
            AppointmentID.set('')
            Appointment_details.set('')
            Status.set('')
            Appointment_Date.set('')
            SearchBar_Var.set('')

                        


        #Treeview
        style = ttk.Style(self)
        style.configure("Treeview",
            background = "silver",
            foreground = "black",
            fieldbackground = "silver"
            )
        style.map('Treeview',background=[('selected','deep sky blue')])
        scroll_y=Scrollbar(self, orient=VERTICAL)

        self.tree = ttk.Treeview(self, height=10, columns=("CustomerID","Customer_name","Customer_mno","PetID","Breed","Pet_type","AppointmentID", \
                                                            "Appointment_details", "Status","Appointment_Date"), yscrollcommand=scroll_y.set)

        #scroll_y.pack(side=RIGHT, fill=Y)
        #scroll_y.place(x=600,y=600)
        
        self.tree.heading("CustomerID", text="Customer ID")
        self.tree.heading("Customer_name", text="Name")
        self.tree.heading("Customer_mno", text="Phone number")
        self.tree.heading("PetID", text="Pet ID")
        self.tree.heading("Breed", text="Breed")
        self.tree.heading("Pet_type", text="Type")
        self.tree.heading("AppointmentID", text="Appointment ID")
        self.tree.heading("Appointment_details", text="Details")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Appointment_Date", text="Date")
        self.tree['show'] = 'headings'

        self.tree.column("CustomerID", width=60)
        self.tree.column("Customer_name", width=110)
        self.tree.column("Customer_mno", width=70)
        self.tree.column("PetID", width=50)
        self.tree.column("Breed", width=100)
        self.tree.column("Pet_type", width=40)
        self.tree.column("AppointmentID", width=70)
        self.tree.column("Appointment_details", width=170)
        self.tree.column("Status", width=50)
        self.tree.column("Appointment_Date", width=50)

        self.tree.bind("<Double-Button-1>", ondoubleclick)
        self.tree.bind("<Return>", onrightclick)
        
        #self.tree.pack(fill=BOTH,expand=1)
        
        self.tree.place(x=50,y=205,width=1195,height=560)
        #scroll_y.config(command=self.tree.yview)
        #displayData()


        ##Functions                                                      ######################################################################################################

        
        #breed_list = ["","GERMAN", "POODLE" ] 
        #type_list = ["","DOG","CAT" ]
        #date_list = ["", "01/01/2021","01/02/2021","01/03/2021","01/04/2021","01/05/2021","01/06/2021","01/07/2021","01/08/2021","01/09/2021","01/10/2021",
        #             "01/11/2021","01/12/2021","01/13/2021","01/14/2021","01/15/2021","01/16/2021","01/17/2021","01/18/2021","01/19/2021","01/20/2021",
        #             "01/21/2021","01/22/2021","01/23/2021","01/24/2021","01/25/2021","01/26/2021","01/27/2021","01/28/2021","01/29/2021","01/30/2021",
        #             "01/31/2021","02/01/2021","02/02/2021","02/03/2021","02/04/2021","02/05/2021","02/06/2021","02/07/2021","02/08/2021","02/09/2021",
        #             "02/10/2021","02/11/2021","02/12/2021","02/13/2021","02/14/2021","02/15/2021","02/16/2021","02/17/2021","02/18/2021","02/19/2021",
        #             "02/20/2021","02/21/2021","02/22/2021","02/23/2021","02/24/2021","02/25/2021","02/26/2021","02/27/2021","02/28/2021"]


        def add():
            clear()
            global breed_list
            global type_list
            global date_list
            win = Toplevel()
            win.title("Add")
            win.geometry("600x680")
            win.resizable(False,False)
            win.configure(background="white")

            Label(win, text= "ADD APPOINTMENT",font=("Courier", 20),fg="gray50",bg="white",width=32).place(x=120,y=15)
            ######### Autofill #######################


            def dates(data):
                datelist.delete(0,END)
                for item in data:
                    datelist.insert(END, item)

            def filloutdates(event):
                App_date.delete(0, END)
                App_date.insert(0,datelist.get(ACTIVE))

            def checkdates(event):
                click = App_date.get()

                if click =='':
                    data = date_list
                else:
                    data = []
                    for i in date_list:
                        if click.lower() in i.lower():
                            data.append(i)
                    dates(data)


            #========================================# 
         

            def breeds(data):
                breedlist.delete(0, END)
                for item in data:
                    breedlist.insert(END, item)

            def fillout(event):
                breed.delete(0,END)
                breed.insert(0,breedlist.get(ACTIVE))

            def check(event):
                click = breed.get()

                if click == '':
                    data = breed_list
                else:
                    data = []
                    for i in breed_list:
                        if click.lower() in i.lower():
                            data.append(i)
                breeds(data)
            #=========================================#
            def pettypes(data):
                typelist.delete(0,END)
                for item in data:
                    typelist.insert(END, item)


            def fillout1(event):
                pettype.delete(0,END)
                pettype.insert(0,typelist.get(ACTIVE))


            def check1(event):
                click = pettype.get()
                if click =="":
                    data = type_list
                else:
                    data = []
                    for i in type_list:
                        if click.lower() in i.lower():
                            data.append(i)
                pettypes(data) 
            #========================================#           

        
            frame1= LabelFrame(win,  width=51, bg="white",fg="grey24", text="Appointment Form", font= ("Courier",20))
            frame1.place(x= 5,y=50,height=615,width=590)
            
        
            self.pic1a = PhotoImage(file="g2.png", master=self) 
        
            pic1a = tk.Label(win, image = self.pic1a, bd=0)
            pic1a.place(x=500,y=0)
            
            LCus_name = Label(frame1, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Customer Name:")
            LCus_name.place(x=20, y=10,width=151 )
            Cus_name = Entry(frame1, font=("Courier", 14),textvariable = Customer_name, width=33, bg="snow",fg="grey24",highlightthickness=2)
            Cus_name.place(x=180, y=10)
            

            LCus_ID = Label(frame1, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Customer ID:")
            LCus_ID.place(x=20, y=60,width=147 )
            Cus_ID = Entry(frame1, font=("Courier", 14),textvariable = CustomerID, width=33, bg="snow",fg="grey24",highlightthickness=2)
            Cus_ID.place(x=180, y=60)
            
            
            
            LCus_mno = Label(frame1, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Mobile No.:")
            LCus_mno.place(x=20, y=110,width=140 )
            Cus_mno = Entry(frame1, font=("Courier", 14),textvariable = Customer_mno, width=33, bg="snow",fg="grey24",highlightthickness=2)
            Cus_mno.place(x=180, y=110)
           
            
            
            Lpet_ID = Label(frame1, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Pet ID:")
            Lpet_ID.place(x=20, y=160,width=80 )            
            pet_ID = Entry(frame1, font=("Courier", 14),textvariable = PetID, width=33, bg="snow",fg="grey24",highlightthickness=2)
            pet_ID.place(x=180, y=160)
          
            
            
            Lpettype  = Label(frame1, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Pet Type:")
            Lpettype.place(x=20, y=210,width=100 )
            pettype = Entry(frame1, font=("Courier", 14),textvariable = Pet_type, width=33, bg="snow",fg="grey24",highlightthickness=2)
            pettype.place(x=180, y=210)
            typelist = Listbox(frame1, width=61,height=1,bg="snow",bd=0)
            typelist.place(x=180, y=230)
            
            
            
            Lbreed  = Label(frame1, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Breed:")
            Lbreed.place(x=20, y=270,width=100 )
            breed = Entry(frame1, font=("Courier", 14),textvariable = Breed, width=33, bg="snow",fg="grey24",highlightthickness=2)
            breed.place(x=180, y=270)
            breedlist = Listbox(frame1, width=61,height=1,bg="snow",bd=0)
            breedlist.place(x=180, y=290)
            
            
            
            LApp_ID = Label(frame1, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Appointment ID:")
            LApp_ID.place(x=20, y=320,width=160 )
            App_ID = Entry(frame1, font=("Courier", 14),textvariable = AppointmentID, width=33, bg="snow",fg="grey24",highlightthickness=2)
            App_ID.place(x=180, y=320)
            
            
            LApp_det = Label(frame1, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Details:")
            LApp_det.place(x=20, y=370,width=90 )
            App_det = Entry(frame1, font=("Courier", 14),textvariable = Appointment_details, width=33, bg="snow",fg="grey24",highlightthickness=2)
            App_det.place(x=180, y=370)
            
            
            LApp_date = Label(frame1, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Date:")
            LApp_date.place(x=20, y=420,width=70 )
            App_date = Entry(frame1, font=("Courier", 14),textvariable = Appointment_Date, width=33, bg="snow",fg="grey24",highlightthickness=2)
            App_date.place(x=180, y=420)
            datelist = Listbox(frame1, width=61,height=1,bg="snow",bd=0)
            datelist.place(x=180, y=440)
           

            dates(date_list)
            datelist.bind("<<ListboxSelect>>",filloutdates)
            App_date.bind("<KeyRelease>", checkdates)

            breeds(breed_list)
            breedlist.bind("<<ListboxSelect>>", fillout)
            breed.bind("<KeyRelease>" ,check) 

            pettypes(type_list)
            typelist.bind("<<ListboxSelect>>",fillout1)
            pettype.bind("<KeyRelease>",check1)


            Lstat  = Label(frame1, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Status:")
            Lstat.place(x=20, y=470,width=80 )
            stat = Entry(frame1, font=("Courier", 14),textvariable = Status , width=33, bg="snow",fg="grey24",highlightthickness=2)
            #stat = ttk.Combobox(frame1, font=("Courier", 14),value=["Processing","Completed","Cancelled"], textvariable = Status, width=31,state='readonly')
            stat.place(x=180, y=470)
            stat.insert(0,"Processing")

           

            def addApp():
                global role

                conn=sqlite3.connect('PSMS.db')
                cur=conn.cursor()
                cur.execute("SELECT * FROM user WHERE login = 'Online'")
                #cur.execute("SELECT * FROM Appointment WHERE username != '-' AND company_name != '-' ")
                item=cur.fetchall()
                for m in item:
                    n = m[0]#NAME
                    role = m[2]
                    c_name = m[3]
                    #cur.execute("SELECT * FROM user WHERE username = ?",(n,))
                    #userrow = cur.fetchall()
                    #for k in userrow:
                        #role = k[2]
                        #if role == k[2]:#role
                            #cur.execute("SELECT * FROM user WHERE role = ? AND username = ?",(role,n))
                            #row = cur.fetchall()
                            #for c in row:
                                #c_name = c[3] #company name


                #conn.commit()
                if role == 'Admin':
                    if Customer_name.get()=="" or CustomerID.get()=="" or Customer_mno.get()=="" or Appointment_Date.get()=="" or PetID.get()=="" or AppointmentID.get()=="" or Status.get()=="":
                        tkinter.messagebox.showinfo("Pet Shop Management System","Please Fill All the Entries")
                    else:
                        #customer_ID
                        #conn=sqlite3.connect('PSMS.db')
                        #cur=conn.cursor()
                        #cur.execute("SELECT * FROM CUSTOMER")
                        #cus = cur.fetchall()
                        #for customer in cus:
                            #if customer[0] == CustomerID.get() or customer[1] == Customer_name.get():
                                #clear()
                                #win.destroy()
                                #conn.commit()
                                #tkinter.messagebox.showinfo("Pet Shop Management System","The Customer is already exist")
                        #PET_ID
                        cur.execute("SELECT * FROM PET")
                        pets = cur.fetchall()
                        for pet in pets:
                            if pets == PetID.get():
                                win.destroy()
                                conn.commit()
                                tkinter.messagebox.showinfo("Pet Shop Management System","The PET ID is already not available anymore")
                                clear()

                        #APP_ID
                        cur.execute("SELECT * FROM Appointment")
                        appoint = cur.fetchall()
                        for appointment in appoint:
                            if appointment[0] == AppointmentID.get():
                                win.destroy()
                                conn.commit()
                                tkinter.messagebox.showinfo("Pet Shop Management System","The APPOINTMENT ID is already exist")
                                clear()



                        x = AppointmentID.get()
                        appidlist = []
                        for i in x:
                            appidlist.append(i)
                        if "-" in appidlist:
                            y=x.split("-") 
                            Cname = y[0]
                            if Cname  != c_name:
                                win.destroy()
                                conn.commit()
                                tkinter.messagebox.showinfo("Pet Shop Management System","Invalid Appointment ID")
                                clear()


                            conn=sqlite3.connect('PSMS.db')
                            cur=conn.cursor()
                            cur.execute("PRAGMA foreign_keys = ON")
                            cur.execute("SELECT * FROM CUSTOMER WHERE customer_id = ?",(CustomerID.get(),))
                            row=cur.fetchall()
                            if row != []:
                                cur.execute("SELECT Customer_id FROM Appointment WHERE Customer_id = ?", (CustomerID.get(),))
                                Id = cur.fetchall()
                                if Id != []:
                                    tkinter.messagebox.showinfo("Pet Shop Management System","The Customer is having a Appointment on another Company")
                                    win.destroy()
                                    conn.commit()
                                    conn.close()
                                else:                           
                                    cur.execute("INSERT INTO PET(Pet_id,Breed,type,Customer_id) VALUES(?,?,?,?)",(pet_ID.get(),breed.get(),pettype.get(),Cus_ID.get()))
                                    cur.execute("INSERT INTO Appointment(Appointment_ID,Appointment_details,appointment_date,Status,Customer_id,company_name,username) \
                                        VALUES(?,?,?,?,?,?,?)",(App_ID.get(),App_det.get(),App_date.get(),stat.get(),Cus_ID.get(),c_name,n))
                                    tkinter.messagebox.showinfo("Pet Shop Management System","Appointment Recorded Successfully")
                                    win.destroy()
                                    conn.commit()
                                    conn.close()
                                    #clear()
                                    display()
                                       
                            else:# MAKING A NEW CUSTOMER

                                    cur.execute("INSERT INTO Customer(Customer_id,Customer_name,Mobile_no) VALUES(?,?,?)",(CustomerID.get(),Cus_name.get(),Cus_mno.get()))                                
                                    cur.execute("INSERT INTO PET(Pet_id,Breed,type,Customer_id) VALUES(?,?,?,?)",(pet_ID.get(),breed.get(),pettype.get(),Cus_ID.get()))
                                    cur.execute("INSERT INTO Appointment(Appointment_ID,Appointment_details,appointment_date,Status,Customer_id,company_name,username) \
                                        VALUES(?,?,?,?,?,?,?)",(App_ID.get(),App_det.get(),App_date.get(),stat.get(),Cus_ID.get(),c_name,n))
                                    tkinter.messagebox.showinfo("Pet Shop Management System","Appointment Recorded Successfully")
                                    win.destroy()
                                    conn.commit()
                                    conn.close()
                                    #clear()
                                    display()
                                #tkinter.messagebox.showinfo("Pet Shop Management System","Invalid")


                            #else:   
                                #try:
#                                    cur.execute("INSERT INTO Customer(Customer_id,Customer_name,Mobile_no) VALUES(?,?,?)",(Cus_ID.get(),Cus_name.get(),Cus_mno.get()))
#                                    cur.execute("INSERT INTO PET(Pet_id,Breed,type,Customer_id) VALUES(?,?,?,?)",(pet_ID.get(),breed.get(),pettype.get(),Cus_ID.get()))
#                                    cur.execute("INSERT INTO Appointment(Appointment_ID,Appointment_details,appointment_date,Status,Customer_id,company_name,username) \
#                                        VALUES(?,?,?,?,?,?,?)",(App_ID.get(),App_det.get(),App_date.get(),stat.get(),Cus_ID.get(),c_name,n))
#                                    tkinter.messagebox.showinfo("Pet Shop Management System","Appointment Recorded Successfully")
#                                    win.destroy()
#                                    conn.commit()
#                                    clear()
#                                    display()
#                                except:
#                                    win.destroy()
#                                    clear()
#                                    display()
                                        #tkinter.messagebox.showinfo("Pet Shop Management System","Invalid")
                        #except:
                            #win.destroy()
                          #  clear()
                          #  display()
                            #tkinter.messagebox.showinfo("Pet Shop Management System","The PET ID is already exist")

                            #tkinter.messagebox.showinfo("Pet Shop Management System","Invalid")



                else:
                    win.destroy()
                    tkinter.messagebox.showinfo("Pet Shop Management System","Only The Admin can ADD Appoinment")





            but2= tk.Button(frame1,font=("Courier", 14),width=20,text="SUBMIT",bg="gray50",fg="white",command=addApp)
            but2.place(x=200,y=520,height=50)




        def update():
            global breed_list
            global type_list
            global date_list
            win2 = Toplevel()
            win2.title("EDIT DATA")
            win2.geometry("600x690")
            win2.resizable(False,False)
            win2.configure(background="white")

            Label(win2, text= "EDIT APPOINTMENT",font=("Courier", 20),fg="gray50",bg="white",width=32).place(x=100,y=15)
            
            
            
            frame2= LabelFrame(win2,  width=51, bg="white",fg="grey24", font= ("Courier",20))
            frame2.place(x= 5,y=60,height=615,width=590)
            
        
            self.pic1ab = PhotoImage(file="g2a.png", master=self) 
        
            pic1a = tk.Label(win2, image = self.pic1ab, bd=0)
            pic1a.place(x=500,y=0)
            
            LCus_name1 = Label(frame2, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Customer Name:")
            LCus_name1.place(x=20, y=10,width=151 )
            Cus_name1 = Entry(frame2, font=("Courier", 14),textvariable = Customer_name, width=33, bg="snow",fg="grey24",highlightthickness=2)
            Cus_name1.place(x=180, y=10)
            

            LCus_ID1 = Label(frame2, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Customer ID:")
            LCus_ID1.place(x=20, y=60,width=147 )
            Cus_ID1 = Entry(frame2, font=("Courier", 14),textvariable = CustomerID, width=33, bg="snow",fg="grey24",highlightthickness=2)
            Cus_ID1.place(x=180, y=60)
            
            
            
            LCus_mno1 = Label(frame2, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Mobile No.:")
            LCus_mno1.place(x=20, y=110,width=140 )
            Cus_mno1 = Entry(frame2, font=("Courier", 14),textvariable = Customer_mno, width=33, bg="snow",fg="grey24",highlightthickness=2)
            Cus_mno1.place(x=180, y=110)
           
            
            
            Lpet_ID1 = Label(frame2, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Pet ID:")
            Lpet_ID1.place(x=20, y=160,width=80 )            
            pet_ID1 = Entry(frame2, font=("Courier", 14),textvariable = PetID, width=33, bg="snow",fg="grey24",highlightthickness=2)
            pet_ID1.place(x=180, y=160)
          
            
            
            Lpettype1  = Label(frame2, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Pet Type:")
            Lpettype1.place(x=20, y=210,width=100 )
            pettype1 = Entry(frame2, font=("Courier", 14),textvariable = Pet_type, width=33, bg="snow",fg="grey24",highlightthickness=2)
            pettype1.place(x=180, y=210)
            typelist1 = Listbox(frame2, width=61,height=1,bg="snow",bd=0)
            typelist1.place(x=180, y=230)
            
            
            
            LApp_ID1 = Label(frame2, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Appointment ID:")
            LApp_ID1.place(x=20, y=320,width=160 )
            App_ID1 = Entry(frame2, font=("Courier", 14),textvariable = AppointmentID, width=33, bg="snow",fg="grey24",highlightthickness=2)
            App_ID1.place(x=180, y=320)
            
            
            LApp_det1 = Label(frame2, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Details:")
            LApp_det1.place(x=20, y=370,width=90 )
            App_det1 = Entry(frame2, font=("Courier", 14),textvariable = Appointment_details, width=33, bg="snow",fg="grey24",highlightthickness=2)
            App_det1.place(x=180, y=370)
            
            
            LApp_date1 = Label(frame2, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Date:")
            LApp_date1.place(x=20, y=420,width=70 )
            App_date1 = Entry(frame2, font=("Courier", 14),textvariable = Appointment_Date, width=33, bg="snow",fg="grey24",highlightthickness=2)
            App_date1.place(x=180, y=420)
            datelist1 = Listbox(frame2, width=61,height=1,bg="snow",bd=0)
            datelist1.place(x=180, y=440)
            
            
            Lstat1  = Label(frame2, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Status:")
            Lstat1.place(x=20, y=470,width=80 )
            stat1 = Entry(frame2, font=("Courier", 14),textvariable =Status , width=33, bg="snow",fg="grey24",highlightthickness=2)
            #stat1 = ttk.Combobox(frame2, font=("Courier", 14),value=["Processing","Completed","Cancelled"], textvariable = Status, width=31,state='readonly')
            stat1.place(x=180, y=470)
            

            def breeds1(data):
                breedlist1.delete(0, END)
                for item in data:
                    breedlist1.insert(END, item)

            def filloutbreed1(event):
                breed1.delete(0,END)
                breed1.insert(0,breedlist1.get(ACTIVE))


            def checkbreed1(event):
                click = breed1.get()

                if click == '':
                    data = breed_list
                else:
                    data = []
                    for i in breed_list:
                        if click.lower() in i.lower():
                            data.append(i)


                breeds1(data)

            
            Lbreed1  = Label(frame2, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Breed:")
            Lbreed1.place(x=20, y=270,width=100 )
            breed1 = Entry(frame2, font=("Courier", 14),textvariable = Breed, width=33, bg="snow",fg="grey24",highlightthickness=2)
            breed1.place(x=180, y=270)
            breedlist1 = Listbox(frame2, width=61,height=1,bg="snow",bd=0)
            breedlist1.place(x=180, y=290)
            
            breeds1(breed_list)
            breedlist1.bind("<<ListboxSelect>>", filloutbreed1)
            breed1.bind("<KeyRelease>" ,checkbreed1)

            def pettypes1(data):
                typelist1.delete(0,END)
                for item in data:
                    typelist1.insert(END, item)

            def fillouttype1(event):
                pettype1.delete(0,END)
                pettype1.insert(0,typelist1.get(ACTIVE))


            def checktype1(event):
                click = pettype1.get()
                if click =="":
                    data = type_list
                else:
                    data = []
                    for i in type_list:
                        if click.lower() in i.lower():
                            data.append(i)
                pettypes1(data)

                    
            pettypes1(type_list)
            typelist1.bind("<<ListboxSelect>>",fillouttype1)
            pettype1.bind("<KeyRelease>",checktype1)

            def dates1(data):
                datelist1.delete(0,END)
                for item in data:
                    datelist1.insert(END, item)

            def filloutdates1(event):
                App_date1.delete(0, END)
                App_date1.insert(0,datelist1.get(ACTIVE))

            def checkdates1(event):
                click = App_date1.get()

                if click =='':
                    data = date_list
                else:
                    data = []
                    for i in date_list:
                        if click.lower() in i.lower():
                            data.append(i)
                    dates1(data)
                    
            dates1(date_list)
            datelist1.bind("<<ListboxSelect>>",filloutdates1)
            App_date1.bind("<KeyRelease>", checkdates1)
            
            
                    
            def updatedata():
                slctd = self.tree.selection()
                for i in slctd:
                    conn=sqlite3.connect("PSMS.db")
                    cur=conn.cursor()
                    cur.execute("UPDATE Customer SET Customer_id=?,Customer_name=?,Mobile_no=?\
                        WHERE Customer_id =?",(CustomerID.get(),Customer_name.get(),Customer_mno.get(),self.tree.set(i,"#1")))
                    cur.execute("UPDATE PET SET Pet_id = ?, Breed=?, type=?,Customer_id=? WHERE Customer_id = ?",\
                        (PetID.get(),Breed.get(),Pet_type.get(),CustomerID.get(),self.tree.set(i,"#1")))
                    cur.execute("UPDATE Appointment SET Appointment_ID=?,Appointment_details=?,Status=?,appointment_date=?,Customer_id=?\
                        WHERE Customer_id=?",(AppointmentID.get(),Appointment_details.get(),Status.get(),Appointment_Date.get(),CustomerID.get(),self.tree.set(i,"#1")))

                    win2.destroy()
                    conn.commit()
                    tkinter.messagebox.showinfo("Pet Shop Management System","Customer Updated Successfully")
                    clear()
                    display()

            but6= tk.Button(frame2,font=("Courier", 14),width=20,text="SUBMIT",bg="gray50",fg="white",command=updatedata)
            but6.place(x=200,y=520,height=50)

        def search():
            for i in self.tree.get_children():
                self.tree.delete(i)

            search = self.SearchBar.get()
            conn=sqlite3.connect("PSMS.db")
            cur=conn.cursor()
            cur.execute("SELECT * FROM Customer INNER JOIN PET INNER JOIN Appointment ON Customer.Customer_id = PET.Customer_id AND Customer.Customer_id = Appointment.Customer_id")
            rows=cur.fetchall()
            
            for row in rows:
                if row[0].startswith(search) or row[1].startswith(search) or row[2].startswith(search) or row[3].startswith(search) or row[4].startswith(search) or row[5].startswith(search) or row[7].startswith(search) or row[8].startswith(search) or row[9].startswith(search) or row[10].startswith(search):
                    self.tree.insert("", tk.END,text=row[0], values=(row[0],row[1],row[2],row[3],row[4],row[5],row[7],row[8],row[9],row[10]))

            conn.close()

        def deletedata():
            global role
            conn=sqlite3.connect('PSMS.db')
            cur=conn.cursor()
            cur.execute("SELECT * FROM user WHERE login = 'Online'")
            #cur.execute("SELECT * FROM Appointment WHERE username != '-' AND company_name != '-' ")
            item=cur.fetchall()
            for m in item:
                role = m[2]#role
                response = messagebox.askyesno("Are you sure you want to delete this??")                              
                if response > 0:
                    if role == 'Admin':
                        click = self.tree.selection()[0]
                        cus_id = self.tree.item(click)["values"][0]
                        conn = sqlite3.connect("PSMS.db")
                        cur=conn.cursor()
                        cur.execute("SELECT * FROM Customer INNER JOIN PET INNER JOIN Appointment ON Customer.Customer_id = PET.Customer_id \
                            AND Customer.Customer_id = Appointment.Customer_id")
                        rows = cur.fetchall()
                        for row in rows:
                            if cus_id == row[0]:
                                cus_id = row[0]
                    
                        cur.execute("DELETE FROM Appointment WHERE Customer_id = ?", (cus_id,))
                        cur.execute("DELETE FROM PET WHERE Customer_id = ?", (cus_id,))

                        conn.commit()
                        self.tree.delete(click)
                        display()
                    else:
                        tkinter.messagebox.showinfo("Pet Shop Management System","Only The Admin can DELETE Appointment")



        def display():
            self.tree.tag_configure('oddrow',background="white")
            self.tree.tag_configure('evenrow',background="silver")
            for i in self.tree.get_children():
                self.tree.delete(i)
            conn = sqlite3.connect("PSMS.db")
            cur= conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("SELECT * FROM Customer INNER JOIN PET INNER JOIN Appointment ON Customer.Customer_id = PET.Customer_id \
                AND Customer.Customer_id = Appointment.Customer_id WHERE Appointment.username != '-' AND Appointment.company_name != '-' \
                AND Appointment.Status ='Processing'")
            conn.commit()
          
            rows = cur.fetchall()
            count=0
            for row in rows:
                if count % 2 == 0:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(row[0],row[1],row[2],row[3],row[4],row[5],row[7],row[8],row[9],row[10]), tags=('evenrow',))
                else:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(row[0],row[1],row[2],row[3],row[4],row[5],row[7],row[8],row[9],row[10]), tags=('oddrow',))
                count +=1
            conn.commit()
            conn.close()

        def updatestat():
            up=Toplevel()
            up.title("UPDATE STATUS")
            up.geometry("230x150")
            Label(up, text = "STATUS",fg="grey24", font=("Courier", 14)).place(x=80,y=10)

            #Lstat1  = Label(up, width=50, bg="snow",fg="grey24", font=("Courier", 14),text="Status:")
            #Lstat1.place(x=50, y=10,width=80 )
            stat1 = ttk.Combobox(up, font=("Courier", 14),value=["Completed","Cancelled"], textvariable = Status, width=17,state='readonly')
            stat1.place(x=10, y=50)

            def Selectstat():
                conn=sqlite3.connect('PSMS.db')
                cur=conn.cursor()
                cur.execute("SELECT * FROM Appointment WHERE username != '-' AND company_name != '-' ")
                item=cur.fetchall()
                for m in item:
                    n = m[6]#NAME
                    cur.execute("SELECT * FROM user WHERE username = ?",(n,))
                    userrow = cur.fetchall()
                    for k in userrow:
                        role = k[2]
                        if role == k[2]:#role
                            cur.execute("SELECT * FROM user WHERE role = ? AND username = ?",(role,n))
                            row = cur.fetchall()
                            for c in row:
                                c_name = c[3]
                slctd = self.tree.selection()
                for i in slctd:
                    conn = sqlite3.connect("PSMS.db")
                    cur=conn.cursor()
                    cur.execute("UPDATE Appointment SET Status = ? WHERE Appointment_id = ?",(Status.get(),AppointmentID.get()))
                    cur.execute("INSERT INTO History(Appointment_ID,Appointment_details,appointment_date,Status,Customer_id,company_name,Pet_id)VALUES(?,?,?,?,?,?,?)",\
                        (AppointmentID.get(),Appointment_details.get(),Appointment_Date.get(),Status.get(),CustomerID.get(),c_name,PetID.get()))
                #cur.execute("UPDATE History SET company_name = '***' WHERE Appointment_id = ?",(AppointmentID.get(),))
                cur.execute("DELETE FROM Appointment WHERE Status = ?", (Status.get(),))
                cur.execute("DELETE FROM PET WHERE Customer_id = ?",(CustomerID.get(),))
                up.destroy()
                conn.commit()
                tkinter.messagebox.showinfo("Pet Shop Management System","Status Updated Successfully")
                display()
                clear()

            but3= tk.Button(up,font=("Courier", 14),width=10,text="ENTER",bg="gray50",fg="white",command = Selectstat)
            but3.place(x=50,y=90,height=30)

        def clickevent(event):
            for i in self.tree.get_children():
                self.tree.delete(i)
                #Button.bind("<Button-1>",clickevent)
            #   statcolor()
            #display() 

        ##Labels,Entries, and Buttons in the Page
        title = tk.Label(self, text= "Pet Shop Management System", font=("Courier", 25), bg="white", bd=0, fg="grey23")
        title.place(x=250,y=80)

        pagetitle = tk.Label(self, text= "APPOINTMENTS", font=("Courier", 10, "bold"), bg="white", bd=0, fg="grey23")
        pagetitle.place(x=85,y=780)
        
        #self.ref = tk.Button(self, bd=0, bg="white",command=resfresh)#add
        #self.ref.place(x=830,y=165)
        #self.btnadd.config(cursor= "hand2")


        self.SearchBar = Entry(self, font=("Courier", 14), textvariable=SearchBar_Var, width=47,bg="snow",fg="grey23")
        self.SearchBar.place(x=250,y=170)
        self.SearchBar.insert(0,'Search here')

        self.btnsearch = tk.Button(self, image=self.btna, bd=0, bg="white",command=search)
        self.btnsearch.place(x=775,y=170)
        self.btnsearch.config(cursor= "hand2")

        self.btnrefresh = tk.Button(self, image=self.btnd, bd=0, bg="white",command=display)
        self.btnrefresh.place(x=200,y=165)
        self.btnrefresh.config(cursor= "hand2")


        self.btnadd = tk.Button(self, image=self.btnb, bd=0, bg="white",command=add)#add
        self.btnadd.place(x=830,y=165)
        self.btnadd.config(cursor= "hand2")

        self.btndel = tk.Button(self, image=self.btnc, bd=0, bg="white",command=deletedata)#delete
        self.btndel.place(x=880,y=162)
        self.btndel.config(cursor= "hand2")

        self.btnhom = tk.Button(self, image=self.btne, bd=0, bg="white",command=lambda: controller.show_frame(HomePage))
        self.btnhom.place(x=100,y=165)
        self.btnhom.config(cursor= "hand2")
        self.btnhom.bind("<Button-1>",clickevent)
        
        self.btnhisto = tk.Button(self, image=self.btnf, bd=0, bg="white",command=lambda: controller.show_frame(history))
        self.btnhisto.place(x=158,y=165)
        self.btnhisto.config(cursor= "hand2")
        
        #Button = tk.Button(self, text="Home", font=("Courier", 12, "bold"), bd=0, bg="white", fg="grey23", command= lambda: controller.show_frame(HomePage))
        #Button.place(x=450,y=90)
        #Button.bind("<Button-1>",clickevent)

        #display()

class history(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("PSMS")

        ##Pics
        self.pica = PhotoImage(file="g1.png", master=self) 
        self.picb = PhotoImage(file="h1.png", master=self) 
        self.picc = PhotoImage(file="bi.png", master=self)
        self.picd = PhotoImage(file="bi1.png", master=self)
        self.pice = PhotoImage(file="bi2.png", master=self)
        self.picf = PhotoImage(file="histo2.png",master=self)
        self.btna = PhotoImage(file="j.png", master=self) 
        self.btnb = PhotoImage(file="p2.png", master=self) 
        self.btnc = PhotoImage(file="p3.png", master=self)
        self.btnd = PhotoImage(file="ap5.png",master=self) 
        self.btne = PhotoImage(file="house1.png",master=self)
        self.btng = PhotoImage(file="appo2.png",master=self)
        
        app_pica = tk.Label(self, image = self.pica, bd=0)
        app_pica.place(x=30,y=25)
        
        app_picb = tk.Label(self, image = self.picb, bd=0)
        app_picb.place(x=800,y=0)

        app_picc = tk.Label(self, image = self.picc, bd=0)
        app_picc.place(x=560,y=30)
        
        app_picd = tk.Label(self, image = self.picd, bd=0)
        app_picd.place(x=440,y=30)
        
        app_pice = tk.Label(self, image = self.pice, bd=0)
        app_pice.place(x=500,y=30)
        
        app_picf = tk.Label(self, image = self.picf, bd=0)
        app_picf.place(x=50,y=770)
        
        SearchBar_Var = StringVar()

        #Treeview
        style = ttk.Style(self)
        style.configure("Treeview",
            background = "silver",
            foreground = "black",
            fieldbackground = "silver"
            )
        style.map('Treeview',background=[('selected','deep sky blue')])
        scroll_y=Scrollbar(self, orient=VERTICAL)

        self.tree = ttk.Treeview(self, height=10, columns=("AppointmentID", "Appointment_details", "Status","Appointment_Date","CustomerID","PetID"), \
            yscrollcommand=scroll_y.set)

        #scroll_y.pack(side=RIGHT, fill=Y)
        #scroll_y.place(x=600,y=600)

        self.tree.heading("AppointmentID", text="Appointment ID")
        self.tree.heading("Appointment_details", text="Details")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Appointment_Date", text="Date")
        self.tree.heading("CustomerID", text="Customer ID")
        self.tree.heading("PetID", text="Pet ID")
        self.tree['show'] = 'headings'


        self.tree.column("AppointmentID", width=200)
        self.tree.column("Appointment_details", width=300)
        self.tree.column("Status", width=100)
        self.tree.column("Appointment_Date", width=100)
        self.tree.column("CustomerID", width=100)
        self.tree.column("PetID", width=10)

        self.tree.place(x=50,y=205,width=1195,height=560)




        def display1():
            self.tree.tag_configure('oddrow',background="white")
            self.tree.tag_configure('evenrow',background="silver")
            for i in self.tree.get_children():
                self.tree.delete(i)
            conn=sqlite3.connect('PSMS.db')
            cur=conn.cursor()
            cur.execute("SELECT * FROM user WHERE login = 'Online'")
            #cur.execute("SELECT * FROM Appointment WHERE username != '-' AND company_name != '-' ")
            item=cur.fetchall()
            for m in item:
                n = m[0]#NAME
                role = m[2]
                c_name = m[3]


            conn = sqlite3.connect("PSMS.db")
            cur= conn.cursor()
            cur.execute("PRAGMA foreign_keys = ON")
            cur.execute("SELECT * FROM History WHERE company_name = ?",(c_name,))
            conn.commit()
          
            rows = cur.fetchall()
            count=0
            for row in rows:
                if count % 2 == 0:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(row[0],row[1],row[2],row[3],row[4],row[5]), tags=('evenrow',))
                else:
                    self.tree.insert("", tk.END,iid=count,text=f'{count + 1}', values=(row[0],row[1],row[2],row[3],row[4],row[5]), tags=('oddrow',))
                count +=1
            conn.commit()
            conn.close()
        #display()

        def search():
            for i in self.tree.get_children():
                self.tree.delete(i)
            conn=sqlite3.connect('PSMS.db')
            cur=conn.cursor()
            cur.execute("SELECT * FROM Appointment WHERE username != '-' AND company_name != '-' ")
            item=cur.fetchall()
            for m in item:
                n = m[6]#NAME
                cur.execute("SELECT * FROM user WHERE username = ?",(n,))
                userrow = cur.fetchall()
                for k in userrow:
                    role = k[2]
                    if role == k[2]:#role
                        cur.execute("SELECT * FROM user WHERE role = ? AND username = ?",(role,n))
                        row = cur.fetchall()
                        for c in row:
                            c_name = c[3]

            search = self.SearchBar.get()
            conn=sqlite3.connect("PSMS.db")
            cur=conn.cursor()
            cur.execute("SELECT * FROM History WHERE company_name = ?",(c_name,))
            rows=cur.fetchall()
            
            for row in rows:
                if row[0].startswith(search) or row[1].startswith(search) or row[2].startswith(search) or row[3].startswith(search) or row[4].startswith(search):
                    self.tree.insert("", tk.END, values=(row[0],row[1],row[2],row[3],row[4],row[5]))

            conn.close()
        def clickevent1(event):
            for i in self.tree.get_children():
                self.tree.delete(i)

        title = tk.Label(self, text= "Pet Shop Management System", font=("Courier", 25), bg="white", bd=0, fg="grey23")
        title.place(x=250,y=80)

        pagetitle = tk.Label(self, text= "HISTORY", font=("Courier", 10, "bold"), bg="white", bd=0, fg="grey23")
        pagetitle.place(x=80,y=780)

        self.SearchBar = Entry(self, font=("Courier", 14), textvariable=SearchBar_Var, width=47,bg="snow",fg="grey23")
        self.SearchBar.place(x=250,y=170)
        self.SearchBar.insert(0,'Search here')

        self.btnsearch = tk.Button(self, image=self.btna, bd=0, bg="white",command=search)
        self.btnsearch.place(x=775,y=170)
        self.btnsearch.config(cursor= "hand2")
        
        self.btnrefresh = tk.Button(self, image=self.btnd, bd=0, bg="white",command=display1)
        self.btnrefresh.place(x=200,y=165)
        self.btnrefresh.config(cursor= "hand2")
        
        self.btnhom = tk.Button(self, image=self.btne, bd=0, bg="white",command=lambda: controller.show_frame(HomePage))
        self.btnhom.place(x=100,y=165)
        self.btnhom.config(cursor= "hand2")
        self.btnhom.bind("<Button-1>",clickevent1)


        self.btnappo = tk.Button(self, image=self.btng, bd=0, bg="white",command=lambda: controller.show_frame(AddPage))
        self.btnappo.place(x=155,y=167)
        self.btnappo.config(cursor= "hand2")        
        self.btnappo.bind("<Button-1>",clickevent1)
        
        #Button = tk.Button(self, text="Home", font=("Courier", 12, "bold"), bd=0, bg="white", fg="grey23", command= lambda: controller.show_frame(HomePage))
        #Button.place(x=450,y=90)
        #Button.bind("<Button-1>",clickevent1)
        #display1()
           
app = Application()
app.mainloop() 