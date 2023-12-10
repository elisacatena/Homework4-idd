import os
import xml.etree.ElementTree as ET

myPath = "/Users/elisacatena/Desktop/Ingegneria dei dati/Homework/hw 4/file hw4"
filesName = os.listdir(myPath)
print(len(filesName))
print("\n")
for i in range(0,5):
    print(filesName[i])
    #fileXML = open(myPath+"/"+filesName[i],"r")
    #print(fileXML.read())
    tree = ET.parse(myPath+"/"+filesName[i])
    root = tree.getroot()
    #PMCID
    print("PMCID: "+root.find(".//article-id[@pub-id-type='pmc']").text)
    #title
    print("TITLE: "+root.find(".//title-group/article-title").text)
    #abstract
    abstract = root.find(".//abstract//p")
    print("ABSTRACT: "+ET.tostring(abstract,encoding='unicode'))
    #keywords
    for keyword in root.findall(".//kwd-group//kwd"):
        print("KEYWORDS: "+keyword.text)
    #tables
    for table in root.findall(".//table-wrap"):
        #table ID
        print("TABLE ID: "+table.attrib.get("id"))
        #caption
        caption = root.find(".//table-wrap[@id='"+table.attrib.get("id")+"']//caption//p")
        print("CAPTION: "+ET.tostring(caption,encoding='unicode'))
        #foot
        feet = root.findall(".//table-wrap[@id='"+table.attrib.get("id")+"']//table-wrap-foot//p")
        for foot in feet:
            print("FOOT: "+ET.tostring(foot,encoding='unicode'))
        #caption_citation

        #body
        tableHead = root.find(".//table-wrap[@id='"+table.attrib.get("id")+"']//table//thead")
        tableBody = root.find(".//table-wrap[@id='"+table.attrib.get("id")+"']//table//tbody")
        print("TABLE HEAD: "+ET.tostring(tableHead,encoding='unicode'))
        print("TABLE BODY: "+ET.tostring(tableBody,encoding='unicode'))
        #paragraph text
        #print("TEXT: "+root.find(".//xref[@ref-type='table',@rid='"+table.attrib.get("id")+"']/..").text)
        text = root.find(".//xref[@ref-type='table'][@rid='"+table.attrib.get("id")+"']/..")
        print("TEXT: "+ET.tostring(text,encoding='unicode'))
        #paragraph citations
        allCit = text.findall(".//xref[@ref-type='bibr']")
        for cit in allCit:
            citID = cit.attrib.get("rid")
            citation = root.find(".//ref[@id='"+citID+"']")
            print("CITATIONS: "+ET.tostring(citation,encoding='unicode'))


    
    print("\n")