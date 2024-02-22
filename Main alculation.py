  i = 1
	j = 1 
	x = 0
	consumed = 0
	#cap_weight = 		#grams
	#logger = system.util.getLogger("SiloResinUpdate")
	#logger.info("currentValue")
	#preform_weight = system.tag.read("Projects/BLT/ResinSilos/NaderSilo1/UsageData/Injection/HyPET1/PartWeight").value #grams
	
	if currentValue.value == True:
		#logger.info("iflog")
		plbs = system.tag.read("Projects/BLT/ResinSilos/NaderSilo1/SiloData/LevelLbs").value #levellbs
		system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/PreviousLBS", plbs) #levellbs
		#HYPETS 1-7
		machine=8	
				
		for i in range(1, machine):
#			get_consumed(i)				
			#CurrentHyPET = system.tag.read("Projects/BLT/ResinSilos/NaderSilo1/UsageData/Injection/HyPET" + str(i) + "/ProductionCount").value
			pHyPET = system.tag.read("Projects/BLT/ResinSilos/NaderSilo1/UsageData/Injection/HyPET" + str(i) + "/ProductionCount").value
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(i) + "/PrevProd" + str(i) + "", pHyPET)
			

				
	if currentValue.value == False:
		
		for j in range(1, 8):
#			previous_HyPET = system.tag.read("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/PetProd" + str(j) + "").value
#			arr.append(previous_HyPET)
			totalconsumed = get_consumed(j)
		previous_lbs =  system.tag.read("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/PreviousLBS").value
		new_lbs = system.tag.read("Projects/BLT/ResinSilos/NaderSilo1/SiloData/LevelLbs").value
		totalincreased = new_lbs - previous_lbs
		if totalincreased < 0:
			totalincreased = 0
		totaloffload = totalconsumed + totalincreased
		system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/LevelDifference", totalincreased)
		system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/TotalOffloadWeight", totaloffload)
		
def get_consumed(Machine):
	#HyPets NO HYCAPS INCLUDED
	
	for Machine in range(1,8):
		preform_weight = system.tag.read("Projects/BLT/ResinSilos/NaderSilo1/UsageData/Injection/HyPET"+ str(Machine) + "/PartWeight").value #grams
		previous_HyPET = system.tag.read("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/PrevProd" + str(Machine) + "").value
		new_HyPET = system.tag.read("Projects/BLT/ResinSilos/NaderSilo1/UsageData/Injection/HyPET" + str(Machine) + "/ProductionCount").value
		difference = new_HyPET - previous_HyPET
		if Machine == 1: 
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/NewProd" + str(Machine) + "", new_HyPET)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Difference" + str(Machine) + "", difference)
			consumedvalue1 = (difference * preform_weight / 453.592 * 0.34)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Consumption", consumedvalue1)
		if Machine == 2: 
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/NewProd" + str(Machine) + "", new_HyPET)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Difference" + str(Machine) + "", difference)
			consumedvalue2 = (difference * preform_weight / 453.592 * 0.34)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Consumption", consumedvalue2)
		if Machine == 3: 
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/NewProd" + str(Machine) + "", new_HyPET)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Difference" + str(Machine) + "", difference)			
			consumedvalue3 = (difference * preform_weight / 453.592 * 0.94)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Consumption", consumedvalue3)
		if Machine == 4:
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/NewProd" + str(Machine) + "", new_HyPET)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Difference" + str(Machine) + "", difference)
			consumedvalue4 = (difference * preform_weight / 453.592 * 0)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Consumption", consumedvalue4)
		if Machine == 5: 
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/NewProd" + str(Machine) + "", new_HyPET)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Difference" + str(Machine) + "", difference)
			consumedvalue5 = (difference * preform_weight / 453.592 * 0)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Consumption", consumedvalue5)
		if Machine == 6:
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/NewProd" + str(Machine) + "", new_HyPET)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Difference" + str(Machine) + "", difference)
			consumedvalue6 = (difference * preform_weight / 453.592 * 1)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Consumption", consumedvalue6)
		if Machine == 7: 
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/NewProd" + str(Machine) + "", new_HyPET)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Difference" + str(Machine) + "", difference)
			consumedvalue7 = (difference * preform_weight / 453.592 * 0.4)
			system.tag.write("Projects/BLT/ResinSilos/NaderSilo1/SiloData/Values/InjectionValues/HyPets/HyPET" + str(Machine) + "/Consumption", consumedvalue7)
	consumed = consumedvalue1 + consumedvalue2 + consumedvalue3 + consumedvalue4 + consumedvalue5 + consumedvalue6 + consumedvalue7
	return consumed
