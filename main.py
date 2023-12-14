import os
import xml.etree.ElementTree as ET
from lxml import etree 

#out = ["PMC4356455.xml", "PMC5515033.xml","PMC5475329.xml","PMC5515018.xml","PMC5512763.xml","PMC5270587.xml","PMC5515025.xml","PMC5973265.xml",".DS_Store","PMC5791588.xml",
    #    "PMC5496061.xml","PMC4433911.xml","PMC4786848.xml","PMC5405378.xml","2PMC3809197.xml","PMC3507533.xml","PMC5515053.xml","PMC4316945.xml",
    #    "PMC5434249.xml","PMC5328349.xml","PMC4304213.xml","PMC4482215.xml"]

myPath = "/Users/elisacatena/Desktop/Ingegneria dei dati/Homework/hw 4/file hw4/"
filesName = os.listdir(myPath)
print(len(filesName))
print("\n")
cont=0
for file in filesName:
    cont+=1
    if file != ".DS_Store" and cont >10000:
        print(file)
        print("CONT:")
        
        print(cont)
        data = open(myPath+file).read()
        root = etree.fromstring(data)
        #for i in range(0,3):
        #print(filesName[i])
        #tree = ET.parse(myPath+"/"+file)
        #tree = ET.parse(myPath+"/"+filesName[i])s
        #root = tree.getroot()
        #PMCID
        print("PMCID: ")
        pmcid=root.find(".//article-id[@pub-id-type='pmc']")
        if pmcid is not None:
            print(pmcid.text)
        #title
        print("TITLE: ")
        title = (root.xpath(".//title-group/article-title//text()"))
        title_text = ""
        for i in range(0,len(title)):
            title_text = title_text + title[i]
        print(title_text)
        #abstract
        abstract = root.find(".//abstract//p")
        if abstract is not None:
            print("ABSTRACT: "+ET.tostring(abstract,encoding='unicode'))
        #keywords
        kwd_elements = root.xpath(".//kwd-group/kwd")
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
            
            text = root.find(".//xref[@ref-type='table'][@rid='"+table.attrib.get("id")+"']/..")
            if text is not None:
                print("TEXT: ")
                #print(str(text.text))
                stampa=ET.tostring(text,encoding='unicode',method='text')
                print(stampa)
            # text_tot = ""
            # for i in range(0,len(text)):
            #     text_tot = text_tot + text[i].text
            # print("TEXT: ")
            # print(text_tot)
            #paragraph citations
            #if len(text) > 0:
                allCit = text.xpath(".//xref[@ref-type='bibr']")
                for cit in allCit:
                    citID = cit.attrib.get("rid")
                    citation = root.find(".//ref[@id='"+citID+"']")
                    if citation is not None:
                        print("CITATIONS: "+ET.tostring(citation,encoding='unicode',method='text'))
        
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