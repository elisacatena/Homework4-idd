import os
import xml.etree.ElementTree as ET
from lxml import etree 

myPath = "/Users/elisacatena/Desktop/Ingegneria dei dati/Homework/hw 4/file hw4"
filesName = os.listdir(myPath)
print(len(filesName))
print("\n")
for file in filesName:
    prova = open(myPath+"/"+file)
    data = prova.read()
    root1 = etree.fromstring(data)
    print(file)
    #for i in range(0,3):
    #print(filesName[i])
    tree = ET.parse(myPath+"/"+file)
    #tree = ET.parse(myPath+"/"+filesName[i])
    root = tree.getroot()
    #PMCID
    print("PMCID: "+root.find(".//article-id[@pub-id-type='pmc']").text)
    #title
    print("TITLE: "+root.find(".//title-group/article-title").text)
    #abstract
    abstract = root.find(".//abstract//p")
    if abstract is not None:
        print("ABSTRACT: "+ET.tostring(abstract,encoding='unicode'))
    #keywords
    kwd_elements = root1.xpath(".//kwd-group/kwd")
    for kwd_element in kwd_elements:
        content = etree.tostring(kwd_element, method="text", encoding=str)
        print("KEYWORDS: " + content)
    #tables
    for table in root.findall(".//table-wrap"):
        #table ID
        print("TABLE ID: "+table.attrib.get("id"))
        #caption
        caption = root.find(".//table-wrap[@id='"+table.attrib.get("id")+"']//caption//*")
        if caption is not None:
            print("CAPTION: "+ET.tostring(caption,encoding='unicode'))
        #foot
        feet = root.findall(".//table-wrap[@id='"+table.attrib.get("id")+"']//table-wrap-foot//p")
        for foot in feet:
            print("FOOT: "+ET.tostring(foot,encoding='unicode'))
        #caption_citation


        #body
        tableHead = root.find(".//table-wrap[@id='"+table.attrib.get("id")+"']//table//thead")
        tableBody = root.find(".//table-wrap[@id='"+table.attrib.get("id")+"']//table//tbody")
        if tableHead is not None:
            print("TABLE HEAD: "+ET.tostring(tableHead,encoding='unicode'))
        if tableBody is not None:
            print("TABLE BODY: "+ET.tostring(tableBody,encoding='unicode'))
        #paragraph text
        #print("TEXT: "+root.find(".//xref[@ref-type='table',@rid='"+table.attrib.get("id")+"']/..").text)
        text = root.find(".//xref[@ref-type='table'][@rid='"+table.attrib.get("id")+"']/..")
        if text is not None:
            print("TEXT: "+ET.tostring(text,encoding='unicode'))
            #paragraph citations
            allCit = text.findall(".//xref[@ref-type='bibr']")
            for cit in allCit:
                citID = cit.attrib.get("rid")
                citation = root.find(".//ref[@id='"+citID+"']")
                if citation is not None:
                    print("CITATIONS: "+ET.tostring(citation,encoding='unicode'))
        
        #cells



    #figure
    for fig in root.findall(".//fig"):
        #fig ID
        print("FIGURE ID: "+fig.attrib.get("id"))
        #caption
        figCaption = root.find(".//fig[@id='"+fig.attrib.get("id")+"']//caption//*")
        if figCaption is not None:
            print("CAPTION: "+ET.tostring(figCaption,encoding='unicode'))
        #source
        #print(root.find(".//fig[@id='"+fig.attrib.get("id")+"']//graphic/*"))
        #print(root.find('.//graphic').attrib.get('xlink:href', None))
    


    print("\n")