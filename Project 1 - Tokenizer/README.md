Hello and Welcome to this tutorial.

To begin, we will list all the necessary files to run this creation.
1.interface.c -The piece of the code that reads what you input.

2.history.c and history.h -Which contain the implementation of the code that
keeps a record of what you input.

3.tokenizer.c and tokenizer.h -Which contain the implementation of the code
that divides the input into pieces the interface can display or use for
command purposes.

To compile, you will need to do the following:
1-. Run the following line in bash:
    gcc interface.c history.c history.h tokenizer.c tokenizer.h

2-. After the compilation is done the following command must be ran:
    ./a.out

3-. Alternatively you can allow the Makefile found in this repository to build
it for you. To do such thing just type make in the bash terminal and this
would erase the unnecessary files from your repository and allow you to run a
file called Emma.out to start the program- this program can be run just like
in step 2, but instead use "./Emma.out".

After running the previous commands the following will appear:
    * (The asterisk indicates the buffer is reading).

    The following commands can be run in this buffer:
    - get 1 (Gets the first entry in the history. The number must be greater or
    equal to 1).
    - history  (Displays the inputs the history has recorded).
    - Any string (e.g. Hello World) which will output back the sentence
    divided by parts, like:
    	    * Hello World
	    Hello
	    World

    -free which would allow you to terminate the execution. 

To exit: Combine C-x C-c and the buffer will stop and control will be given
back to the shell.

Thank You.
Oscar Galindo
2019

