#makefile references
COMMON_OBJECTS =
CPU            = msp430g2553
CFLAGS         = -mmcu=${CPU} -Os -I../demos/h
LDFLAGS        = -L../demos/lib  -L/opt/ti/msp430_gcc/include/ -L/opt/ti/ms430_gcc/rtc.h
CC             = msp430-elf-gcc
AS             = msp430-elf-gcc -mmcu=${CPU} -c

all: clean load

main.elf:${COMMON_OBJECTS} main.c redraw.* buzzer.* randomizer.* 
	@${CC} ${CFLAGS} ${LDFLAGS} -o $@ $^ -lTimer -lLcd -lShape -lp2sw -lCircle

load: main.elf
	@mspdebug rf2500 "prog $^"

clean:
	@rm -f *.o *.elf
