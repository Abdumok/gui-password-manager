import random
import string
from tkinter import *

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

        #Display the generated password in the password field:
        password_input.insert(index=0, string=password)

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
add_button= Button(width= 43, text= "Add")
add_button.place(x= 156, y=289)
search_button= Button(width=15, text="Search")
search_button.place(x= 350, y= 197)

window.mainloop()