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

# Types of letters: Invoice, Welcome to Service, Disconnection of Service

# All letters need to be dated, have a letterhead, have a greeting/salutation.

# Create a preview letter button so a user does not have to navigate to the PDF

# What if a user wants to create a new letter/email?


def retrieveInput():
    
    # Creating unique identifier for the letter for tracking/accounting
    # And setting up the datetime for the letter header
    uniqueLetterID = str(uuid.uuid4())
    dt = str(datetime.datetime.now().date())
    fileFormat = ".pdf"
    uniqueLetterFormat = uniqueLetterID + fileFormat
    
    
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
    pdf.set_y(245)
    pdf.cell(40, 5, "Regards,", 0, 2, "L")
    pdf.cell(40, 5, "The powerful Python Team", 0, 2, "L")
    
    # Footer Section
    pdf.line(10,270,190,270)
    
    # Output all of the above to PDF
    pdf.output(uniqueLetterFormat, "f")
    
    
def previewLetter(fileName):
    pass


# Creating the general Tkinter window and text area
root = Tk()
title = root.title("Letter/Email Generation Tool")
textArea = Text(root, height=25, width=50)
textArea.pack()
userButton = Button(root, height = 3, width = 10, text = "Copy to letter",
                    command = lambda: retrieveInput())

# Letter or Email choice
letterOrEmail = StringVar(root)
letterOrEmail.set("one") # default value
dropdown1 = OptionMenu(root, letterOrEmail, "Email", "Letter")


# What type of letter will be sent out choice
letterFormat = StringVar(root)
letterFormat.set("one") # default value
dropdown2 = OptionMenu(root, letterFormat, "Introduction", "Billing Invoice",
                       "Custom")

# Generating the buttons/window
dropdown1.pack()
dropdown2.pack()
userButton.pack()
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
