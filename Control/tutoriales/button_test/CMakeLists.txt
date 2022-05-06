add_executable(button_test
	button_test.c
	)

# ponemos las bibliotecas  pico_stdlib y hardware_gpio en el programa button_test
target_link_libraries(button_test pico_stdlib hardware_gpio)

#habilitamos la salida usb y deshabilitamos la salida uart para mandar el mensaje 
pico_enable_stdio_usb(button_test 1)
pico_enable_stdio_uart(button_test 0)

# create map/bin/hex file etc.
pico_add_extra_outputs(button_test)

