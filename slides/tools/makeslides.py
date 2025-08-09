#!/usr/local/bin/python3

import subprocess, sys, os, shutil, glob

chap		  = str(sys.argv[1])
kind		  = str(sys.argv[2]).upper()
slidebase = open("slidebase.tex","r")
slide		  = open("slide.tex", "w")

if chap not in [ '00', '01', '02', '03', '04', '05', '06', '07', '08', '09' ]:
	print("Invalid chapter")
	os._exit(0)

if kind in ['S']:
	slide.write("\\documentclass[10pt,aspectratio=169,xcolor=dvipsnames]{beamer}\n")
elif kind in ['H','X']:
	slide.write("\\documentclass[10pt,handout,xcolor=dvipsnames]{beamer}\n")
else:
	print("Expected specification of slides (S) or handouts (H)")
	os._exit(0)

for line in slidebase:
	if line.startswith("%@@CHAP"):
		line = r'\renewcommand{\chap}{'+chap+'}'
	if line.startswith("%@@NOTES") and kind in ['X']:
		line = r'\renewcommand{\NotesFrame}{}'
	slide.write(line)
slide.close()

command = ["pdflatex", "-halt-on-error", "slide.tex"]
if not subprocess.call(command):
	subprocess.call(command)
else:
	print("Error occurred, bailing out...")
	os._exit(0)

if kind == 'S':
	outfilename = "slides."+chap+".pdf"
	shutil.copy("slide.pdf","slides/" + outfilename)
	shutil.copy("slide.pdf","slides.pdf")
else:
	if kind == 'H':
		outfilename = "notes."+chap+".pdf"
	else:
		outfilename = "handout."+chap+".pdf"
	command = ["tools/pdfnup", "--nup", "2x3", "--delta", "\"0cm 2cm\"", "--scale", "0.91", "--outfile", outfilename, "slide.pdf"]
	subprocess.call(command)
	shutil.move(outfilename,"slides/" + outfilename)

for f in glob.glob("slide.*"):
	os.remove(f)
