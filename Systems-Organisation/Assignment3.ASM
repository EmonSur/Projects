;read 2-digit numbers from keyboard and write them into the VDU until the user enters 99
start:
call 20
cmp al, 63 ; 63 in Hex is 99 in decimal
jz finish
call 40
jz start




org 20      ; read a 2-digit number and place result in al
in 00       ; get first digit from the keyboard

sub al, 30  ; convert the ASCII numeric character to integer
mul al, 0a  ;
push al
pop bl      ; save the al value in bl

in 00       ; get second digit
sub al, 30  ; ascii --> number
add al, bl


ret

org 40      ; write the value in al to the VDU
push al 
pop bl      ; save the al value in bl
div al, 0a  ; get the number of 10s in al
add al, 30  ; number --> ascii
mov [c0], al
mod bl, 0a
add bl, 30
mov [c1], bl

ret

finish:
end