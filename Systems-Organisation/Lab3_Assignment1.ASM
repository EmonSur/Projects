mov al, 00

movetoc0:
mov bl, F0

loop:
mov [bl], al
inc al
inc al
jz movetoc0
jmp loop
end
