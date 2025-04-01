#define LEDPIN 9
#define INPIN A0

void setup() {
    DDRB |= (1 << LEDPIN); // ledpin as output
    cli(); // disable global interrupts
    TCCR1A = 0;
    TCCR1B = 0; // timer1 off
    OCR1A = (16000000 / (64 * 2 * 10)) - 1;
    TCCR1B |= (1 << WGM12); // turn on CTC mode
    TCCR1B |= (1 << CS10);
    TCCR1B |= (1 << CS11); // set prescaler to 64
    TIMSK1 |= (1 << OCIE1A); // enable timer compare interrupt
    sei(); // enable global interrupts
}

ISR(TIMER1_COMPA_vect) {
    PORTB ^= (1 << LEDPIN); // toggle ledpin
}

void loop() {
    int POTENTIOMTR = map(analogRead(INPIN), 0, 1023, 2, 10);
    OCR1A = (16000000 / (64 * 2 * POTENTIOMTR)) - 1;
}
