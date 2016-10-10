const int sensorPin = A0;    // select the input pin for the mic
const int speakerPin = 9;     // select output pin for speaker

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

int bias = 0.67/5.0;
float average = 0.67 / 3.3; //initial DC bias level
int sample;

void loop() {
  // put your main code here, to run repeatedly:
//bais = 5/1024 * .67;
sample = analogRead(sensorPin) - bias;
Serial.println(sample);
}
