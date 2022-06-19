#include <SoftwareSerial.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <TimerOne.h>
#include <math.h>

/* Pin definitions */
#define motor_A     8
#define motor_B     9
#define encoder_A   2
#define encoder_B   3
#define pwmPin      11

/* PID coeficients definitions*/
#define b0 4.3887
#define b1 -3.3075
#define b2 0.0000

/* PID limits*/
#define lUp 12
#define lDo -12


/* Variables */
volatile unsigned int counter = 0;
volatile unsigned int dataIndex = 0;
unsigned int sampleTime;       
unsigned int dataMax;

volatile double setPoint = 0;
volatile double preError1 = 0;
volatile double preError2 = 0;
volatile double preU = 0;

/* Functions */
void encoderCount();
void angularVelocity();

void setup() {
  pinMode(motor_A,OUTPUT);
  pinMode(motor_B,OUTPUT);
  pinMode(pwmPin,OUTPUT);

  Serial.begin(115200);
  pinMode(encoder_A, INPUT);
  pinMode(encoder_B, INPUT);

  attachInterrupt(digitalPinToInterrupt(encoder_A),encoderCount_A,CHANGE);
  attachInterrupt(digitalPinToInterrupt(encoder_B),encoderCount_B,CHANGE);

  Timer1.attachInterrupt(angularVelocity);
  Timer1.stop();
}

void loop(){
  digitalWrite(pwmPin, LOW);
  while(Serial.available()==0) {counter = 0;}
  sampleTime = 1000*Serial.parseInt();
  while(Serial.available()==0) {;}
  dataMax = Serial.parseInt();
  while(Serial.available()==0) {;}
  setPoint = Serial.parseInt();

  Timer1.initialize(sampleTime);
  digitalWrite(motor_A, LOW);
  digitalWrite(motor_B, HIGH);
  
  while(dataIndex<dataMax){;}
    
  Timer1.stop(); 
  digitalWrite(motor_B, LOW); 
  delay(20);
  Serial.read();
  dataIndex = 0;
  counter = 0;
}

void encoderCount_A(){
  counter++;
}

void encoderCount_B(){
  counter++;
}

void angularVelocity(){
  /* Velocity calculation*/
  Timer1.setPeriod(sampleTime); 
  double diffPos = M_PI*counter/1536;
  double vel = 1000000*(diffPos/sampleTime);

  /*Error*/
  double e = setPoint - vel; 
  
  /*PI controller*/
  double u = b0*e + b1*preError1 + b2*preError2 + preU;
  
  /* Anti-windup: Constrained control signal */
  u = constrain(u, lDo, lUp);

  /* PWM modification */
  if (u > 0){
      digitalWrite(motor_A, HIGH);
      digitalWrite(motor_B, LOW);
  }
  else{
      digitalWrite(motor_A, LOW);
      digitalWrite(motor_B, HIGH);
  }
  
  analogWrite(pwmPin, map(abs(u), 0, lUp, 0, 255));

  /* Data time shifting*/
  preError1 = e;
  preError2 = preError1;
  preU = u;
  
  /* Sending data */
  Serial.println(vel);
  counter = 0;
  dataIndex++;

}
