# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:42:36 2018

@author: rjr
"""


# Creating a PDF writer
# FPDF Docs: https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html
from tkinter import *
from fpdf import FPDF
import uuid
import datetime
import os

# Types of letters: Invoice, Welcome to Service, Custom(Complete)

# All letters need to be dated, have a letterhead, have a greeting/salutation(Complete)

# Create a preview letter button so a user does not have to navigate to the PDF(Complete)

# Make it so that the button's don't dissappear(Complete)

# Place the buttons in different places(Complete)

# Create options for the letter type and if it will be email of physical(Complete)

# TODO: Make the dropdowns actually do something(Partially Complete) (Still need email )

# TODO: Send out stuff via an email client.

# TODO: Create the image/billing invoice(complete)

def retrieveInput(string=""):
    if string == "Standard":
        # Creating unique identifier for the letter for tracking/accounting
        # And setting up the datetime for the letter header
        uniqueLetterID = str(uuid.uuid4())
        dt = str(datetime.datetime.now().date())
        fileFormat = ".pdf"
        uniqueLetterFormat = uniqueLetterID + fileFormat
        
        global filename
        filename = uniqueLetterFormat
        # Creating the PDF
        pdf = FPDF()
        pdf.add_page()
        
        headers = ["Powerful Python", "A Python Productivity Blog", 
                   "555 Fake Street", "Wilmington, DE", "555-555-5555",
                   "PowerfulPython@fakeaddress.com"]
        
        
        # Header Section
        # This is more direct than the fpdf header/footer class, because
        # that class has to be overridden, this is more explict/readable
        # fpdf.cell(w, h = 0, txt = '', border = 0, ln = 0, align = '', fill = False, link = '')
        # fpdf.line(x1, y1, x2, y2)
        pdf.set_font("Arial", "B", 16)
        pdf.set_x(180)
        pdf.image("pythonLogo.png", w = 20, h = 25, type = "PNG")
        pdf.set_x(0)
        pdf.set_y(0)
        pdf.cell(40, 10, headers[0], 0, 2, "L")
        pdf.set_font("Arial", "", 16)
        
        
        pdf.cell(40, 10, headers[1], 0, 2, "L")
        pdf.cell(40, 10, headers[2], 0, 2, "L")
        pdf.cell(90, 10, headers[3], 0, 2, "L") 
        pdf.cell(100, 10, headers[4], 0, 2, "L")
        pdf.cell(40, 10, dt, 0, 2, "L")    
        pdf.line(10,70,190,70)
    
        # Main Body Section
        pdf.set_font("Arial", "", 16)
        inputValue = textArea.get("1.0", "end-1c")
        pdf.cell(40, 10, " ", 0, 2, "L")
        pdf.multi_cell(180, 10, inputValue)
        
        # Salutation/signoff
        pdf.set_y(250)
        pdf.cell(40, 5, "Regards,", 0, 2, "L")
        pdf.cell(40, 5, "The powerful Python Team", 0, 2, "L")
        
        # Footer Section
        pdf.line(10,270,190,270)
        
        # Output all of the above to PDF
        pdf.output(uniqueLetterFormat, "f")
        
        return uniqueLetterFormat
    else:
        # Creating unique identifier for the letter for tracking/accounting
        # And setting up the datetime for the letter header
        uniqueLetterID = str(uuid.uuid4())
        dt = str(datetime.datetime.now().date())
        fileFormat = ".pdf"
        uniqueLetterFormat = uniqueLetterID + fileFormat
        
        filename = uniqueLetterFormat
        # Creating the PDF
        pdf = FPDF()
        pdf.add_page()
        
        headers = ["Powerful Python", "A Python Productivity Blog", 
                   "555 Fake Street", "Wilmington, DE", "555-555-5555",
                   "PowerfulPython@fakeaddress.com"]
        
        
        # Header Section
        # This is more direct than the fpdf header/footer class, because
        # that class has to be overridden, this is more explict/readable
        # fpdf.cell(w, h = 0, txt = '', border = 0, ln = 0, align = '', fill = False, link = '')
        # fpdf.line(x1, y1, x2, y2)
        pdf.set_font("Arial", "B", 16)
        pdf.set_x(180)
        pdf.image("pythonLogo.png", w = 20, h = 25, type = "PNG")
        pdf.set_x(0)
        pdf.set_y(0)
        pdf.cell(40, 10, headers[0], 0, 2, "L")
        pdf.set_font("Arial", "", 16)
        # pdf.image(name, x = None, y = None, w = 0, h = 0, type = '', link = '')
        
        pdf.cell(40, 10, headers[1], 0, 2, "L")
        pdf.cell(40, 10, headers[2], 0, 2, "L")
        pdf.cell(90, 10, headers[3], 0, 2, "L") 
        pdf.cell(100, 10, headers[4], 0, 2, "L")
        pdf.cell(40, 10, dt, 0, 2, "L")    
        pdf.line(10,70,190,70)
    
        # Main Body Section
        pdf.image("BillingInvoice.jpg",x = 50, y = 80, w = 100, h = 140, type = "JPG")
        
        # Salutation/signoff
        pdf.set_y(250)
        pdf.cell(40, 5, "Regards,", 0, 2, "L")
        pdf.cell(40, 5, "The powerful Python Team", 0, 2, "L")
        
        # Footer Section
        pdf.line(10,270,190,270)
        
        # Output all of the above to PDF
        pdf.output(uniqueLetterFormat, "f")
        
        return uniqueLetterFormat
    
def previewLetter():
    path  = filename
    os.startfile(path)
    
def letterOrEmailDropdownMenu(*args):
    if letterOrEmail.get() == "Email":
        # Placeholder for now
        top = Toplevel()
        top.title("About this app...")
        msg = Message(top, text="Email")
        emailField = Entry(top)
        confirmEmailField = Entry(top)
        
        
        emailField.insert(END, "Enter Email")
        confirmEmailField.insert(END, "Confirm Email")
        
        emailField.pack()
        confirmEmailField.pack()
        msg.pack()
    else:
        # Placeholder for now
        top = Toplevel()
        top.title("Letter")
        msg = Message(top, text="Address Info")

        e = Entry(top)
        f = Entry(top)
        g = Entry(top)
        h = Entry(top)
        i = Entry(top)
        
        e.insert(END, "Address Field 1(Street address, P.O. Box, etc...")
        f.insert(END, "Address Field 2(APT #, etc...")
        g.insert(END, "City")
        h.insert(END, "State")
        i.insert(END, "ZIP")
        
        e.pack()
        f.pack()
        g.pack()
        h.pack()
        i.pack()
        msg.pack()
    
def letterFormatDropdownMenu(*args):
    if letterFormat.get() == "Billing Invoice":
        global billingInvoice
        billingInvoice = "Invoice"
        textArea.insert("1.0", """Billing invoice to be added/filled out upon preview""")
        retrieveInput("Invoice")
    elif letterFormat.get() == "Introduction":
        billingInvoice = "Standard"
        textArea.insert("1.0", """    On behalf of the entire Powerful Python staff, we'd like to take this opportunity to welcome you as a new customer. We are thrilled to have you with us.\n\n"""

