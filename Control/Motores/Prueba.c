#include "pico/stdlib.h"
#include "hardware/pwm.h"

#define LED_PIN 25
#define LED_SLICE 4 //slice del pin
#define LED_CHANNEL 1 //channel del pin(B)


void setup()
{
	//configurar gpio
	gpio_init(LED_PIN);
	gpio_set_function(LED_PIN, GPIO_FUNC_PWM);
	// Configurar modulo PWM
	pwm_set_clkdiv(LED_SLICE, 1.0);
	pwm_set_wrap(LED_SLICE, 200);
	pwm_set_chan_level(LED_SLICE, LED_CHANNEL, 0);
	pwm_set_enabel(LED_SLICE, true);
}
int main()
{
	setup();
	// bucle principal
	pwm_set_chan_level(LED_SLICE, LED_CHANNEL, 10);
	sleep_ms(1000);
	//cambio de modulación
	pwm_set_chan_level(LED_SLICE, LED_CHANNEL, 200);
	sleep_ms(1000);

}