//Este programa es para comprender el funcionamiento de pico en C probando un botón y poniendo un mensaje serial


#include <stdio.h> //biblioteca mas importante en C
#include "pico/stdlib.h" //biblio con funciones principales de la pico
#include "hardware/gpio.h" //biblio que contiene el uso de hardware de la pico

//EL pin que vamos a usar es el 15
#define BUTTON_PIN 15

//Función principal
int main () {

    //Se inicializa la biblioteca stdio       
    stdio_init_all();    
    //Se inicializa el botón seleccionado
    gpio_init(BUTTON_PIN);
    // Se da función de entrada al GPIO del Button_PIN
    gpio_set_dir(BUTTON_PIN, GPIO_IN);    
    // Se pone una resistencia interna de pull up al pin requerido 15
    gpio_pull_up(BUTTON_PIN);

    while (true)
    {
        //mientras se detecte un 0 del gpio 15 se mandará un mensaje de que se ha presionado el botón
        if(!gpio_get(BUTTON_PIN)){
            printf("Se ha presionado el botón\n");
        }
        //se pone un retador de 250 ms para enviar rebotes
        sleep_ms(250);
    }
    

}
