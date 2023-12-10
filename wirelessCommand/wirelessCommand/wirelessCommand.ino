#include <SoftwareSerial.h>

// Left motor
int Lin1 = 32;
int Lin2 = 34;
int pwmL = 11;

// Right motor
int Rin1 = 28;
int Rin2 = 30;
int pwmR = 10;

#define TX 52
#define RX 50
uint8_t a = 0;
SoftwareSerial myserial(TX, RX);

void setup() {
  Serial.begin(9600);
  myserial.begin(9600);
  pinMode(Lin1, OUTPUT);
  pinMode(Lin2, OUTPUT);
  pinMode(pwmL, OUTPUT);
  pinMode(Rin1, OUTPUT);
  pinMode(Rin2, OUTPUT);
  pinMode(pwmR, OUTPUT);
}

void loop() {
  if (myserial.available() > 0) {
    char data = myserial.read();
    Serial.print(data);
    Serial.print("\n");

    switch (data) {
      case 'F': avancer(a); break;
      case 'B': reculer(a); break;
      case 'L': gauche(a); break;
      case 'R': droite(a); break;
      case '0': change(50); break;
      case '1': change(75); break;
      case '2': change(100); break;
      case '3': change(120); break;
      case '4': change(140); break;
      case '5': change(160); break;
      case '6': change(180); break;
      case '7': change(200); break;
      case '8': change(220); break;
      case '9': change(240); break;
      case 'q': change(255); break;
      default: stopp(); break;
    }
  }
}

void change(uint8_t x) {
  a = x;
}

void reculer(uint8_t val) {
  digitalWrite(Lin1, LOW);
  digitalWrite(Lin2, HIGH);
  analogWrite(pwmL, val);
  digitalWrite(Rin1, LOW);
  digitalWrite(Rin2, HIGH);
  analogWrite(pwmR, val);
}

void avancer(uint8_t val) {
  digitalWrite(Lin1, HIGH);
  digitalWrite(Lin2, LOW);
  analogWrite(pwmL, val);
  digitalWrite(Rin1, HIGH);
  digitalWrite(Rin2, LOW);
  analogWrite(pwmR, val);
}

void gauche(uint8_t val) {
  digitalWrite(Lin1, LOW);
  digitalWrite(Lin2, HIGH);
  analogWrite(pwmL, val);
  digitalWrite(Rin1, HIGH);
  digitalWrite(Rin2, LOW);
  analogWrite(pwmR, val);
}

void droite(uint8_t val) {
  digitalWrite(Lin1, HIGH);
  digitalWrite(Lin2, LOW);
  analogWrite(pwmL, val);
  digitalWrite(Rin1, LOW);
  digitalWrite(Rin2, HIGH);
  analogWrite(pwmR, val);
}

void stopp() {
  digitalWrite(Lin1, LOW);
  digitalWrite(Lin2, LOW);
  analogWrite(pwmL, 0);
  digitalWrite(Rin1, LOW);
  digitalWrite(Rin2, LOW);
  analogWrite(pwmR, 0);
}