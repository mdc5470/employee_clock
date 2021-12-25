/**
 * --------------------------------------------------------------------------------------------------------------------
 * Example sketch/program showing how to read data from more than one PICC to serial.
 * --------------------------------------------------------------------------------------------------------------------
 * This is a MFRC522 library example; for further details and other examples see: https://github.com/miguelbalboa/rfid
 *
 * Example sketch/program showing how to read data from more than one PICC (that is: a RFID Tag or Card) using a
 * MFRC522 based RFID Reader on the Arduino SPI interface.
 *
 * Warning: This may not work! Multiple devices at one SPI are difficult and cause many trouble!! Engineering skill
 *          and knowledge are required!
 *
 * @license Released into the public domain.
 *
 * Typical pin layout used:
 * -----------------------------------------------------------------------------------------
 *             MFRC522      Arduino       Arduino   Arduino    Arduino          Arduino
 *             Reader/PCD   Uno/101       Mega      Nano v3    Leonardo/Micro   Pro Micro
 * Signal      Pin          Pin           Pin       Pin        Pin              Pin
 * -----------------------------------------------------------------------------------------
 * RST/Reset   RST          9             5         D9         RESET/ICSP-5     RST
 * SPI SS 1    SDA(SS)      ** custom, take a unused pin, only HIGH/LOW required **
 * SPI SS 2    SDA(SS)      ** custom, take a unused pin, only HIGH/LOW required **
 * SPI MOSI    MOSI         11 / ICSP-4   51        D11        ICSP-4           16
 * SPI MISO    MISO         12 / ICSP-1   50        D12        ICSP-1           14
 * SPI SCK     SCK          13 / ICSP-3   52        D13        ICSP-3           15
 *
 */

/*
A4  LCD SDA Pin
A5  LCD SCL Pin

8 SDA Reader 1
9 RST for SPI
10 SDA for reader 0
11 MOSI
12 MISO
13 SCK



*/




#include <Firmata.h>
#include <SPI.h>
#include <MFRC522.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_1_PIN        10         // Configurable, take a unused pin, only HIGH/LOW required, must be diffrent to SS 2
#define SS_2_PIN        8          // Configurable, take a unused pin, only HIGH/LOW required, must be diffrent to SS 1
#define NR_OF_READERS   1

byte ssPins[] = {SS_1_PIN, SS_2_PIN};

LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 20 chars and 4 line display
MFRC522 mfrc522[NR_OF_READERS];   // Create MFRC522 instance.

/**
 * Initialize.
 */
int lastLine = 1;

void stringDataCallback(char *stringData){
   if ( lastLine ) {
     lastLine = 0;
     
     lcd.clear();
   } else {
     lastLine = 1;
     lcd.setCursor(0,1);
   }
   lcd.print(stringData);
}
/*Go through this when it gets restarted on the command.*/
void setup() {
  
  {
  lcd.init();                      // initialize the lcd
  // Print a message to the LCD.
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Rossell");
  lcd.setCursor(0,1);
  lcd.print("Automation");
   lcd.setCursor(0,2);
  lcd.print("                    ");
   lcd.setCursor(0,3);
  lcd.print("                    ");

 
}
/*
  lcd.init();
  lcd.backlight();
  Firmata.setFirmwareVersion( FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION );
  Firmata.attach( STRING_DATA, stringDataCallback);
  Firmata.begin();  
*/
  Serial.begin(9600); // Initialize serial communications with the PC
  while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)

  SPI.begin();        // Init SPI bus

  for (uint8_t reader = 0; reader < NR_OF_READERS; reader++) {
    mfrc522[reader].PCD_Init(ssPins[reader], RST_PIN); // Init each MFRC522 card
    // Enhance the MFRC522 Receiver Gain to maximum value of some 48 dB
    mfrc522[reader].PCD_SetAntennaGain(mfrc522[reader].RxGain_max);
    //Serial.print(F("Reader "));
    //Serial.print(reader);
    //Serial.print(F(": "));
    //mfrc522[reader].PCD_DumpVersionToSerial();
 
}
  delay(5000);

  lcd.clear();
  lcd.print("Please Scan Your");
  lcd.setCursor(0,1);
  lcd.print("Badge");
}

/**
 * Main loop.
 */
void loop() {

  /*while ( Firmata.available() ) {
    Firmata.processInput();
  }*/
/*while (!Serial.available()){
  lcd.clear();
  lcd.print("Please Scan Your");
  lcd.setCursor(0,1);
  lcd.print("Badge");
*/
 
  for (uint8_t reader = 0; reader < NR_OF_READERS; reader++) {
    // Look for new cards

    if (mfrc522[reader].PICC_IsNewCardPresent() && mfrc522[reader].PICC_ReadCardSerial()) {
      //Serial.print(F("Reader "));
      Serial.print(reader);
      // Show some details of the PICC (that is: the tag/card)
      //Serial.print(F(": Card UID:"));
      dump_byte_array(mfrc522[reader].uid.uidByte, mfrc522[reader].uid.size);
      Serial.println();
      //Serial.print(F("PICC type: "));nb
      //MFRC522::PICC_Type piccType = mfrc522[reader].PICC_GetType(mfrc522[reader].uid.sak);
      //Serial.println(mfrc522[reader].PICC_GetTypeName(piccType));

      // Halt PICC
      mfrc522[reader].PICC_HaltA();
      // Stop encryption on PCD
      mfrc522[reader].PCD_StopCrypto1();
    } //if (mfrc522[reader].PICC_IsNewC
  } //for(uint8_t reader
  String t_f = "";
  char x;
if (Serial.available()){  
  
  lcd.clear();
  while (Serial.available()){
    
    x = Serial.read();
    t_f = String(x);
    /*lcd.print(x);*/
  }
    if (t_f == "T"){
      Serial.end();
      Serial.begin(9600);
      delay(500);
      lcd.clear();
      if (Serial.available()){
        lcd.clear();
        lcd.print("Welcome");
        lcd.setCursor(0,1);
      while (Serial.available()){
      x = Serial.read();
      lcd.print(x);
      }
      }
    }
    else if (t_f == "F") {
      Serial.end();
      Serial.begin(9600);
      delay(500);
      lcd.clear();
      lcd.print("Please use computer");
      lcd.setCursor(0,1);
      lcd.print("to enter name");
      delay(5000);
      if (Serial.available()){
        lcd.clear();
      while (Serial.available()){
        x = Serial.read();
        lcd.print(x);
      }
      delay(1000);
      }
    
    }
  delay(5000);
  lcd.clear();
  lcd.print("Please Scan Your");
  lcd.setCursor(0,1);
  lcd.print("Badge");
  }
 
}

/**
 * Helper routine to dump a byte array as hex values to Serial.
 */
void dump_byte_array(byte *buffer, byte bufferSize) {
  for (byte i = 0; i < bufferSize; i++) {
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.print(buffer[i], HEX);
  }
}
