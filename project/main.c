#include <msp430.h>
#include "libTimer.h"
#include "lcdutils.h"
#include "lcddraw.h"
#include "shape.h"
#include "abCircle.h"
#include "sr.h"
#include "lcdtypes.h"
#include "chordVec.h"
#include "special_shape.c"
#include "redraw.h"
#include "buzzer.h"
#include "stdlib.h"
#include "randomizer.h"

#define GREEN BIT6
#define COLS 128
#define ROWS 160

static unsigned char switch_mask;
static unsigned char switches_last_reported;
static unsigned char switches_current;
int play_time = 0;
u_char frequency = 0;
u_char redraw = 0;
int wins = 0;
//Direction Buttons//
#define S1 BIT0
#define S2 BIT1
#define S3 BIT2
#define S4 BIT3
/////////////////////

/////Declarations of Sprites in the game./////
AbRect first = {abRectGetBounds, abRectCheck, {10,10}};
AbRect background = {abRectGetBounds, abRectCheck, {COLS/2, ROWS/2}};
AbEye abeye = {abEyeGetBounds, abEyeCheck, {13,13}};
AbRectOutline fieldOutline = {abRectOutlineGetBounds, abRectOutlineCheck, {COLS/2 - 10, ROWS/2 - 10}};
Layer bg = {(AbShape*)&background, {COLS/2, ROWS/2}, {COLS/2,ROWS/2},{COLS/2,ROWS/2},COLOR_BLACK,0};
Layer eye_shape = {(AbShape*)&abeye, {COLS/2,ROWS/2}, {COLS/2,ROWS/2}, {COLS/2,ROWS/2}, COLOR_NAVY, 0};
Layer outline_box = {(AbShape*)&fieldOutline, {COLS/2, ROWS/2},{COLS/2,ROWS/2},{COLS/2,ROWS/2},COLOR_ORANGE, &eye_shape};
MovLayer outline = {&outline_box, {0,0}, 0};
MovLayer eye = {&eye_shape, {0,0}, 0};
u_int bgColor = COLOR_BLACK;
u_int game_started = 0;
//////////////////////////////////////////////

////Imported functions into the system.////
void p2sw_init(u_char mask);
static void switch_update_interrupt_sense();
extern void randomMovement();
extern void initialize(Layer* eye_shape);
//////////////////////////////////////////

////Game Variables////////////////////////
char* message1 ="Welcome!";
char* message2 = "I am Emma.";
char* message3 = "Press any button";
char* message4 = "to start.";
char* message_lost = "YOU LOST!";
char* win_message = "The Universe has";
char* win_message1 = "limits. You Don't.";
char* win_message2 = "Congratulations!!";
char* coord_x = "X:";
char* coord_y = "Y:";
char* win = "W:";
char choiceMade = 0;
char choice = 0;
char corrects = 0;
short random_seed = 0;
char won = 0;
char lost = 0;
char victory[] = {150,200,170,190};
int length_victory = 4;
//////////////////////////////////////////
  
int main (){
  P1DIR |= GREEN;
  P1OUT |= GREEN;
  configureClocks();
  lcd_init();
  buzzer_init();
  p2sw_init(15);
  enableWDTInterrupts();
  layerDraw(&bg);
  layerDraw(&outline_box);
  movLayerDraw(&eye, &eye_shape);
  int offset_x =  ROWS/4, offset_y = 3 * COLS/4;
  drawString5x7(offset_x,7+offset_y, message1,COLOR_WHITE,COLOR_BLACK);
  drawString5x7(offset_x,16+offset_y, message2,COLOR_WHITE,COLOR_BLACK);
  drawChar5x7(0,0,(choice + '0'), COLOR_WHITE, COLOR_BLACK);
  or_sr(0x8);
}

