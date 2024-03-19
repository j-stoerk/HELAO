import pyHamiltonPSD as PSD
#from pyHamiltonPSD import util2

PSD.pumps = []
PSD.pumpLength = 16
PSD.connect(8, 9600)
PSD.definePump('0', PSD.PSDTypes.psd4.value, PSD.SyringeTypes.syringe125mL.value) # make sure that 1.25 mL syringe is added in util.py and psd.py

cmd = PSD.CommandPSD4(PSD.CommandPSD4)
cm = PSD.Command(PSD.Command)

### Initialialization of the pump as from the software
PSD.communication.sendCommand('0', '/1h30001R') # enable Hamilton protocol
PSD.executeCommand(PSD.pumps[0], cm.enableHFactorCommandsAndQueries() + PSD.pumps[0].command.executeCommandBuffer())

PSD.communication.sendCommand('0', '/1h20000R') # initialization of the valve
PSD.executeCommand(PSD.pumps[0], cm.initializeValve() + PSD.pumps[0].command.executeCommandBuffer())

PSD.communication.sendCommand('0', '/1h10010R') # initialization of the syringe, speed = 10
PSD.executeCommand(PSD.pumps[0], cm.initializeSyringeOnly(10) + PSD.pumps[0].command.executeCommandBuffer())

### Set speed of the syringe
PSD.executeCommand(PSD.pumps[0], cm.setSpeed(10) + PSD.pumps[0].command.executeCommandBuffer()) # from 1 to 40 (40 is the slowest)

### Move the syringe to the absolute position
PSD.executeCommand(PSD.pumps[0], cmd.absolutePosition(0)+ PSD.pumps[0].command.executeCommandBuffer()) # 3000 is max (number of rotations) corresponds to 1.25 mL

### Set speed and move the syringe combined
PSD.executeCommand(PSD.pumps[0], cmd.absolutePosition(0)+ PSD.pumps[0].command.executeCommandBuffer())

### Rotate the valve
PSD.executeCommand(PSD.pumps[0], cm.clockwiseAngularValveMove(45)+ PSD.pumps[0].command.executeCommandBuffer())
PSD.communication.sendCommand('0', '/1h28000R')

PSD.executeCommand(PSD.pumps[0], cm.shortestDirectAngularValveMove(0)+ PSD.pumps[0].command.executeCommandBuffer())

### Queries
response = PSD.executeCommand(PSD.pumps[0], cm.commandBufferStatusQuery())

PSD.QueryCommandsEnumeration.BUFFER_STATUS.value


### Other settings
PSD.executeCommand(PSD.pumps[0], cmd.setStartVelocity(50)) 
PSD.executeCommand(PSD.pumps[0], cmd.setMaximumVelocity(500))
PSD.executeCommand(PSD.pumps[0], cmd.stopVelocity(50))
PSD.executeCommand(PSD.pumps[0], cmd.syringeHomeSensorStatusQuery())


PSD.executeCommand(PSD.pumps[0], cm.moveValveClockwiseDirection(2))
PSD.executeCommand(PSD.pumps[0], cm.angularValveMoveCommandCtr(45, 15))
PSD.executeCommand(PSD.pumps[0], cm.clockwiseAngularValveMove(45))        

PSD.executeCommand(PSD.pumps[0], cm.setSpeed(5) + cmd.absolutePosition(0)+ PSD.pumps[0].command.executeCommandBuffer()) 


PSD.disconnect()


