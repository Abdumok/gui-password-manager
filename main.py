import json
import random
import string
from tkinter import *
from tkinter import messagebox

from click import confirm

# setup main screen
window= Tk()
window.title("Password Manager")
window.minsize(width=600, height=400)
window.config(padx=20, pady=20)
#=========================================== Functions ================================================================
def generate_password():
        letters= [random.choice(string.ascii_letters) for _ in range(random.randint(6, 8))]
        numbers= [random.choice(string.digits) for _ in range(random.randint(2, 4))]
        symbols= [random.choice(string.punctuation) for _ in range(random.randint(2, 4))]

        password_list= letters + numbers + symbols
        random.shuffle(password_list)
        password= "".join(password_list)

        # Clear the password field before generate new one:
        password_input.delete(first=0, last=END)

        #Display the generated password in the password field:
        password_input.insert(index=0, string=password)


def save_data():
        website= website_input.get()
        email= email_input.get()
        password= password_input.get()

        new_data= {
                website : {
                        "email": email,
                        "password": password,
                }
        }
        # check for empty field:
        if len(website) == 0 or len(email) == 0 or len(password) == 0:
                messagebox.showerror(title="Empty Field", message="You let one or more field empty")
        else:
                is_ok= messagebox.askokcancel(title=f"{website}", message=f"These are the details entered: "
                        f"\n\nEmail: {email} \n\nPassword: {password} \n\n Are you sure want to save that")
                if is_ok:
                        # if the data file is already created
                        try:
                                with open ("data_file.json", mode="r") as file:
                                        data= json.load(file)
                        # if the data file not exist(lunch the program for first time)
                        except FileNotFoundError:
                                with open("data_file.json", mode="w") as my_file:
                                        json.dump(obj=new_data, fp=my_file, indent=4) # use indent property to justify json data
                        else:
                                data.update(new_data)
                                with open("data_file.json", mode="w") as myfile:
                                        json.dump(obj= data, fp=myfile, indent=4)
                        finally:
                                # clear website and password field
                                website_input.delete(0, END)
                                password_input.delete(0, END)

#======================================================================================================================
canvas= Canvas(width=200, height=200)
img=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.place(x=180, y=0)

#=========================================== Labels ===================================================================
website_text = Label(text="Website: ", font=("Times New Roman", 10, "bold"))
website_text.place(x= 95, y= 200)
email_text= Label(text= "Email/Username: ", font=("Times New Roman", 10, "bold"))
email_text.place(x= 50, y= 230)
password_text= Label(text= "Password: ", font=("Times New Roman", 10, "bold"))
password_text.place(x= 87, y= 260)

#========================================== Entry ====================================================================
website_input= Entry(width=30)
website_input.place(x= 160, y= 200)
email_input= Entry(width=50)
email_input.place(x= 160, y= 230)
password_input= Entry(width=27)
password_input.place(x= 160, y=260)

#========================================== Button ===================================================================
gen_password_button= Button(width=18, text= "Generate Password", command= generate_password)
gen_password_button.place(x=329, y= 258)
add_button= Button(width= 43, text= "Add", command=save_data)
add_button.place(x= 156, y=289)
search_button= Button(width=15, text="Search")
search_button.place(x= 350, y= 197)

window.mainloop()