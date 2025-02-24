int redPin = 11;
int greenPin = 10;
int bluePin = 9;

void setup() {
  Serial.begin(9600);  // Start serial communication
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');  // Read incoming data
    int r, g, b;
    sscanf(input.c_str(), "%d,%d,%d", &r, &g, &b);  // Parse RGB values
    setColor(r, g, b);
  }
}

void setColor(int redValue, int greenValue, int blueValue) {
  analogWrite(redPin, redValue);
  analogWrite(greenPin, greenValue);
  analogWrite(bluePin, blueValue);
}
