#define in1 13
#define in2 12
#define in3 8
#define in4 7
#define ENA 10
#define ENB 11

#include <stdio.h>
#include <string.h>

int potenciaA = 0;
int potenciaB = 0;
int dir = 0;
int contador = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  Serial.begin(9600);
}

void loop() {
 // Motor A HL --> Adelante
  if (Serial.available()>0){
    //input=Serial.read();
    potenciaA = Serial.parseInt();
    potenciaB = Serial.parseInt();
    dir = Serial.parseInt();
    
if (dir == 0){
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  analogWrite(ENA , potenciaA); 
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
  analogWrite(ENB , potenciaB); 
}
if (dir == 1){
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  analogWrite(ENA , potenciaA); 
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  analogWrite(ENB , potenciaB); 
}
if (dir == 2) {
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  analogWrite(ENA , potenciaA);  
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  analogWrite(ENB , potenciaB); 
}

if (dir == 3) {
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  analogWrite(ENA , potenciaA);  
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
  analogWrite(ENB , potenciaB); 
}
}}
