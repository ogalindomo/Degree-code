#ifndef sound_module
#define sound_module
#include "libTimer.h"

void buzzer_set_period(short cycles);
void buzzer_init();
void play(unsigned char pitch);

#endif
