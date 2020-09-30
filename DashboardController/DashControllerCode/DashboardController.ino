#include <CAN.h>
#include <FastLED.h>
#define LED_TYPE    WS2811
#define NUM_LEDS 16
//#define BRIGHTNESS  96
#define DATA_PIN    3
#define COLOR_ORDER GRB

uint8_t convertRPM(uint16_t);
void  rpmToLight(uint8_t, bool);

CRGB leds[NUM_LEDS];
const CRGB default_colors[16] = {CRGB::Green, CRGB::Green, CRGB::Green, CRGB::Green,CRGB::Green, CRGB::Green, CRGB::Red,CRGB::Red,CRGB::Red,CRGB::Red,CRGB::Red,CRGB::Blue,CRGB::Blue,CRGB::Blue,CRGB::Blue,CRGB::Blue};

uint16_t brightness = 50;
uint16_t rpm = 0;         //0x640 Engine speed        (16 bits->0-15)   Unsigned 1 rpm resolution.
uint8_t coolant_temp = 0; //0x649 Coolant Temperature (8 bits -> 0-7)   Unsigned 1C resolution with 40C offset // when it reaches 130C car will shut down!!!
uint16_t oil_pressure = 0; //0x644 Engine oil pressure (16bits -> 48-63) Unsigned 0.1kPa
uint8_t gear =0;          //0x64D Gear                (4 bits -> 52-55) Signed Unknown resolution (believe is 1 to 1)

uint8_t prevGear = 0;



void setup() {
    Serial.begin(115200);
    while (!Serial);

    // start the CAN bus at 500 kbps
    if (!CAN.begin(500E3)) {
      Serial.println("Starting CAN failed!");
      while (1);
    }
    //Cycle through gears.  
    /*for (int i = 0; i < 6; i++){
      Serial.write(i);
      delay(500);
    }*/

    /*for (uint8_t i = 0; i < 16; i++){
      for (uint8_t j=0; j < 16; j++){
        if ( j <= i){
            leds[j] = default_colors[j];
        }else{
            leds[j] = CRGB::Black;
        }
      }
      FastLED.show();
      delay(100);
    }*/

    //all red:
    /*for (uint8_t j=0; j < 16; j++){
        leds[j] = CRGB::Red;
    }*/
    
    
    //attach CAN interrupt to onReceive function
    CAN.onReceive(onReceive);
    FastLED.addLeds<LED_TYPE,DATA_PIN,COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
    FastLED.setBrightness(brightness);
}

void loop() {
  // put your main code here, to run repeatedly:
    if (gear != prevGear){ //check if gear changed.
         // Serial.write(gear);  //Sends gear to gear controller
         // Serial.print(gear);
          prevGear = gear;              
  }
  Serial.println(rpm);
  convertRPM(rpm);
  delay (50);
}

uint8_t convertRPM(uint16_t rpmVal){
      if (rpmVal < 6500){ // if < 6500 0 lights
        rpmToLight(0, false);
      }else if(rpmVal > 11000){ //if > 11000 all red
        rpmToLight(16, true);
      }else{
        rpmToLight((uint8_t)map(rpmVal, 0, 11500, 0, 16), false); //linear function converts values from rpm range (0-11500) to n LEDs (0-16)
      }
}

void  rpmToLight(uint8_t numLeds, bool shift){
  if (numLeds >= 0 and numLeds <= 16){
      for (uint8_t i=0; i < 16; i++){
        if ( i <= numLeds and numLeds != 0){
            if (!shift){leds[i] = default_colors[i];}else{leds[i] = CRGB::Red;}
        }else{
            leds[i] = CRGB::Black;
        }
    }
  }
  FastLED.show();
}

void onReceive(int packetSize){

    uint8_t data [8] = {0,0,0,0,0,0,0,0};
    uint8_t index = 0;

    while (CAN.available()) {
        if (index < 8)// <-prevents buffer overflow
          data[index] = CAN.read();
        index++;
    }
     
  switch (CAN.packetId()){
    case 0x640:
              rpm = (data[0] <<8 | data[1]);
              //convertRPM(rpm);
              break;
    case 0x649:
              coolant_temp = data[0] - 40;
              break;
    case 0x644:
              oil_pressure = (data[6] <<8 | data[7]); //todo convert from whatever units the sensor is giving
              break;
    case 0x64D:
              gear = (data[6] & 0b00001111);
              //Serial.println(gear);
              break;
    default:  //nothing
              break;
  }
/*  
Serial.print ("RPM: ");
Serial.println (rpm);
Serial.print ("Coolant: ");
Serial.println (coolant_temp);
Serial.print ("oil: ");
Serial.println (oil_pressure);
Serial.print ("gear: ");
Serial.println (gear);*/
  
}
