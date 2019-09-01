all: say_hello clean compile

say_hello:
	@echo "Hello User, I am cleanning your mess and compiling your good ideas."

compile:interface.c tokenizer.c tokenizer.h history.c history.h
	@$gcc interface.c tokenizer.c tokenizer.h history.c history.h -o Emma.out

clean:interface.c tokenizer.c tokenizer.h history.c history.h README.md Makefile
	@find . ! -name interface.c ! -name tokenizer.c ! -name tokenizer.h ! -name history.c ! -name history.h ! -name Makefile ! -name README.md ! -name tester.c ! -name test.c -type f -delete