"""    At Powerful Python, we pride ourselves on offering our customers responsive, competent and excellent service. Our customers are the most important part of our business, and we work tirelessly to ensure your complete satisfaction, now and for as long as you are a customer.\n\n"""

"""    Thank you again for entrusting Powerful Python with your most important business needs. We are honored to serve you.\n\n""")
    else:
        textArea.insert("1.0", """As this is a custom letter, fill it out as is appropriate""")
        billingInvoice = "Standard"
        
# Creating the general Tkinter window and text area
root = Tk()

root.minsize(20, 20)
title = root.title("Letter/Email Generation Tool")

textArea = Text(root, height=25, width=170)

# Letter or Email choice/dropdown menu
letterOrEmail = StringVar(root)
letterOrEmail.set("Make a selection(Letter/Email)") # default value
dropdown1 = OptionMenu(root, letterOrEmail, "Email", "Letter")
letterOrEmail.trace("w", letterOrEmailDropdownMenu)

# What type of letter will be sent out choice/dropdown menu
letterFormat = StringVar(root)
letterFormat.set("Make a selection(Letter format)") # default value
dropdown2 = OptionMenu(root, letterFormat, "Introduction", "Billing Invoice",
                       "Custom")
x = letterFormat.trace("w", letterFormatDropdownMenu)

# Preview letter button
previewButton = Button(root, height = 3, width = 10, text = "Preview", 
                       command = lambda: previewLetter())

copyButton = Button(root, height = 3, width = 10, text = "Generate letter/email",
                    command = lambda: retrieveInput(billingInvoice))
# Generating the buttons/window and sizing the window so that buttons 
# don't dissapear 
root.update()
dropdown1.pack(side="top", fill="both", expand=True, padx=2, pady=2)
dropdown2.pack(side="top", fill="both", expand=True, padx=2, pady=2)


textArea.pack()
copyButton.pack(side="bottom", fill="both", expand=True, padx=2, pady=2)
previewButton.pack(side="bottom", fill="both", expand=True, padx=2, pady=2)
root.geometry()
root.update()
root.geometry() 
root.minsize(root.winfo_width(), root.winfo_height())




root.mainloop()

"""
User Stories:
    
    1.  As a user I want to be able to copy/paste text that will be put
        into a letter.
    2.  As a user I want to be able to use a template that I just put in
        select information that will be put into a letter(name, address, etc).
    3.  As a user I want to be able to preview what the letter will look like
    4.  As a user I want to be able to be able to convert/send the letter as
        an email attachment.
    
"""


"""
Steps/Breakdown:
    
    Research:
        1.  What kind of GUI library will I use and why?
            Tkinter, because it doesn't cause crazy issues when I try to install it
            
        2.  What PDF library will I use and why?
            FPDF, because it's clear and straightforward 
            
        3.  Are there other solutions that I can look at that do something
            similar?
            
        4.  What should I use for an email? 
    
    Implementation:
        1.  How will I go about testing this 
        2.  What if any classes need to be made?
        3.  There should probably be a next/preview button
        
"""
