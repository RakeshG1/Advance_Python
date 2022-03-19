import os 
import xml.dom.minidom as xml # Works well for small documents

def xml_file_parse():
    filepath = os.getcwd()+"/Advance_Python/Sample_Data/Sample.xml"
    print("--"*30)
    print("XML File Parsing")
    print("--"*30)
    print("Filepath --> ", filepath, "\n")
    doc = xml.parse(filepath)
    print("doc.nodename --> ", doc.nodeName, "\n")
    print("doc.firstChild.tagName --> ", doc.firstChild.tagName, "\n")
    fname = doc.getElementsByTagName("fname")
    print("fname --> ", fname[0].firstChild.nodeValue, "\n")
    skills = doc.getElementsByTagName("skills")
    print("No. of skills : %d"% skills.length)
    print("Different Skills : ")
    print("--"*10)
    for skill in skills:
        print(skill.getAttribute("name"))
    programming_langs = doc.getElementsByTagName("Programming_Languages")
    for programming_lang in programming_langs:
        print("\n")
        print("No. of programming_langs : %d"% programming_lang.getElementsByTagName('language').length)
        print("Different Programming Languages : ")
        print("----"*10)             
        for child in programming_lang.getElementsByTagName('language'):
            print(child.getAttribute('name'))    

def xml_string():
    xml_data =  """<?xml version="1.0" encoding="UTF-8"?>
                    <employee>
                        <fname>Rakesh</fname>
                        <skills name="AI"></skills>
                        <Programming_Languages>
                            <language name="Python"></language>
                            <language name="R"></language>
                            <language name="SAS"></language>
                            <language name="SCALA"></language>
                            <language name="Julia"></language>
                            <language name="Java"></language>
                            <language name="SQL"></language>
                        </Programming_Languages>
                    </employee>
                """
    print("--"*30)
    print("XML String Parsing")
    print("--"*30)                
    xmldoc = xml.parseString(xml_data)
    parent = xmldoc.getElementsByTagName('employee')
    for item in parent:
        for child in item.getElementsByTagName('language'):
            print(child.getAttribute('name'))                

if __name__ == "__main__":
    #### Parsing XML File #####
    xml_file_parse()
    #### Parsing XML String #####
    xml_string()

'''
Output :
------------------------------------------------------------
XML File Parsing
------------------------------------------------------------
Filepath -->  /Users/rock/Git_Repo/Advance_Python/Sample_Data/Sample.xml 

doc.nodename -->  #document 

doc.firstChild.tagName -->  employee 

fname -->  Rakesh 

No. of skills : 1
Different Skills : 
--------------------
AI


No. of programming_langs : 7
Different Programming Languages : 
----------------------------------------
Python
R
SAS
SCALA
Julia
Java
SQL
------------------------------------------------------------
XML String Parsing
------------------------------------------------------------
Python
R
SAS
SCALA
Julia
Java
SQL
'''