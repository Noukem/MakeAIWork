import csv 

marslanderSpecs = { 'length': 6, 
                   'width': 1.56, 
                   'weight': 360, 
                   'deckHeight': (83, 108), 
                   'robotArmLength': 1.8, 
                   'numberOfSolarPanels': 2}
marslanderSpecs.items()

marslanderSpecs.update( {'scienceInstruments' : ("seismometer", "heat probe", "radio science experiment")} )
marslanderSpecs.update( {'image': "../pics/mars.nasa.jpg"} )
print(marslanderSpecs)