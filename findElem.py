import xml.etree.ElementTree as ET
from lxml import etree 
import elementpath

class FindElement:

    def __init__(self,file):
        myPath = "/Users/elisacatena/Desktop/Ingegneria dei dati/Homework/hw 4/file hw4/"
        data = open(myPath+file).read()
        root = etree.fromstring(data)
        for element in root:
            for comment in element.xpath('.//comment()'):
                comment.getparent().remove(comment)
        self.root=root

    def getPmcid(self):
        #print("PMCID: ")
        pmcid = self.root.find(".//article-id[@pub-id-type='pmc']")
        #if pmcid is not None:
            #print(pmcid.text)
        return pmcid
    
    def getTitle(self):
        #print("TITLE: ")
        title = (self.root.xpath(".//title-group/article-title//text()"))
        title_text = ""
        for i in range(0,len(title)):
            title_text = title_text + title[i]
        #print(title_text)
        return title_text
    
    def getAbstract(self):
        abstract = self.root.find(".//abstract//p")
        # if abstract is not None:
        #     print("ABSTRACT: "+ET.tostring(abstract,encoding='unicode'))
        # else:
        #     print('')
        return abstract
    
    def getKeywords(self):
        kwd_elements = self.root.xpath(".//kwd-group/kwd")
        kwd_list = []
        for kwd_element in kwd_elements:
            content = etree.tostring(kwd_element, method="text", encoding=str)
            kwd_list.append(content)
            #print("KEYWORDS: " + content)
        return kwd_list
    
    def getTables(self):
        return self.root.findall(".//table-wrap")
    
    def getTableID(self,table):
        tableID = table.attrib.get("id")
        #if tableID is not None:
            #print("TABLE ID: "+tableID)
        return tableID
    
    def getTableCaption(self,tableID):
        caption = self.root.find(".//table-wrap[@id='"+tableID+"']//caption/*")
        #if caption is not None:
            #print("CAPTION: "+ET.tostring(caption,encoding='unicode',method='text'))
        return caption
    
    def getCaptionCitations(self,caption):
        caption_citations = []
        if caption is not None:
            allCit = caption.findall(".//xref[@ref-type='bibr']")
            for cit in allCit:
                citID = cit.attrib.get("rid")
                caption_citations.append(citID)
                #print("CAPTION CITATIONS: "+str(caption_citations))
        return caption_citations

    
    def getTablesFoot(self,tableID):
        feet_list = []
        feet = self.root.findall(".//table-wrap[@id='"+tableID+"']//table-wrap-foot//p")
        for foot in feet:
            feet_list.append(ET.tostring(foot,encoding='unicode'))
            #print("FOOT: "+ET.tostring(foot,encoding='unicode'))
        return feet_list
    

    def getTableHead(self, tableID):
        tableHead = self.root.find(".//table-wrap[@id='"+tableID+"']//table//thead")
        #if tableHead is not None:
            #print("BODY: "+ET.tostring(tableHead,encoding='unicode'))
        return tableHead
    
    def getTableBody(self, tableID):
        tableBody = self.root.find(".//table-wrap[@id='"+tableID+"']//table//tbody")
        #if tableBody is not None:
            #print("TABLE HEAD: "+ET.tostring(tableBody,encoding='unicode'))
        return tableBody
    
    def getParagraphText(self, tableID):
        text = self.root.xpath(".//xref[@ref-type='table' and @rid='"+tableID+"']/..")
        #for element in text:
            # for comment in element.xpath('.//comment()'):
            #     comment.getparent().remove(comment)
        #print("TEXT: ")
        #for i in range(0,len(text)):
            #print(ET.tostring(text[i],encoding='utf-8').decode('utf-8'))
        return text
    
    def getParagraphCitations(self, p):
        allCit = p.findall(".//xref[@ref-type='bibr']")
        cit_list = []
        for cit in allCit:
            citID = cit.attrib.get("rid")
            citation = self.root.find(".//ref[@id='"+citID+"']")
            if citation is not None:
                # for comment in citation.xpath('.//comment()'):
                #     comment.getparent().remove(comment)
                cit_list.append(ET.tostring(citation,encoding='utf-8').decode('utf-8'))
                #print("PARAGRAPH CITATIONS: "+ET.tostring(citation,encoding='utf-8').decode('utf-8'))
        return cit_list
    
    def getCells(self, tableID):
        content_cells = self.root.xpath(".//table-wrap[@id='"+tableID+"']//td/text()")
        return content_cells
    
    def getCitedIn(self, cell):
        #print("CONTENT: ", cell)
        part1, part3 = '', ''
        part2 = cell.lower()
        if "'" in cell:
            if '"' in cell:
                h = cell.split("'")
                text = h[0]
                for i in range(len(h)):
                    if(i>0):
                        text = text+"\'"+h[i]
                part2 = text.lower()
                part1 = ".//p[contains(lower-case(.), '"
                part3 = "')]"
            part1 = './/p[contains(lower-case(.), "'
            part3 = '")]'
        else:
            part1 = ".//p[contains(lower-case(.), '"
            part3 = "')]"
        # print("cell: "+cell)
        # print(part1+part2+part3)
        cited_in_list = elementpath.select(self.root,(part1+part2+part3))
        out_list = []
        for cit in cited_in_list:
            #print("CITED_IN: " + ET.tostring(cit,encoding='utf-8').decode('utf-8'))
            out_list.append(ET.tostring(cit,encoding='utf-8').decode('utf-8'))
        return out_list

    def getFigures(self):
        fig_list = self.root.findall(".//fig")
        return fig_list
    
    def getFigureID(self, fig):
        figID = fig.attrib.get("id")
        #print("FIGURE ID: "+figID)
        return figID
    
    def getFigureCaption(self,figID):
        figCaption = self.root.find(".//fig[@id='"+figID+"']//caption//*")
        #if figCaption is not None:
            #print("CAPTION: "+ET.tostring(figCaption,encoding='unicode'))
        return figCaption
    
    def getParagraphCitedIn(self, figID):
        cited_in_list = self.root.xpath(".//xref[@ref-type='fig' and @rid='"+figID+"']/..")
        #for element in text:
            # for comment in element.xpath('.//comment()'):
            #     comment.getparent().remove(comment)
        #print("CITED_IN: ")
        #for i in range(0,len(cited_in_list)):
            #print(ET.tostring(cited_in_list[i],encoding='utf-8').decode('utf-8'))
        return cited_in_list
    
    def getSource(self,figID,fileName):
        graphic = self.root.find(".//fig[@id='"+figID+"']//graphic")
        url = ''
        src = ''
        if graphic is not None:
            for k in graphic.attrib:
                if "href" in k:
                    src = graphic.attrib.get(k)
            url = "https://www.ncbi.nlm.nih.gov/pmc/articles/"+fileName+"/bin/"+src+".jpg"
            #print("SRC: " + url)
        return url
    
    def get_second_element_by_content(self, value, cells_list):
        for element in cells_list:
            if element.get("content") == value:
                return element.get("cited_in")
        return None


















    

    

    