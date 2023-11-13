/*SENSADO DE VOLTAJE*/
const int voltaje = A2;
int sensorValue;
float vout;
float vin;

/* SENSADO DE CORRIENTE */
/* modelo de 30A == 66mV/A = 0.066 v/A */ 
float sensibilidad = 0.066; // s: [v/A]
/* v = I * s + 2.5 */
// despejando 
/* I = (v - 2.5)/s */
/* UMBRAL DE ENERGÍA */ 
int umbral = 7;

void setup() {
  pinMode(umbral,OUTPUT);
  Serial.begin(9600);
/* Establecemos la comunicación serial a 9600 baudios */
}

void loop() {
/* obtenemos la corriente promedio de 200 muestras  */
  sensorValue = analogRead(voltaje);
  float vin = obtener_voltaje(sensorValue, 0, 1023, 0.0, 25.0); 
  float I = obtener_corriente(200); 
  float Irms = I * 0.7071; 
  //float P = Irms * vin;
  Serial.print("Corriente: ");  Serial.print(Irms,5);     Serial.println("A ");
  Serial.print("Vrms: ");       Serial.print(vin,5);      Serial.println("V ");
  //Serial.print("Potencia: ");   Serial.print(P,5);        Serial.println("W ");
  delay(100); 
}
float obtener_voltaje(float x, float in_min, float in_max, float out_min, float out_max){
  float vsal = (x - in_min)*(out_max - out_min) / (in_max - in_min) + out_min;
  return(vsal); // Divisor de voltaje    
}
float obtener_corriente(int n_muestras)
{
  float voltajeSensor;
  float V0 = 2.460; //voltaje en OUT cuando la corriente a medir es 0A (varia de dispositivo a dispositivo)
  float corriente;
  float Imax = 0;
  float Imin = 0;
  for(int i=0;i<n_muestras;i++)
  {
   voltajeSensor = analogRead(A0) * (5.0 / 1023.0); //lectura del sensor    
   corriente=(0.9*corriente)+0.1*(voltajeSensor-V0)/sensibilidad; //Ecuación para obtener la corriente
  }
corriente=corriente/n_muestras;
return(corriente); 
}