CSV File Input Format and Explanation

JMS Module:
module,moduleName,serverTarget:type

Foreign Server:
foreign,moduleName,foreignName,jndiInitContextFactory,jndiConnUrl

Foreign Destination:
dest,moduleName,foreignName,foreignDestName,localJNDIName,remoteJNDIName

Foreign Connection Factory Name:
conn,moduleName,foreignName,foreignConnFactName,localJNDIName,remoteJNDIName




JMS Module
- module		: tag that use to create JMS Module (dont change)
- moduleName	: name of JMS Module you want (change)
- serverTarget	: targetName:Server  => for server target
				  targetName:Cluster => for cluster target
				  targetName:Server|targetName:Cluster => for target more than one

Foreign Server:
- foreign		: tag that use to create Foreign Server (dont change)
- moduleName	: name of JMS Module that has been created before (change)
- foreignName	: name of Foreign Server in JMS Module (change)
- jndiInitContextFactory	: JNDI Initial Context Factory
- jndiConnUrl	: JNDI Connection URL

Foreign Destination:
- dest			: tag that use to create Foreign Destination inside Foreign Server (dont change)
- moduleName	: name of JMS Module that has been created before (change)
- foreignName	: name of Foreign Server in JMS Module that has been created before (change)
- foreignDestName	: name of Foreign Destination that created inside Foreign Server (change)
- localJNDIName	: Local JNDI Name
- remoteJNDIName: Remote JNDI Name

Foreign Connection Factory Name:
- conn			: tag that use to create Connection Factory inside Foreign Server (dont change)
- moduleName	: name of JMS Module that has been created before (change)
- foreignName	: name of Foreign Server in JMS Module that has been created before (change)
- foreignConnFactName	: name of Foreign Connection Factory that created inside Foreign Server (change)
- localJNDIName	: Local JNDI Name
- remoteJNDIName: Remote JNDI Name