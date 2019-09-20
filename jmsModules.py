from java.io import FileInputStream


def createJMSModule(line):
  try:
    startEdit()
    cd('/')
    items = line.split(',')
    items = [item.strip() for item in items]
    (type,moduleName,serverTarget) = items
    
    # Check if JMS Module already exist
    redirect('/dev/null','false')
    exist = ls('/JMSSystemResources/',returnMap='true')
    if moduleName in exist:
      print('\nJMS Modules ' + moduleName + ' already exist !!!!')
      exit(exitcode=1,defaultAnswer='y')
	
    # Create new JMS Module
    print('\nCreate JMS Module: ' + moduleName + '\n')
    cmo.createJMSSystemResource(moduleName)
    
    # Set Up Target server/cluster
    cd('/JMSSystemResources/' + moduleName)
    targetsForDeployment = []
    targets = serverTarget.split('|')
    for target in targets: 
      if(target == '') :
        break;
      index=target.find(':')
      serverName=target[0:index]
      type=target[index+1:]
      nextName =str('com.bea:Name='+serverName+',Type='+type)
      targetsForDeployment.append(ObjectName(nextName))
    set('Targets',jarray.array(targetsForDeployment, ObjectName))
	
    save()
    activate()
	
  except Exception, e:
    print e



def createForeignServer(line):
  try:
    startEdit()
    cd('/')
    items = line.split(',')
    items = [item.strip() for item in items]
    (type,moduleName,foreignName,jndiInitConnFac,jndiConUrl) = items
	
    # Check if JMS Module name correct
    redirect('/dev/null','false')
    modExist = ls('/JMSSystemResources/',returnMap='true')
    if moduleName not in modExist:
      print('\nWrong JMS Module Name :' + moduleName + ' !!!\n')
      exit(exitcode=1,defaultAnswer='y')
	
    # Check if Foreign Server already exist
    cd('/JMSSystemResources/' + moduleName + '/JMSResource/' + moduleName )
    redirect('/dev/null','false')
    exist = ls('ForeignServers',returnMap='true')
    if foreignName in exist:
      print('\nForeign Server ' + foreignName + ' already exist !!!!')
      exit(exitcode=1,defaultAnswer='y')
	  
    # Create Foreign Name
    print('\nCreate Foreign Server: ' + foreignName )
    cmo.createForeignServer(foreignName)
	
    # Set Initial Context Factory and Connection URL
    cd('/JMSSystemResources/' + moduleName + '/JMSResource/' + moduleName + '/ForeignServers/' + foreignName)
    print('Foreign Server: ' + foreignName + ' Initial Context Factory: ' + jndiInitConnFac)
    cmo.setInitialContextFactory(jndiInitConnFac)
    print('Foreign Server: ' + foreignName + ' Set JNDI Connection URL: ' + jndiConUrl)
    cmo.setConnectionURL(jndiConUrl)

    save()
    activate()

  except Exception, e:
    print e



def createForeignDest(line):
  try:
    startEdit()
    cd('/')
    items = line.split(',')
    items = [item.strip() for item in items]
    (type,moduleName,foreignName,foreignDestName,localJNDIName,remoteJNDIName) = items
	
    # Check if JMS Module name correct
    redirect('/dev/null','false')
    modExist = ls('/JMSSystemResources/',returnMap='true')
    if moduleName not in modExist:
      print('\nWrong JMS Module Name :' + moduleName + '  !!!\n')
      exit(exitcode=1,defaultAnswer='y')
    
    # Check if Foreign name correct
    redirect('/dev/null','false')
    forExist = ls('/JMSSystemResources/' + moduleName + '/JMSResource/' + moduleName + '/ForeignServers/',returnMap='true')
    if foreignName not in forExist:
      print('\nWrong Foreign Name :' + foreignName + ' !!!\n')
      exit(exitcode=1,defaultAnswer='y')	  

    # Check if foreign Destination name already exist
    cd('/JMSSystemResources/' + moduleName + '/JMSResource/' + moduleName + '/ForeignServers/' + foreignName)
    redirect('/dev/null','false')
    exist = ls('ForeignDestinations',returnMap='true')
    if foreignDestName in exist:
      print('\nForeign Destination ' + foreignDestName + ' already exist !!!!')
      exit(exitcode=1,defaultAnswer='y')
	  
    # Create Foreign Destination 
    print('\nCreate Foreign Destination: ' + foreignDestName)
    cmo.createForeignDestination(foreignDestName)
	
    # Set Local and Remote JNDI for Foreign Destination Name
    cd('/JMSSystemResources/' + moduleName + '/JMSResource/' + moduleName + '/ForeignServers/' + foreignName + '/ForeignDestinations/' + foreignDestName)
    print('Foreign Destination: ' + foreignDestName +' Local JNDI Name: ' + localJNDIName)
    cmo.setLocalJNDIName(localJNDIName)
    print('Foreign Destination: ' + foreignDestName +' Remote JNDI Name: ' + localJNDIName)
    cmo.setRemoteJNDIName(remoteJNDIName)

    save()
    activate()

  except Exception, e:
    print e



