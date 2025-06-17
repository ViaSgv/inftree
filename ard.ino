int pin_btn = 2;
int pin_led = 3;
int pin_pot = 0;

int val_btn_new, val_btn_old, val_pot;
bool stat_btn = true;

void setup() {
  pinMode(pin_btn, INPUT_PULLUP);
  pinMode(pin_led, OUTPUT);
  Serial.begin(9600);
  val_btn_old = 1;
}

void loop() {
  
  val_btn_new = digitalRead(pin_btn);

  if(val_btn_new != val_btn_old && val_btn_new == 1) {

    if(stat_btn) {
      Serial.println("start");
    }
    else {
      Serial.println("end");
    }

    stat_btn = !stat_btn;
    digitalWrite(pin_led, !stat_btn);

  }
  
  delay(100);
  val_btn_old = val_btn_new;

  if(!stat_btn) {
    val_pot = analogRead(pin_pot);
    Serial.println(val_pot);
  }

}