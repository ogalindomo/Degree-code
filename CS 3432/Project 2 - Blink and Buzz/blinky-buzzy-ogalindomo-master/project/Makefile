#makefile references
COMMON_OBJECTS =
CPU	       = msp430g2553
CFLAGS         = -mmcu=${CPU}  -I../demos/h
LDFLAGS        = -L/opt/ti/msp430_gcc/include

#switch for compilers
CC             = msp430-elf-gcc
AS             = msp430-elf-as

all: project.elf load

#additional rules
project.elf: ${COMMON_OBJECTS} project.c ins.h ins.s ../demos/lib/libTimer.a
	@${CC} $^ ${CFLAGS} ${LDFLAGS} -o $@

load: project.elf
	mspdebug rf2500 "prog project.elf"
