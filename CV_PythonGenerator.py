#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 15:45:06 2022

@author: Robert_Hennings
"""
import datetime as dt
import pandas as pd
from PIL import Image 

# Define the displayed text variables
Header = 'This resume was generated entirely in Python. See Github for Code.'
Name = 'Robert Hennings'
Title = 'Data Science & Analytics'
Contact = 'hennings.robert@web.de | +49-1757367903 | Renzer Str. 5, 24211 Preetz SH Germany\nGithub: github.com/RobertHennings | LinkedIn: linkedin.com/in/robert-hennings'

# Define the Main section titles of the CV
Section1_Title = "Education"
Section2_Title = "Professional Experience"
Section3_Title = "Skills"
Section4_Title = "Projects & Leadership"
Section5_Title = "Additional Information"

# Define the single positions - Section 1: Education
Education1_Title = "Christian-Albrechts-University of Kiel"
Position1_Title = "Master of Science: Quantitative Finance"

Education2_Title = "University Duisburg-Essen, Campus Essen"
Position2_Title = "Bachelor of Science: Business Administration, Energy and Finance"
Position2_Grade = "2,1 (GPA: ~3,0)"
Position2_Thesis = "Thesis: Is liquidity risk still priced in the cross-section of US stocks? (R, Python based) Grade: 1,3 (GPA: 3,7, see Github)"
Position2_RelevantCourses = "Relevant Courses: Investment and Finance, Asset Management, Introduction to Derivatives, Descriptive Statistics, Statistical\n\t\t\t\t\t\t\t\t\t\t\tInference, Business Statistics, Introduction to Econometrics, Database Management Systems, Statistics and Computing"
                             


# Define the single positions - Section 2: Professional Experience
# Position 1
Position1_Company = "Vattenfall Energy Trading GmbH"
Position1_Job = "Working Student Data Science in the Trading Analysis & Algorithms Unit"
Position1_Details1 = "• Identifying, reviewing, and integrating (new) information and sources/feeds for market or fundamental data, e.g., \nbuilding web scrapers or data quality monitoring tools, further developing and automating routines/ applications for analysis-related data flows"
Position1_Details2 = "• Further developing the fundamental and mathematical market modelling, incl. utilizing machine learning approaches"

# Position 2
Position2_Company = "Deutsche Börse Group, EUREX Frankfurt AG"
Position2_Job = "Internship Fixed Income Analysis/ ETD Product Design"
Position2_Details1 = "• Assist in the delivery of new derivatives protypes, actively support project management tasks by providing analysis for positioning"
Position2_Details2 = "• Conduct competition and a multitude of in-depth market analysis using SQL and Python to collect market data from Eurex T7\nSystem and the Bloomberg-Terminal"
Position2_Details3 = "• Creation of an algorithms and backtesting library for Product Use cases, writing a research paper about Trading Volume forecasting"
Position2_Details4 = "• Insights into back-testing of new derivatives prototypes and build models/analytics from large and varied data sets"

# Position 3
Position3_Company = "Deutsche Bundesbank"
Position3_Job = "Internship in the Market Intelligence and Analysis Unit"
Position3_Details1 = "• Support in the programming of analytical tools for the pricing of securities using Python and Bloomberg"
Position3_Details2 = "• Actively participate in the development of an analysis solution tailored to the needs of collateral valuation"
Position3_Details3 = "• Insights into current issues of pricing and establishing dashboards with Tableau, xlwings, OpenpyXl, pptx"

# Position 4
Position4_Company = "Statista GmbH"
Position4_Job = "Working student Data Analytics at Statista Q (Data Science branch of Statista)"
Position4_Details1 = "• Independent Data research on various topics in combination with data preparation and cleaning"
Position4_Details2 = "• Carrying out descriptive analyses and preparation of results in common presentation formats using Python, R"

# Define the single positions - Section 3: Skills

Skill1 = "Programming Languages: Python, R, SQL, Basic knowledge in: Java, JavaScript, HTML, CSS"
Skill2 = "Big Data & Machine Learning: Python (Scikit-learn, Numpy, SciPy, Pandas, Matplotlib, Seaborn, SHAP, xlwings, pptx, glob)"
Skill3 = "Additional: Financial databases (Bloomberg-Terminal, Refinitiv Reuters and S&P Capital IQ), Tableau, SAP SRM, SPSS"

# Define the single positions - Section 4: Projects & Leadership
Position1_Lead = "Volunteer European Championships: Volunteer Management (August 2022)"
Position2_Lead = "Volunteer Special Olympics Kiel: Swimming Team athlete support (June 2022)"
Position3_Lead = "Vice Chairman of the Board"
Position3_Lead_Company = "Academic Stock Association Bochum eV (ABBeV)"
Position3_Lead_Details1 = "• Administrative activities including initialization /holding of lectures and new formats on quantitative finance topics (see Github)"
Position3_Lead_Details2 = "• Promoting discourse on developments in capital and technology markets"

# Define the single positions - Section 4: Additional Information

Info1 = "Bertelsmann Technology scholarship Udacity: Artificial Intelligence 2020, Business Analytics 2022"
Info2 = "E-Fellows.net career network scholarship"
Info3 = "Languages: German (native), English, French (basic knowledge)"
Info4 = "Interests: competitive sports athletics, powerlifting, kiteboarding/wakeboarding, road cycling, archery, reading (math, physiscs)"


# Drawing the CV plot and placing the elements
# Setting style for bar graphs
import matplotlib.pyplot as plt
#%matplotlib inline
# set font
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'
fig, ax = plt.subplots(figsize=(8.5, 11))
# Decorative Lines
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

image = plt.imread('/Users/Robert_Hennings/Dokumente/Uni/MusterBewerbung/Meine Unterlagen/Bewerbungsfotos/BWF.png') 
ax.add_artist(AnnotationBbox(OffsetImage(image,zoom=0.14),(0.87,0.98),frameon=True))
#plt.axhline(y=.88, xmin=0, xmax=1, color='black', linewidth=1.8)
#plt.axvline(x=0.98,ymin=0,ymax=1, color = "black", linewidth = 0.8)
# set background color
ax.set_facecolor('white')
# remove axes
plt.axis('off')
# add text


# Add general Information
plt.annotate(Header, (.32,.99), weight='regular', fontsize=6, alpha=.60)
plt.annotate(Name, (.39,.96), weight='bold', fontsize=14)
plt.annotate(Contact, (.27,.93), weight='regular', fontsize=6)

# Add Section 1: Eduaction
plt.annotate(Section1_Title, (.02,.90), weight='heavy', fontsize=10, color='black') # size 10 
# Add line
plt.axhline(y=.897, xmin=0.02, xmax=0.98, color='black', linewidth=1.3)
# Current Degree
plt.annotate(Education1_Title, (.02,.88), weight='bold', fontsize=8) # 7 fett
plt.annotate("Kiel", (.955,.88), weight='regular', fontsize=8) # 7 fett
#plt.annotate(Position1_Title, (.02,.866), weight='regular', fontsize=8) # 7 kursiv
plt.text(.02,.866,Position1_Title,fontsize = 8, style = "italic")
plt.annotate("10/2021 - today", (.864,.866), weight='regular', fontsize=8) 
#plt.text(.02,.87,"Text", fontstyle = "italic",fontsize=7)
# Previous Degree
plt.annotate(Education2_Title, (.02,.84), weight='bold', fontsize=8) # 7 fett
plt.annotate("Essen", (.945,.84), weight='regular', fontsize=8) # 7 fett
#plt.annotate(Position2_Title, (.02,.826), weight='regular', fontsize=8) # 7 kursiv
plt.text(.02,.826,Position2_Title,fontsize = 8, style = "italic")
plt.annotate("10/2018 - 10/2021", (.845,.826), weight='regular', fontsize=8) # 7 kursiv
plt.annotate(Position2_Grade, (.02,.811), weight='regular', fontsize=8) # 7 normal
plt.annotate(Position2_Thesis, (.02,.797), weight='regular', fontsize=8) # 7 normal
plt.annotate(Position2_RelevantCourses, (.02,.768), weight='regular', fontsize=8) # 7 normal

# Add Section 2: Professional Experience
plt.annotate(Section2_Title, (.02,.738), weight='heavy', fontsize=10, color='black') # size 10 
# Add line
plt.axhline(y=.735, xmin=0.02, xmax=0.98, color='black', linewidth=1.3)
# Position 1
plt.annotate(Position1_Company, (.02,.718), weight='bold', fontsize=8)  # 7 fett
plt.annotate("Hamburg", (0.913,.718), weight='regular', fontsize=8)# 

plt.text(.02,.704,Position1_Job, style='italic', fontsize=8)#
#plt.annotate(Position1_Job, (.02,.704), weight='regular', fontsize=8)# 7 kursiv
plt.annotate("12/2022 - today", (0.875,.704), weight='regular', fontsize=8)# 
plt.annotate(Position1_Details1, (.02,.675), weight='regular', fontsize=8) # 7 normal
plt.annotate(Position1_Details2, (.02,.661), weight='regular', fontsize=8) # 7 normal
# Position 2
plt.annotate(Position2_Company, (.02,.638), weight='bold', fontsize=8)  # 7 fett
plt.annotate("Frankfurt am Main", (0.845,.638), weight='regular', fontsize=8)# 
#plt.annotate(Position2_Job, (.02,.624), weight='regular', fontsize=8)# 7 kursiv
plt.text(.02,.624,Position2_Job, style='italic', fontsize=8)#
plt.annotate("07/2022 - 11/2022", (0.845,.624), weight='regular', fontsize=8)# 
plt.annotate(Position2_Details1, (.02,.61), weight='regular', fontsize=8) # 7 normal
plt.annotate(Position2_Details2, (.02,.582), weight='regular', fontsize=8) # 7 normal
plt.annotate(Position2_Details3, (.02,.568), weight='regular', fontsize=8) # 7 normal
plt.annotate(Position2_Details4, (.02,.553), weight='regular', fontsize=8) # 7 normal
# Position 3
plt.annotate(Position3_Company, (.02,.53), weight='bold', fontsize=8)  # 7 fett
plt.annotate("Frankfurt am Main", (0.845,.53), weight='regular', fontsize=8)# 
#plt.annotate(Position3_Job, (.02,.516), weight='regular', fontsize=8)# 7 kursiv
plt.text(.02,.516,Position3_Job, style='italic', fontsize=8)#
plt.annotate("02/2022 - 05/2022", (0.845,.516), weight='regular', fontsize=8)# 
plt.annotate(Position3_Details1, (.02,.502), weight='regular', fontsize=8) # 7 normal
plt.annotate(Position3_Details2, (.02,.488), weight='regular', fontsize=8) # 7 normal
plt.annotate(Position3_Details3, (.02,.474), weight='regular', fontsize=8) # 7 normal
# Position 4
plt.annotate(Position4_Company, (.02,.45), weight='bold', fontsize=8)  # 7 fett
plt.annotate("Hamburg", (0.913,.45), weight='regular', fontsize=8)# 
#plt.annotate(Position4_Job, (.02,.436), weight='regular', fontsize=8)# 7 kursiv
plt.text(.02,.436,Position4_Job, style='italic', fontsize=8)#
plt.annotate("11/2021 - today", (0.864,.436), weight='regular', fontsize=8)# 
plt.annotate(Position4_Details1, (.02,.422), weight='regular', fontsize=8) # 7 normal
plt.annotate(Position4_Details2, (.02,.408), weight='regular', fontsize=8) # 7 normal

# Add Section 3: Skills
plt.annotate(Section3_Title, (.02,.382), weight='heavy', fontsize=10, color='black') # size 10 
# Add line
plt.axhline(y=.379, xmin=0.02, xmax=0.98, color='black', linewidth=1.3)
# Skill 1
plt.annotate(Skill1, (.02,.365), weight='regular', fontsize=8) # 7 normal
# Skill 2
plt.annotate(Skill2, (.02,.351), weight='regular', fontsize=8) # 7 normal
# Skill 3
plt.annotate(Skill3, (.02,.336), weight='regular', fontsize=8) # 7 normal

# Add Section 4: Projects & Leadership
plt.annotate(Section4_Title, (.02,.317), weight='heavy', fontsize=10, color='black') # size 10 
# Add line
plt.axhline(y=.313, xmin=0.02, xmax=0.98, color='black', linewidth=1.3)

plt.annotate(Position1_Lead, (.02,.294), weight='regular', fontsize=8) # 7 normal
plt.annotate("Munich", (0.928,.294), weight='regular', fontsize=8)# 
plt.annotate(Position2_Lead, (.02,.281), weight='regular', fontsize=8) # 7 normal
plt.annotate("Kiel", (0.955,.281), weight='regular', fontsize=8)# 
plt.annotate(Position3_Lead, (.02,.268), weight='regular', fontsize=8) # 7 normal
plt.annotate("Essen/Bochum", (0.869,.268), weight='regular', fontsize=8)# 

#plt.annotate(Position3_Lead_Company , (.02,.254), weight='regular', fontsize=8) # 7 normal
plt.text(.02,.254,Position3_Lead_Company, style='italic', fontsize=8)#
plt.annotate("11/2020 - today", (0.864,.254), weight='regular', fontsize=8)# 
plt.annotate(Position3_Lead_Details1  , (.02,.24), weight='regular', fontsize=8) # 7 normal
plt.annotate(Position3_Lead_Details2  , (.02,.225), weight='regular', fontsize=8) # 7 normal

# Add Section 5: Additional Information
plt.annotate(Section5_Title, (.02,.208), weight='heavy', fontsize=10, color='black') # size 10 
# Add line
plt.axhline(y=.205, xmin=0.02, xmax=0.98, color='black', linewidth=1.3)
plt.annotate(Info1, (.02,.19), weight='regular', fontsize=8) # 7 normal
plt.annotate(Info2, (.02,.176), weight='regular', fontsize=8) # 7 normal
plt.annotate(Info3, (.02,.161), weight='regular', fontsize=8) # 7 normal
plt.annotate(Info4, (.02,.147), weight='regular', fontsize=8) # 7 normal


plt.savefig('/Users/Robert_Hennings/Downloads/CV_PythonGenerated_{}.png'.format(dt.datetime.strftime(dt.datetime.today(),format = "%Y-%M-%d")), dpi=600, bbox_inches='tight')

cv_image = Image.open('/Users/Robert_Hennings/Downloads/CV_PythonGenerated_{}.png'.format(dt.datetime.strftime(dt.datetime.today(),format = "%Y-%M-%d")))
cv = cv_image.convert('RGB')
cv.save('/Users/Robert_Hennings/Downloads/CV_PythonGenerated_{}.pdf'.format(dt.datetime.strftime(dt.datetime.today(),format = "%Y-%M-%d")))
 
#[ 'normal' | 'bold' | 'heavy' | 'light' | 'ultrabold' | 'ultralight']
# dir(ax)
# To do: find optimal spacing of elements on the figure element, place photo in the upper right corner, text formatting 
# ax.get_xlim()
# ax.get_ylim()




