import os
import xml.etree.ElementTree as ET
from lxml import etree 

class FindElement:

    def __init__(self,file):
        myPath = "/Users/elisacatena/Desktop/Ingegneria dei dati/Homework/hw 4/file hw4/"
        data = open(myPath+file).read()
        root = etree.fromstring(data)
        self.root=root

    def getPmcid(self):
        print("PMCID: ")
        pmcid = self.root.find(".//article-id[@pub-id-type='pmc']")
        print(pmcid.text)
        return pmcid
    
    def getTitle(self):
        print("TITLE: ")
        title = (self.root.xpath(".//title-group/article-title//text()"))
        title_text = ""
        for i in range(0,len(title)):
            title_text = title_text + title[i]
        print(title_text)
        return title_text
    
    def getAbstract(self):
        abstract = self.root.find(".//abstract//p")
        if abstract is not None:
            print("ABSTRACT: "+ET.tostring(abstract,encoding='unicode'))
        else:
            print('')
        return abstract
    
    def getKeywords(self):
        kwd_elements = self.root.xpath(".//kwd-group/kwd")
        kwd_list = []
        for kwd_element in kwd_elements:
            content = etree.tostring(kwd_element, method="text", encoding=str)
            kwd_list.append(content)
            print("KEYWORDS: " + content)
        return kwd_list
    
    def getTables(self):
        return self.root.findall(".//table-wrap")
    
    def getTableID(self,table):
        tableID = table.attrib.get("id")
        print("TABLE ID: "+tableID)
        return tableID
    
    def getTableCaption(self,tableID):
        caption = self.root.find(".//table-wrap[@id='"+tableID+"']//caption//*")
        if caption is not None:
            print("CAPTION: "+caption.text)
        return caption
    
    def getTablesFoot(self,tableID):
        feet_list = []
        feet = self.root.findall(".//table-wrap[@id='"+tableID+"']//table-wrap-foot//p")
        for foot in feet:
            feet_list.append(ET.tostring(foot,encoding='unicode'))
            print("FOOT: "+ET.tostring(foot,encoding='unicode'))
        return feet_list
    

    def getTableHead(self, tableID):
        tableHead = self.root.find(".//table-wrap[@id='"+tableID+"']//table//thead")
        if tableHead is not None:
            print("TABLE HEAD: "+ET.tostring(tableHead,encoding='unicode'))
        return tableHead
    
    def getTableBody(self, tableID):
        tableBody = self.root.find(".//table-wrap[@id='"+tableID+"']//table//tbody")
        if tableBody is not None:
            print("TABLE HEAD: "+ET.tostring(tableBody,encoding='unicode'))
        return tableBody
    
    def getParagraphText(self, tableID):
        text = self.root.xpath(".//xref[@ref-type='table' and @rid='"+tableID+"']/..")
        for element in text:
            for comment in element.xpath('.//comment()'):
                comment.getparent().remove(comment)
        print("TEXT: ")
        for i in range(0,len(text)):
            print(ET.tostring(text[i],encoding='utf-8').decode('utf-8'))
            print("LEN TEXT: ", len(text))
        return text
    
    def getParagraphCitations(self, p):
        allCit = p.findall(".//xref[@ref-type='bibr']")
        cit_list = []
        for cit in allCit:
            citID = cit.attrib.get("rid")
            citation = self.root.find(".//ref[@id='"+citID+"']")
            if citation is not None:
                cit_list.append(ET.tostring(citation,encoding='utf-8').decode('utf-8'))
                print("CITATIONS: "+ET.tostring(citation,encoding='utf-8').decode('utf-8'))
        return cit_list
    



    def getFigures(self):
        fig_list = self.root.findall(".//fig")
        return fig_list
    
    def getFigureID(self, fig):
        figID = fig.attrib.get("id")
        print("FIGURE ID: "+figID)
        return figID
    
    def getFigureCaption(self,figID):
        figCaption = self.root.find(".//fig[@id='"+figID+"']//caption//*")
        if figCaption is not None:
            print("CAPTION: "+ET.tostring(figCaption,encoding='unicode'))
        return figCaption











    

    

    