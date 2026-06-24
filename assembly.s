
.global mainthree
    mainthree:
        movl $4, %eax
        neg %eax
        cmpl $0, %eax
        movl $0, %eax 
        sete %al
        ret