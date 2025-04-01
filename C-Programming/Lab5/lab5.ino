#define LED_PIN 8 // initialize all pins and values
#define BUZZER_PIN 9
#define START_PIN 7
#define PLAYERONE 1
#define PLAYERTWO 2
#define B00000000 0x0
#define Bxx000011 0x3

boolean gameStart = false;
int x = 0;
int s = 0;
int e1 = 0;
int e2 = 0;
int difference = 0;
int difference2 = 0;

void setup() { // set up serial monitor and ports
    Serial.begin(9600);
    DDRD = B00000000;
    DDRB = Bxx000011;
    boolean SINGLE = true;
}

void loop() {
    if (digitalRead(START_PIN)) {
        game();
    }
}

void game() {
    delay(random(1000, 10000));
    s = millis();
    
    #if BUZZER_PIN
        digitalWrite(BUZZER_PIN, HIGH);
    #else
        digitalWrite(LED_PIN, HIGH);
    #endif

    #if SINGLE
        if (digitalRead(PLAYERONE)) {
            e1 = millis();
            difference = e1 - s;
            println(difference);
            break;
        }
    #endif
}
