 #la minima version de cmake para que funcione

cmake_minimum_required(VERSION 3.12)

#incluimos el cmake file

include(pico_sdk_import.cmake)

# añadimos el nombre del proyecto
project(pico_tutoriales C CXX ASM)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

# inicializamos el sdk
pico_sdk_init()

# añadimos el ejemplo que queremos probar

add_subdirectory(button_test)
add_subdirectory(ADC_PWM)
add_subdirectory(CAL_talon)
