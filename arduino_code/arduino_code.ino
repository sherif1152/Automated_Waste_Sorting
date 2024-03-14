int redpiston = 7;
int greenpiston = 8;
int bluepiston = 9;
int motor1 = 11; 

 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
    pinMode(redpiston, OUTPUT);
  pinMode(greenpiston, OUTPUT);
  pinMode(bluepiston, OUTPUT);
  pinMode(motor1, OUTPUT); //direction+
  
}

void loop() {
   char command = Serial.read();

     digitalWrite(motor1,LOW );
     digitalWrite(redpiston, HIGH);
     digitalWrite(bluepiston, HIGH);
     digitalWrite(greenpiston, HIGH);
      
    if (command == 'P') {
      //Serial.println("Glass"); 
      delay(1000);
      digitalWrite(redpiston, LOW); 
      delay(1500); 
      digitalWrite(redpiston, HIGH);
      
      
    } 
    else if (command == 'G') { 
      Serial.println("plastic");
      delay(7000); 
      digitalWrite(bluepiston, LOW); 
      delay(1500); 
      digitalWrite(bluepiston, HIGH);
      
      
    } 
    else if (command == 'a') {
      //Serial.println("paper"); 
      delay(3700); 
      digitalWrite(greenpiston, LOW );
      delay(1500); 
      digitalWrite(greenpiston, HIGH);
      
      
   }
    
}
