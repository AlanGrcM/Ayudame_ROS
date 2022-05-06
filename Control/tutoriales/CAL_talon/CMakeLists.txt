add_executable(CAL_talon
	CAL_talon.c
	)

# ponemos las bibliotecas  pico_stdlib y hardware_gpio en el programa CAL_talon
target_link_libraries(CAL_talon pico_stdlib hardware_gpio hardware_adc hardware_pwm)

#habilitamos la salida usb y deshabilitamos la salida uart para mandar el mensaje 
pico_enable_stdio_usb(CAL_talon 1)
pico_enable_stdio_uart(CAL_talon 0)

# create map/bin/hex file etc.
pico_add_extra_outputs(CAL_talon)

