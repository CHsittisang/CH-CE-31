    .data
.balign 4
input_num_f : .asciz "Enter the first number: "

.balign 4
input_num_s : .asciz "Enter the second number: "

.balign 4
out_add     : .asciz "addition: %d \n"

.balign 4
out_mul     : .asciz "multiplication: %d \n"

.balign 4
new_line    : .asciz "\n"

.balign 4
signed_num  : .asciz "%d"

.balign 4
scan_num_f   : .word 0
scan_num_s   : .word 0
soln_add    : .word 0
soln_mul    : .word 0

    .text
    .global main
    .global printf 
    .global scanf

main:
    ldr r0, =input_num_f
    bl printf

    ldr r0, =signed_num
    ldr r1, =scan_num_f
    bl scanf

    ldr r0, =new_line
    bl printf

    ldr r0, =input_num_s
    bl printf

    ldr r0, =signed_num
    ldr r1, =scan_num_s
    bl scanf

    ldr r0, =new_line
    bl printf

    b loop_soln

loop_soln:
    ldr r1 , =scan_num_f
    ldr r1 , [r1]
    ldr r2 , =scan_num_s
    ldr r2 , [r2]
    add r3 , r0 , r1

    ldr r1 , =scan_num_f
    ldr r1 , [r1]
    ldr r2 , =scan_num_s
    ldr r2 , [r2]
    mul r4 , r0 , r1

    ldr r5 , =soln_add
    str r3 , [r5]
    ldr r6 , =soln_mul
    str r4 , [r6]

    b exit

exit:
    ldr r0, =out_add
    bl printf

    ldr r0, =r3 
    bl printf

    ldr r0, =new_line
    bl printf

    ldr r0, =out_mul
    bl printf

    ldr r0, =r4
    bl printf

    ldr r0, =new_line
    bl printf

    mov r7, #1
    swi 0




