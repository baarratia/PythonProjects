#define in1 13
#define in2 12
#define in3 8
#define in4 7
#define ENA 10
#define ENB 11
int input;
int potenciaA = 75;
int potenciaB = 75;
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
 
    input=Serial.read();

 //avanzar w
    if (input=='w'){
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  analogWrite(ENA , potenciaA);  
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
  analogWrite(ENB , potenciaB); 
  }

 //retroceder : s
 if (input=='s'){
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  analogWrite(ENA , potenciaA); 
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  analogWrite(ENB , potenciaB); 
}
//giro derehca: d
if (input=='a') {
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  analogWrite(ENA , potenciaA);  
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  analogWrite(ENB , potenciaB); 
}
//giro izquierda: a
if (input=='d') {
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  analogWrite(ENA , potenciaA);  
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
  analogWrite(ENB , potenciaB); 
}
//frenar: q
if (input=='q') {
  analogWrite(ENB , 0);
  analogWrite(ENA , 0);
}
//subirVel : + 
if (input=='+'){
  if (potenciaA < 240)
  {
    potenciaA += 20;
    potenciaB += 20;
  }
}
if (input=='-'){
  if (potenciaA > 80)
  {
    potenciaA -= 20;
    potenciaB -= 20;
  }
}
}
}
