def smartDuplicate():
    pass
    #check objects for numberBased or letter based suffixes
    #check for underscores
    #do I have underbars?
    #CPS is type
    
def smartRenameIt(name = 'ob', suffix = 'GP'):
    import maya.cmds as cmd
    parent = []
    num = 0
    index = ''
    obLib = {'transform':'GEO',
    'nurbsCurve':'CTL',
    'joint':'JNT',
    'clusterHandle':'CLR',
    'locator':'LOC',
    'ikHandle':'IK',
    'aimConstraint':'amC',
    'pointConstraint':'ptC',
	'orientConstraint':'orC',
	'parentConstraint':'paC',
    'mesh':'GEO'}
    
    obs = cmd.ls(sl=True)
    for one in obs:   
        num += 1  
        index = '%02d' % num   
        objectType = cmd.objectType(one)
        type = obLib[objectType]        
        if type == 'JNT' and one == obs[-1]:
            prnt = cmd.listRelatives(obs[-1], p=True)
            try:
                if prnt[0] == obs[-2]:
                    index = 'end'
            except:
                pass
        if type == 'GEO':     
            child = cmd.listRelatives(one, s = True)
            if child is None:
                type = 'GP' 
        newName = '%s_%s_%s' % (name, index, type) 
        cmd.rename(one, newName)
    

smartRenameIt('foamB')
   