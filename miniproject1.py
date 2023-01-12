#!/usr/bin/env python3

print("Welcome to the computer quiz!")

playing = input("Do you want to play? " )


if playing.lower() != "yes":
    quit()

print("Okay, let's play!")
i = 0

answer = input("What does CPU stand for? " )
if answer.lower() == "central processing unit":
  print("Correct!")
  i += 1
else:
  print("Incorrect!")


  answer = input("What does GPU stand for? " )
if answer.lower() == "graphics processing unit":
  print("Correct!")
  i += 1
else:
  print("Incorrect!")


  answer = input("What does RAM stand for? " )
if answer.lower() == "random access memory":
  print("Correct!")
  i += 1
else:
  print("Incorrect!")


  answer = input("What does PSU stand for? " )
if answer.lower() == "power supply":
  print("Correct!")
  i += 1
else:
  print("Incorrect!")

print("You got " + str(i) + " questions correct!")
print("You got " + str((i / 4) * 100) + "%.")
