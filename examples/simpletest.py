import time
from Drivers.TSL2561 import *
chip = TSL2561()

while True:
	chip.power_on()
	print("Raw Channel 0" + str(chip.read_channel0()))
	print("Raw Channel 1" + str(chip.read_channel1()))
	print("Lux Channel 0" + str(chip.calculate_lux(chip.read_channel0())))
	print("Lux Channel 1" + str(chip.calculate_lux(chip.read_channel1())))
	print("Full Spectrum Lux" + str(chip.get_full_lux()))
	print("IR Spectrum Lux" + str(chip.get_ir_lux()))
	print("Visible Lux" + str(chip.get_visible_lux()))
	chip.power_off()
	time.sleep(1)
