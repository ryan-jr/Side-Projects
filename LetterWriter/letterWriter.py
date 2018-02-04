# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 11:42:36 2018

@author: rjr
"""

# Creating a PDF writer

from tkinter import *
from fpdf import FPDF

root = Tk()
title = root.title("Welcome!")
textArea = Text(root, height=100, width=80)
textArea.pack()
quote = " lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum "
textArea.insert(END, quote)
root.mainloop()


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(40, 10, quote)
pdf.output("firstTry.pdf", "f")
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
