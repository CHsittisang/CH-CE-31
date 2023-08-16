.data
    .balign 4
input: .asciz   "enter Input: "


    .balign 4
output: .asciz   "output: "

    .balign 4
message:    .asciz  "%c"

    .balign 4
data_small: .asciz  "gzvfuthsojlkdecnmrgpyxbaiw"

    .balign 4
data_large: .asciz  "GZVFUTHSOJLKDECNMRGPYXBAIW"

    .balign 4
return: .word 0

    .balign 4
scan_data:  .asciz ""

    .balign 4
scan_string:  .asciz "%s"

    .balign 4
next_line:  .asciz "\n"

    .text
    .global main
    .global printf
    .global scanf

return_data:
    ldrb    r1,[r4,r7] 
    pop     {r4-r12,lr}
    bx      lr


index_of_key:
    add r7,r7,#26
    b   return_data

if_equal:
    sub r7,r5,#5
    cmp r7,#0
    blt index_of_key
    b   return_data

while_loop:
    ldrb   r6,[r4,r5]
    cmp    r6,r0 
    beq     if_equal

    cmp     r2,#25
    add     r5,r5,#1
    ble     while_loop

encode:
    push    {r4-r12,lr}
    ldr    r4,=data_small
    mov     r5,#0
    b       while_loop

loop_input:
    ldr   r0,=scan_data
    ldrb    r0,[r0,r8]

    bl    encode

    cmp     r0,#0
    beq     exit
    cmp     r0,#32
    beq     exit

    ldr    r0,=message
    bl     printf

    add    r8,r8,#1
    b      loop_input


main:
    push {lr}

    ldr r0,=input
    bl  printf

    ldr r0,=scan_string
    ldr r1,=scan_data
    bl  scanf

    ldr r0,=output
    bl  printf

    mov r8,#0
    b   loop_input

exit:
    ldr     r0,=next_line
    bl      printf
    pop     {lr}
    bx      lr