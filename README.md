# Resin-Efficiency

#This is one of the projects done at my old Company NiagaraBottling. 
#The issue at hand was that there was no accurate way to measure exactly how much  resin was being delivered from Resin supplier.
#There is a sensor that allows for the measurement of each Silo that holds the Resin in pounds. You might think that it's a simple FinalWeight-InitialWeight = Weight Delivered
#The thing is, there are PLC's constantly consuming the resin from each silo to create the bottles and caps. 
#Measuring how much resin was consumed by each PLC requires knowing how many bottles were created from that machine during the time of shipment of Resin. 
#A simple arithemetic equation will calculate how much resin was used. First Final-InitialProduction count of Bottles, that will be multiplied by the weight of each preform that makes the bottle/cap and then divided by (1/453grams) to convert to pounds. 
#This is then multiplied by a percetange based on what type of resin the PLC takes from whichever Silo or Silos it takes from. 

#The code given is the main code for this calculation; it was done in a program called Ignition.
#There are more things that could be done to make sure these results are accurate, but that would be done with a bit more coding in some other areas of the program. 