void __interrupt_vec(PORT2_VECTOR)Port_2(){
  static Region boundaries;
  if(P2IFG & S1){
    if(!won && !lost){
      P2IFG &= ~S1;
      and_sr(~8);
      eye.velocity.axes[0] = -4;
      eye.velocity.axes[1] = 0;
      layerGetBounds(&outline_box, &boundaries); 
      mlAdvance(&eye, &boundaries);
    }
    if(!game_started){
      and_sr(~8);
      layerDraw(&bg);
      layerDraw(&outline_box);
      movLayerDraw(&eye, &eye_shape);
      drawString5x7(0, ROWS-8, win, COLOR_WHITE, COLOR_BLACK);
      game_started = 1;
      or_sr(8);
    }
    else if(choice == 1){
      choiceMade = 0;
      corrects += 1;
    }
    else if(choice != 1 && !won && game_started)
    {
      lost = 1;
      and_sr(~8);
      drawString5x7(COLS/2, ROWS/2, message_lost, COLOR_RED, COLOR_BLACK);
    }
    if(corrects == 20){
      won = 1;
      drawString5x7(15, 3* COLS/4, win_message, COLOR_GREEN, COLOR_BLACK);
      drawString5x7(15, (3 * COLS/4)+8, win_message1, COLOR_GREEN, COLOR_BLACK);
      drawString5x7(15, (3* COLS/4)+16, win_message2, COLOR_GREEN, COLOR_BLACK);
    }
    or_sr(8);
    play_time = 10;
    frequency = 180;
  }
  else if(P2IFG & S2){
    if(!won && !lost){
      P2IFG &= ~S2;
      and_sr(~8);
      eye.velocity.axes[1] = 4;
      eye.velocity.axes[0] = 0;
      layerGetBounds(&outline_box, &boundaries);
      mlAdvance(&eye, &boundaries);
    }
    if(!game_started){
      and_sr(~8);
      layerDraw(&bg);
      layerDraw(&outline_box);
      movLayerDraw(&eye, &eye_shape);
      drawString5x7(0, ROWS-8, win, COLOR_WHITE, COLOR_BLACK);
      game_started = 1;
      or_sr(8);
    }
    else if(choice == 2){
      choiceMade = 0;
      corrects += 1;
    }
    else if(choice != 2 && !won && game_started)
    {
      lost = 1;
      and_sr(~8);
      drawString5x7(COLS/2, ROWS/2, message_lost, COLOR_RED, COLOR_BLACK);
    }
    if(corrects == 20){
      won = 1;
      drawString5x7(15, 3* COLS/4, win_message, COLOR_GREEN, COLOR_BLACK);
      drawString5x7(15, (3 * COLS/4)+8, win_message1, COLOR_GREEN, COLOR_BLACK);
      drawString5x7(15, (3* COLS/4)+16, win_message2, COLOR_GREEN, COLOR_BLACK);
    }
    or_sr(8);
    play_time = 10;
    frequency = 190;
  }
  else if(P2IFG & S3){
    if(!won && !lost){
      P2IFG &= ~S3;
      and_sr(~8);
      eye.velocity.axes[1] = -4;
      eye.velocity.axes[0] = 0;
      layerGetBounds(&outline_box, &boundaries);
      mlAdvance(&eye, &boundaries);
    }
    if(!game_started){
      and_sr(~8);
      layerDraw(&bg);
      layerDraw(&outline_box);
      movLayerDraw(&eye, &eye_shape);
      game_started = 1;
      or_sr(8);
    }
    else if(choice == 3){
      eye_shape.color = COLOR_GREEN;
      choiceMade = 0;
      corrects+=1;
    }
    else if(choice != 3 && !won && game_started)
    {
      lost = 1;
      drawString5x7(COLS/2, ROWS/2, message_lost, COLOR_RED, COLOR_BLACK);
    }
    if(corrects == 20){
      won = 1;
      drawString5x7(15, 3* COLS/4, win_message, COLOR_GREEN, COLOR_BLACK);
      drawString5x7(15, (3 * COLS/4)+8, win_message1, COLOR_GREEN, COLOR_BLACK);
      drawString5x7(15, (3* COLS/4)+16, win_message2, COLOR_GREEN, COLOR_BLACK);
    }
    or_sr(8);
    play_time = 10;
    frequency = 200;
  }
  else if(P2IFG & S4){
    if(!won && !lost){
      P2IFG &= ~S4;
      and_sr(~8);
      eye.velocity.axes[1] = 0;
      eye.velocity.axes[0] = 4;
      layerGetBounds(&outline_box, &boundaries);
      mlAdvance(&eye, &boundaries);
    }
    if(!game_started){
      and_sr(~8);
      layerDraw(&bg);
      layerDraw(&outline_box);
      movLayerDraw(&eye, &eye_shape);
      game_started = 1;
      or_sr(8);
    }
    else if(choice == 4){
      choiceMade = 0;
      corrects+=1;
    }
    else if(choice != 4 && !won && game_started)
    {
      lost = 1;
      drawString5x7(COLS/2, ROWS/2, message_lost, COLOR_RED, COLOR_BLACK);
    }
    if(corrects == 20){
      won = 1;
      drawString5x7(15, 3* COLS/4, win_message, COLOR_GREEN, COLOR_BLACK);
      drawString5x7(15, (3 * COLS/4)+8, win_message1, COLOR_GREEN, COLOR_BLACK);
      drawString5x7(15, (3* COLS/4)+16, win_message2, COLOR_GREEN, COLOR_BLACK);
    }
    or_sr(8);
    play_time = 10;
    frequency = 210;
  }
}

