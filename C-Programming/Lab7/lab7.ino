#define LED 9
#define bLED 13
int buttonPress = 1;

void setup() {
    Serial.begin(9600);
    pinMode(LED, OUTPUT);
}

void loop() {
    attachInterrupt(2, button, FALLING);
    if (buttonPress == 0) {
        digitalWrite(bLED, HIGH);
        delay(50);
        digitalWrite(bLED, LOW);
        delay(50);
    } 
    else if (buttonPress == 1) {
        int light = 0;
        while (true) {
            delay(8); // roughly
            analogWrite(LED, light);
            light += 1;
            if (light >= 255) {
                light = 0;
            }
        }
    } 
    else if (buttonPress == 2) {
        digitalWrite(bLED, HIGH);
        delay(100);
        digitalWrite(bLED, LOW);
        delay(100);
    }
}

void button() {
    buttonPress += 1;
    if (buttonPress > 2) {
        buttonPress = 0;
    }
}
