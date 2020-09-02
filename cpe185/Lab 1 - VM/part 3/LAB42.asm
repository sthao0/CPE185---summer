Page 58,132
Title MASMLab
;************************
;* *
;* MASM Hello *
;* *
;************************
cseg segment 'code'
assume cs:cseg, ds:cseg, ss:cseg, es:cseg   //set up memory segment at cseg 

		org 100h //organize every data starting at 100h(in hex), by default, wihtout the h at the end its become a decimal #

start: 

	mov cx,10  //move 10 deciaml to cx
       mov ah,9		//move 9 to ah

again: mov dx, offset Hello    //offset mean, 
       int 21h
 	mov dx, offset Num_msg
 	int 21h
 	inc byte ptr Num_msg  		//byte ptr (byte pointer) incrementing by one, 
	mov bl, byte ptr Num_msg
	cmp bl, 3Ah			
	jge IncTen
back: 	loopne again //check if value is less than ever and jump to again again

done: mov ah, 4ch  // set to 4c in hex
 	int 21h

IncTen: mov dl,30h
	mov byte ptr Num_msg, dl
	inc byte ptr Tens_msg
	jmp back
	
	org 200h  //organize at 200 
 
Hello db "Hello World", 20h, 20h, "$"  //db data being inter in byte

Num_msg db 30h,13,10, 36   //handle it in byte
 
cseg ends
end start


/////////// things to try
mov cx,0
cx = 99
cx = 10
cx 04 // less then 10
cx = 11




mov cx,000A
mov ah, 09
mov dx, 0200
int 21
mov dx, 020E
int 21
inc byte ptr [020E]
loopnz 0105
mov byte ptr [020E],30
mov ah,4c
int 20