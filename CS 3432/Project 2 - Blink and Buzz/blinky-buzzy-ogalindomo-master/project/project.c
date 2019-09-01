#include <msp430.h>
#include <stdio.h>
#include "libTimer.h"
#include "ins.h"

#define LED_RED BIT0
#define LED_GREEN BIT6
#define LEDS (BIT0 | BIT6)
#define S1 BIT0
#define S2 BIT1
#define S3 BIT2
#define S4 BIT3
#define P2_SWITCHES (S1 | S2 | S3 | S4)

void screen_interrupt_handler();
void switch_init();
void led_init();
void switch_interrupt_handler();
void buzzer_init();
static char switch_update_interrupt_sense();
void led_update();
void buzzer_set_period(short cycles);
extern char update_allowed(char value);
char switch_state_down, switch_state_changed;
static short play_time_ms;
static char allowed;
static char music[];
static int i = 0;

int main(void)
{
  play_time_ms = -1;//Prevents the song of beign played.
  allowed = 0;//Variable allows to play music or not.
  configureClocks();//Sets clocks.
  /////Initialization of Elements///////
  buzzer_init();
  switch_init();
  led_init();
  /////////////////////////////////////
  enableWDTInterrupts();//Allows interrupts of the WDT.
  play_time_ms = 2000;//Amount of time the music[] will play.
  or_sr(0x18);//Turn off the GPU.
}

void buzzer_set_period(short cycles){
  CCR0 = cycles;//Cycle on.
  CCR1 = cycles >> 1;//Cycle off. 
}

void buzzer_init(){
  timerAUpmode();
  P2SEL2 &= ~(BIT6 | BIT7);
  P2SEL &= ~BIT7;
  P2SEL |= BIT6;
  P2DIR = BIT6;
}

void switch_init(){
  P2REN |= P2_SWITCHES;//REN is turned on.
  P2OUT |= P2_SWITCHES;//OUT is set to zero.
  P2DIR &= ~P2_SWITCHES;//DIR is set to zero.
  P2IE = P2_SWITCHES;//Interrupt is turned on.

  switch_update_interrupt_sense();
  led_update();
}

void led_init(){
  P1DIR |= LEDS;
  switch_state_changed = 1;
  led_update();
}

void led_update(){
  if(switch_state_changed) {
  char ledFlags = 0;

  ledFlags |= switch_state_down ? LED_RED : 0;
  ledFlags |= switch_state_down ? 0 : LED_GREEN;
  
  P1OUT &= (0xff - LEDS) | ledFlags;

  P1OUT |= (ledFlags);
  }
switch_state_changed = 0;
}

void
__interrupt_vec(PORT2_VECTOR) Port_2(){
  if(P2IFG & S1){
    P2IFG &= ~S1;
    screen_interrupt_handler();
  }
  
  else if(P2IFG & S2){
    void all_up();
    P2IFG &= ~S2;
    all_up();
  }
  
  else if(P2IFG & S3){
    void all_down();
    P2IFG &= ~S3;
    all_down();
  }
  
  else if(P2IFG & S4){
    P2IFG &= ~S4;
    P2IES |= (P2IN & S4);
    P2IES &= (P2IN | ~S4);
    play_time_ms = (2 * 250);//2 seconds * number of interrupts per second.
    i = 0;
    allowed = update_allowed(allowed);
  }
}

void __interrupt_vec(WDT_VECTOR) WDT(){
 if(play_time_ms > -1 && allowed){
   if(--play_time_ms == 0){
      buzzer_set_period(0);
      allowed = 0;
    }
    else if((play_time_ms % 50) == 0){
     void play();
     play();
    }
  }
}

void play(){
  static char sequence[10] = {160,170,180,190,200,210,220,230,240,250};//Frequencies to display.
  buzzer_set_period(sequence[i++]+90);//Plays the frequency.
  void leds();
  leds();//Turns on LEDS.
}

void leds(){
  P1OUT = LEDS;
  __delay_cycles(10000);//Allows dim of both lights.
  P1OUT &= ~LED_GREEN;
  __delay_cycles(10000);//Allows dim of the Red light.
  P1OUT &= ~LED_RED;
  __delay_cycles(10000);//Allows a period of time so that lights turn off.
}

void switch_interrupt_handler(){
  char p1val = switch_update_interrupt_sense();
  switch_state_down = (p1val & S1) ? 0 : 1;
  switch_state_changed = 1;
  led_update();
}

void screen_interrupt_handler(){
  char p2 = P2IN;
  P2IES |= (p2 & S1);
  P2IES &= (p2 | ~S1);
  switch_state_down = (p2 & S1) ? 0 : 1;
  switch_state_changed = 1;
  led_update();
}

void all_up(){ //Turns all lights off.
  char p2 = P2IN;
  P2IES |= (p2 & S2);
  P2IES |= (p2 | ~S2);
  char r = ~(p2 & S2);
  if(r){
    P1OUT |= LEDS;
  }
  else{
    P1OUT |= 0;
  }
}

void all_down(){
  char p2 = P2IN;//Turns all lights down.
  P2IES |= (p2 & S3);
  P2IES |= (p2 | ~S3);
  char r = ~(p2 & S3);
  if(r){
    P1OUT &= ~LEDS;
  }  
}

static char switch_update_interrupt_sense(){
  char p1val = P2IN;
  P1IES |= (p1val & S1);
  P1IES &= (p1val | ~S1);
  return p1val;
}
