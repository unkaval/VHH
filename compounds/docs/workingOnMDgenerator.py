import maya.cmds as cmds
import json

#assign colours to data by type
def whichArray(value):
    types = cmds.vnn(listPortTypes = "BifrostGraph")
    floatsArray = [each for each in types if "float" in each and "Math" not in each]
    vectorArray = [each for each in types if "Math" in each and "x" not in each]
    intArray = [each for each in types if "int" in each or "long" in each or "char" in each or "short" in each]
    matrixArray = [each for each in types if "Math" in each and "x" in each]
    objectArray = [each for each in types if "Object" in each]
    stringArray = [each for each in types if "string" in each]
    fieldArray = [each for each in types if "Field" in each]
    boolArray = [each for each in types if "bool" in each and "Math" not in each]
    boolVec = [each for each in types if "bool" in each and "Math" in each] 
    fCurve = [each for each in types if "FCurve" in each]

    if value in floatsArray:
        return "82D99F"
    elif value in vectorArray:
        return "A8D977"    
    elif value in intArray:
        return "62CFD9"  
    elif value in matrixArray:
        return "E67373"  
    elif value in objectArray:
        return "90A3F4"  
    elif value in stringArray:
        return "D9BE6C" 
    elif value in boolArray:
        return "E69963" 
    elif value in fieldArray or value in boolVec or value in fCurve:
        return "CCB699" 
    else:
        return "000000"

def hasNoUI(data):
    #generate string for each port, including colour
    ports = data["compounds"][0]["ports"]
    for each in ports:
        pd = each["portDirection"]
        
        try:
            pt = each["portType"]  
        except:
            pt = "float"
            
        if pd == "input":    
            inString += '<span style="color:#'+whichArray(pt)+'">***'+each["portName"]+'***</span>\n<br />Description.\n\n'
        
        if pd == "output":
            outString += '<span style="color:#'+whichArray(pt)+'">***'+each["portName"]+'***</span>\n<br />Description.\n\n'
    
    return inString, outString

def hasUI(data):
    # get the UI order from the json as a String
    for index, item in enumerate(data["compounds"][0]["metadata"]):
        if item['metaName'] == "UILayout":
            UIString = (data["compounds"][0]["metadata"][index]['metaValue'])
    
    # cleanup that string
    UIString.replace(" ","")
    splitUIString = UIString.splitlines()
    
    # create the master string list in the order that UILayout dictates 
    stringlist = []
    for each in splitUIString:
        each.replace(" ","")
        if "port" in each:
            stringlist.append(each.strip().split(":")[1].replace("\"", "").strip())
    
    # setup the ports arrays
    inPorts = []
    outPorts = []
    
    # gather the ports data
    for port in ports:
        if port["portDirection"] == "input":
            inPorts.append(port)
        else:
            outPorts.append(port)
    
    #reorder ports by UI for the in direction only, build an ordered array
    orderedInPorts = []
    for string in stringlist:
        for port in inPorts:
            if port["portName"] == string:
                orderedInPorts.append(port)
            else:
                pass
    
    # loop through the ordered array of inputs, find the port type for colouring, and add the name of that port in that colour to a string
    for eachPort in orderedInPorts:
        pt = eachPort["portType"]
        inString += '<span style="color:#'+whichArray(pt)+'">***'+eachPort["portName"]+'***</span>\n<br />Description.\n\n'
    
    # loop through the ordered array of outputs, find the port type for colouring, and add the name of that port in that colour to a string
    for eachPort in outPorts:
        try:
            pt = eachPort["portType"]
            outString += '<span style="color:#'+whichArray(pt)+'">***'+eachPort["portName"]+'***</span>\n<br />Description.\n\n'
        except:
            outString += '<span style="color:#CCB699">***'+eachPort["portName"]+'***</span>\n<br />Description.\n\n'
    return inString, outString



# compoundsDir = "C:\\Users\\unkav\\Autodesk\\Bifrost\\Compounds\\VHH\\compounds\\"
compoundsDir = "C:\\Users\\unkav\\Documents\\BF Compounds\\VHH Compounds\\VHH\\compounds\\"


#directory and files
docDir = "docs\\"
compoundDir = "geo\\"
compound = "delete_components_by_volume.json"

#get the json data
compFile = open(compoundsDir+compoundDir+compound,"r")
data = json.load(compFile)
compFile.close()

# find the ports in the json
# ports = data["compounds"][0]["ports"]

# initialize strings
inString = ""
outString = ""

mNames = [index["metaName"] for index in data["compounds"][0]["metadata"]]
if "UILayout" in mNames:
    inString, outString = hasUI(data)
else:
    inString, outString = hasNoUI(data)

# construct generated .md
mdString = '### ***'+compound.split(".")[0]+'***\nDescription.<br />\n\n***\n## Input\n'
mdString += inString
mdString += '***\n## Output\n'
mdString += outString
mdName = compound.split(".")[0]+"_generated.md"

#write generated .md
mdFile = open(compoundsDir+docDir+mdName,"w")
mdFile.write(mdString)
mdFile.close()
