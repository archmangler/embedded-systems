//Basic example ARM assembly file

			.syntax unified
			.cpu cortex-m4
			.fpu softvfp
			.thumb
			.section .text
			.globl __main
			.globl Reset_Handler

//Because we don't have this defined in a separate file
Reset_Handler:
				mov r1, #100
				mov r2, #126

__main:

			mov r5, #45
			mov r3, #45

			add r6,r5,r3

stop:
			b		stop
			.align
			.end

