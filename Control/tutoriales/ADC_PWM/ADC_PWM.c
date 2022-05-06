//incluimos todas las bibliotecas que vamos a usar con las funciones para PWM, ADC y GPIO
#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "hardware/adc.h"
#include "hardware/pwm.h"

//Definimos los nombres de los GPIO que vamos a usar
#define POT_PIN 26
#define LED_PIN 14

// creamos una función para que funcione el pwm desde 0 a 255

//El ADC es de 12 bits por lo que el maximo valor es de 4095
long map(long x, long in_min, long in_max, long out_min, long out_max)
{
    return (x - in_min)*(out_max-out_min) / (in_max-in_min) + out_min;
}

int main(){

    //iniciamos la biblioteca stdio para que funcione todo el programa
    stdio_init_all();

    //Le damos reloj al ADC
    adc_init();
    
    adc_gpio_init(POT_PIN);//iniciamos el PIN 26 correspondiente al ADC que lee el potenciometro
    adc_select_input(0);//Activamos el canal 0 del ADC para el potenciometro
    //canal 0 corresponde a pin 26
    //canal 1 corresponde a pin 27
    //canal 2 corresponde a pin 28
    //canal 3 corresponde a pin 29, aqui se encuentra el sensor de temperatura

    gpio_set_function(LED_PIN, GPIO_FUNC_PWM); // seleccionamos la funcion de gpio con el 
    //numero de pin correspondiente a LED_PIN, la función será PWM


    //existen 8 slices para el PWM cada slice tiene dos salidas PWM, 
    //en total hay 16 salidas PWM, y todos los GPIO pueden controlarlos
    //Para el GPIO 14 es el PWM_A_7
    //LO de abajo significa que seleccionamos el PWM 7, ambos canales A y B
    uint slice_num = pwm_gpio_to_slice_num(LED_PIN);

    //CONFIGURAMOS EL PWM PARA TENER UN MAXIMO DE 256 CICLOS DE RELOJ PARA EL RESET    //existen 8 slices para el PWM cada slice tiene dos salidas PWM, 
    //PARA VERLO EN EL LED
    pwm_set_wrap(slice_num, 255);

    pwm_set_chan_level(slice_num, PWM_CHAN_A,0); //Empezamos en 0 el nivel del PWM
    //RECORDEMOS QUE ESTAMOS EN EL CANAL A

    pwm_set_enabled(slice_num,true); //Habilitamos el PWM

//loop principal
    while (1)
    {
         uint16_t result = adc_read(); //Leemos el resultado del ADC del potenciometro

         long pwm_value = map(result, 0, 4095, 0, 255); //convertimos el resultado del potenciometro a un valor entre 0 a 255

         printf("Raw: %d \t PWM: %d\n", result, pwm_value);
        //imprimimos el valor del resultado del ADC y el valor para el PWM 

        //SELECCIONAMOS CON PWM_VALUE LA CANTIDAD DE CICLOS QUE QUEREMOS 
        //EN ALTO DENTRO DEL PERIODO DE 255, EJ, SI pwm_value ES 10 PUES 10 CICLOS DE LOS 
        //255 SERÁN 1, LOS DEMÁS SERÁN 0

        //INDICAMOS QUE USAREMOS EL NUMERO DE SLICE 7 PORQUE LO DECLARAMOS ARRIBA
        //INDICAMOS QUE USAREMOS EL CANAL A
        //INDICAMOS QUE USAMOS EL VALOR DEL PWM DEL POTENCIOMETRO
         pwm_set_chan_level(slice_num, PWM_CHAN_A, pwm_value);
         
         //RETARDO DE 500ms para visualizar los datos en la pantalla
         sleep_ms(50);
    }
    
}