add_executable(ADC_PWM
	ADC_PWM.c
	)

# ponemos las bibliotecas  pico_stdlib y hardware_gpio en el programa ADC_PWM
target_link_libraries(ADC_PWM pico_stdlib hardware_gpio hardware_adc hardware_pwm)

#habilitamos la salida usb y deshabilitamos la salida uart para mandar el mensaje 
pico_enable_stdio_usb(ADC_PWM 1)
pico_enable_stdio_uart(ADC_PWM 0)

# create map/bin/hex file etc.
pico_add_extra_outputs(ADC_PWM)

