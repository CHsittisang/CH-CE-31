#include <stdio.h>
#include <time.h>

int main() {
    clock_t Run_time, Done_counting_time,Run_time2,Done_counting_time2;
    double total_time;
    double total_time2;
    int num = 1;
    int num2 = 1;
    int total_time_c = 0;
    int total_time_assm = 0;
    Run_time = clock();

    for (int i = 0; i < 100000000; i++) {
        num <<= 2;
        total = total + num * 2;
    }

    Done_counting_time = clock();

    total_time = (double)(Done_counting_time - Run_time) / CLOCKS_PER_SEC;
    printf("No of Instuction In C LANGUAGE : %d\n",total_time_c);
    printf("First Instuction Time Process : %ld\n", Run_time);
    printf("Last Instuction Time Process : %ld\n", Done_counting_time);
    printf("Total Process Time ( C LANGUAGE ) : %.3f seconds\n", total_time);


    Run_time2 = clock();

    for (int i = 0; i < 100000000; i++) {
        asm("lsl %[value], #2" : [value] "+r" (num2));
        total_time_assm = total_time_assm + num2 *2;
    }

    Done_counting_time2 = clock();

    total_time2 = (double)(Done_counting_time2 - Run_time2) / CLOCKS_PER_SEC;
    printf("No of Instuction In Assembly LANGUAGE : %d\n", total_time_assm);
    printf("First Instuction Time Process : %ld\n", Run_time2);
    printf("Last Instuction Time Process : %ld\n", Done_counting_time2);
    printf("Total Process Time ( Assembly LANGUAGE ) : %.3f seconds\n", total_time2);


    return 0;
}