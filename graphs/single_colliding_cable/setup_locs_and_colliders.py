import maya.cmds as cmds
sel = cmds.ls(sl=True)

#create BF
if len(cmds.ls(type="bifrostGraphShape")) == 0:
    cmds.CreateNewBifrostGraph()

bfg = cmds.ls(type="bifrostGraphShape")[0]

#locators
start = cmds.spaceLocator(n="start")[0]
cmds.move(-10,5,0,start)
mid = cmds.spaceLocator(n="mid")[0]
cmds.move(-5,-5,0,mid)
mid2 = cmds.spaceLocator(n="mid2")[0]
cmds.move(5,-5,0,mid2)
end = cmds.spaceLocator(n="end")[0]
cmds.move(10,5,0,end)

cmds.connectAttr(start+".worldPosition[0]", bfg+".start", f=True)
cmds.connectAttr(mid+".worldPosition[0]", bfg+".middle", f=True)
cmds.connectAttr(mid2+".worldPosition[0]", bfg+".middle_2", f=True)
cmds.connectAttr(end+".worldPosition[0]", bfg+".end", f=True)

#colliders
for count,each in enumerate(sel):
    cmds.connectAttr(each+".worldMesh[0]", bfg+".colliders["+str(count)+"]", f=True)