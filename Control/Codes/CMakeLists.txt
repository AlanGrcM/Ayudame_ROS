
cmake_minimum_required(VERSION 3.12)

# Pull in SDK (must before project)
include(pico_sdk_import.cmake)

project(pico_tutorial C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

# Initialize the SDK
pico_sdk_init()

# Add my test example
add_subdirectory(OnLed)
add_subdirectory(button_test)
add_subdirectory(analog_io)
add_subdirectory(ultrasonico)
add_subdirectory(carrito)
add_subdirectory(motores)
add_subdirectory(Display1602)
add_subdirectory(motorblue)
add_subdirectory(hc05)
add_subdirectory(Talonsr)
add_subdirectory(CalTalon)
add_subdirectory(Teclado)
