#include <stdio.h>

#include "pico/stdlib.h"
#include "pico/cyw43_arch.h"

char ssid[] = "moon";
char password[] = "123456789";

int main() {
    
    // Initialise IO
    stdio_init_all();

    // Initialise wifi module 
    if (cyw43_arch_init()) {
        printf("Wi-Fi init failed");
        return -1;
    }

    // Enable connection to an access pt. ie. a wifi router, modem etc...
    cyw43_arch_enable_sta_mode();

    // Connect to the desired access pt. using the hardcoded parameters.
    if (cyw43_arch_wifi_connect_timeout_ms(ssid, password, CYW43_AUTH_WPA2_AES_PSK, 10000))
    {
        return 1;
    }

    // If connection is successful flash the LED.
    while (true) {
        cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 1);
        sleep_ms(250);
        cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 0);
        sleep_ms(250);
    }
}
