void setup() {
  Serial.begin(9600);
  Serial.println("start");
  for (int i = 0; i < 10; i++){
    Serial.println(i);
    delay(1000);
    }
  Serial.println("end");
}

void loop() {

}
