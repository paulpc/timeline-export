# |======================================================|
# | (C) Devon Energy Corporation                         |
# | Paul PC - paul.poputa-clean@dvn.com                  |
# | Distributed under the Apache License (i think        |
# | Script to output the timeline as a colorful xls file |
# |======================================================|

from lxml import etree
from lxml.builder import E
import csv
# reads te timeline from a CSV file. Temporary method until we can merge it with plaso and output the xls from the object in memory.
def read_from_csv(filename):
    timeline=[]
    with open(filename,'rb') as csvfile:
        headers=[]
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if (len(headers) == 0):
                headers = row
            else:
                elements={}
                for i, element in enumerate(row):
                    elements[headers[i]]=element
                timeline.append(elements)
    return timeline

# checks the row for color depending on the values in each column
def check_colors():
    print "I am useless method"

# loads the conditions for the color template
def load_conditions():
    
    print "I am useless method"

def CLASS(*args): # class is a reserved word in Python
    return {"class":' '.join(args)}

# exports the timeline as an html file
def export_html(timeline,file,columns):
    html= page = (
        E.html(
            E.head(
                E.title("Timeline as HTML output")
            ),         
        )
    )
    print(etree.tostring(page, pretty_print=True))
    bdy=etree.SubElement(page,"body")
    tbl=etree.SubElement(bdy,"table")
    tbl.set("border","1")
    tbl_thead=etree.SubElement(tbl,"thead")
    tbl_h=etree.SubElement(tbl_thead,"tr")
    for tlk in columns:
        tbl_td=etree.SubElement(tbl_h,"td")
        tbl_td.text=tlk
    tbl_tbody=etree.SubElement(tbl,"tbody")  
    for row in timeline:
        tbl_tr=etree.SubElement(tbl_tbody,"tr")
        for col in columns:
            tbl_td=etree.SubElement(tbl_tr,"td")
            tbl_td.text=row[col]
            
    f=open(file,'w')
    f.write(etree.tostring(page, pretty_print=True))
    f.close()

timeline=read_from_csv('test_timeline.csv')
print timeline
export_html(timeline,"test.html",["date","time","short"])