def createforeignConnFactName(line):
  try:
    startEdit()
    cd('/')
    items = line.split(',')
    items = [item.strip() for item in items]
    (type,moduleName,foreignName,foreignConnFactName,localJNDIName,remoteJNDIName) = items
	
    # Check if JMS Module name correct
    redirect('/dev/null','false')
    modExist = ls('/JMSSystemResources/',returnMap='true')
    if moduleName not in modExist:
      print('\nWrong JMS Module Name :' + moduleName + ' !!!\n')
      exit(exitcode=1,defaultAnswer='y')
    
    # Check if Foreign name correct
    redirect('/dev/null','false')
    forExist = ls('/JMSSystemResources/' + moduleName + '/JMSResource/' + moduleName + '/ForeignServers/',returnMap='true')
    if foreignName not in forExist:
      print('\nWrong Foreign Name :' + foreignName + ' !!!\n')
      exit(exitcode=1,defaultAnswer='y')
	
    # Check if Foreign Name already exist
    cd('/JMSSystemResources/' + moduleName + '/JMSResource/' + moduleName + '/ForeignServers/' + foreignName)
    redirect('/dev/null','false')
    exist = ls('ForeignConnectionFactories',returnMap='true')
    if foreignConnFactName in exist:
      print('\nForeign Connection Factory ' + foreignConnFactName + ' already exist !!!!')
      exit(exitcode=1,defaultAnswer='y')
	  
    # Create Foreign Destination 
    print('\nCreate Foreign Destination: ' + foreignConnFactName)
    cmo.createForeignConnectionFactory(foreignConnFactName)
	
    # Set Local and Remote JNDI Name
    cd('/JMSSystemResources/' + moduleName + '/JMSResource/' + moduleName + '/ForeignServers/' + foreignName + '/ForeignConnectionFactories/' + foreignConnFactName)
    print('Foreign Destination: ' + foreignConnFactName + ' Local JNDI Name: ' + localJNDIName)
    cmo.setLocalJNDIName(localJNDIName)
    print('Foreign Destination: ' + foreignConnFactName + ' Remote JNDI Name: ' + remoteJNDIName)
    cmo.setRemoteJNDIName(remoteJNDIName)

    save()
    activate()

  except Exception, e:
    print e



def main():
  propInputStream = FileInputStream(sys.argv[1])
  configProps = Properties()
  configProps.load(propInputStream)
   
  url=configProps.get("adminUrl")
  username=configProps.get("importUser")
  password=configProps.get("importPassword")
  csvLoc=configProps.get("csvLoc")
  
  connect(username , password , url)
  edit()
  file=open(csvLoc)
  for line in file.readlines():
    if line.strip().startswith('module'):
      createJMSModule(line)
    elif line.strip().startswith('foreign'):
      createForeignServer(line)
    elif line.strip().startswith('dest'):
      createForeignDest(line)
    elif line.strip().startswith('conn'):
      createforeignConnFactName(line)
    else:
      continue
	
  disconnect()

main()
	