void __interrupt_vec(WDT_VECTOR) WDT(){
  void wdt_c_handler();
  static short count = 0;
  count+=1;
  
  if(!choiceMade){
    and_sr(~8);
    choice = (count%4) + 1;
    drawChar5x7(0,0,(choice + '0'), COLOR_WHITE, COLOR_BLACK);
    drawChar5x7(0,0,(choice + '0'), COLOR_WHITE, COLOR_BLACK);
    choiceMade = 1;
    or_sr(8);
  }
  
  if(count == 50 && !lost && !won){
    drawChar5x7(0,0,(choice + '0'), COLOR_WHITE, COLOR_BLACK);
    count = 0;
    wdt_c_handler();  
  }
 
  if(play_time > 0){
    if(--play_time == 0){
      play_time = 0;
      play(0);
    }
    else{
      play(frequency);
      play_time;
    }
  }
}

void wdt_c_handler(){
    if(!game_started)
      initialize(&eye_shape);
    else
      eye_shape.color = (eye_shape.color+0xdeaf) % 0xffff;
    redraw = 0;
    static char drawn = 0;
    movLayerDraw(&eye, &eye_shape);
    Region bounds;
    drawString5x7(0,ROWS-8,win, COLOR_WHITE, COLOR_BLACK);
    drawChar5x7(10,ROWS-8,corrects/10 + '0', COLOR_WHITE, COLOR_BLACK);
    drawChar5x7(15,ROWS-8,corrects%10 + '0', COLOR_WHITE, COLOR_BLACK);
    layerGetBounds(&eye_shape, &bounds);
    drawString5x7(35,ROWS-8,coord_x, COLOR_WHITE, COLOR_BLACK);
    drawString5x7(65,ROWS-8,coord_y, COLOR_WHITE, COLOR_BLACK);
    
    int center_x = (bounds.botRight.axes[0] + ((bounds.botRight.axes[0]-bounds.topLeft.axes[0])/2));
    int center_y = (bounds.topLeft.axes[1] + ((bounds.botRight.axes[1]-bounds.topLeft.axes[1])/2));
    
    drawChar5x7(45,ROWS-8,((center_x/100) + '0'), COLOR_WHITE, COLOR_BLACK);
    drawChar5x7(50,ROWS-8,((center_x-(center_x/100)*100)/10) + '0', COLOR_WHITE, COLOR_BLACK);
    drawChar5x7(55,ROWS-8, center_x%10 + '0', COLOR_WHITE, COLOR_BLACK);

    drawChar5x7(75,ROWS-8,((center_y/100) + '0'), COLOR_WHITE, COLOR_BLACK);
    drawChar5x7(80,ROWS-8,((center_y-(center_y/100)*100)/10) + '0', COLOR_WHITE, COLOR_BLACK);
    drawChar5x7(85,ROWS-8, center_y%10 + '0', COLOR_WHITE, COLOR_BLACK);
    
    if(!game_started){
      int offset_x =  ROWS/8, offset_y = 3 * COLS/4;
      drawString5x7(offset_x-3,28+offset_y, message3, eye_shape.color, COLOR_BLACK);
      drawString5x7(2 * offset_x,39+offset_y, message4, eye_shape.color, COLOR_BLACK);
    }
    else if(game_started){
      char* game_started = "Guess N,E,W,S.";
      drawString5x7(25, 2, game_started,COLOR_WHITE, COLOR_BLACK);
    }
}
  
static void
switch_update_interrupt_sense()
{
  switches_current = P2IN & switch_mask;
  /* update switch interrupt to detect changes from current buttons */
  P2IES |= (switches_current);  /* if switch up, sense down */
  P2IES &= (switches_current | ~switch_mask); /* if switch down, sense up */
}

void
p2sw_init(unsigned char mask)
{
  switch_mask = mask;
  P2REN |= mask;    /* enables resistors for switches */
  P2IE = mask;      /* enable interrupts from switches */
  P2OUT |= mask;    /* pull-ups for switches */
  P2DIR &= ~mask;   /* set switches' bits for input */

  switch_update_interrupt_sense();
} 
