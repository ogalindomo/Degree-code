#include <msp430.h>
#include "buzzer.h"

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

void play(unsigned char pitch){
  buzzer_set_period(pitch);
}

