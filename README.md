# SmartCheccBot
SmartCheccBot
  Objectives:
 Arrange according to questions, then our code checks first which question we are on. Then after the question has been determined, the code should loop through and find occurences of the intermediate steps and final answer solutions. These should be marked in such a way that once our iterator detects the characters unique to those steps the values can be stored in variables. The code then checks if the final answers and/or intermediate step values provided by the student and instructor match and gives feedback to the student.

PROPOSED DOCUMENTATION

SMART-CHECC DOCUMENTATION FOR INSTRUCTORS
Welcome to Smart-Checc. Smart-Checc is a system that creates an online environment in which a student and professor/instructor can exchange information and guidance on homework assignments. In many schools and universities, students who need feedback or guidance on homework problems don’t have immediate assistance and resort to the use of illegal materials such as homework solutions. Smart-checc makes it possible for the student to check his answers to problems algorithmically without directing looking at the final answer and steps. The student will not have any access to the answers but will receive feedback and guidance on what he/she is doing right or wrong in the process of obtaining a final answer to a question.
As an instructor your job is easy because our team of experts does all the work for you. When an instructor assigns homework or assignments, he/she must create a solution document to the answers. This document will be provided to our team and our algorithms will efficiently extract the solution data to each question together with any feedback the instructor intends to give. This system encourages personalized learning such that a student can know exactly what his/her areas of weakness are in solving problems.
INSTRUCTOR SOLUTION DOCUMENTATION
 The instructor needs to write the solution as a text file (save it as a text file) this can be done using NotePad or any suitable text editor. For every Question the instructor needs to start the solution with  <QQx> where x represents the number of the question. It is important to ensure that this is done correctly and never duplicated to avoid having two solutions to one question. 
For each intermediate step in the process of obtaining an answer, an instructor can provide values and a comment depending on whether a student gets it right or not. These solutions must be written before the final answer and must start with the code ISS ( intermediate step solution) followed by the variable of the intermediate step. For example (ISSL = 54 correct:good job obtaining the length, remember we need length to find area, wrong: you used the wrong length take another look at the diagram, make sure you don’t confuse breadth for length,  ISSW = 76 correct: good job finding the width, remember you need to get the width to find the length, wrong: you used the wrong length take another look at the diagram make sure you don’t confuse thickness and width see Shigley’s 1.1. Similarly, for the final answer the instructor has to start with the code FA (Final answer) followed by the variable of the final answer eg FAA = 4104 (Final answer area = 4104).This must be followed by correct and wrong answer feedback as for the intermediate solutions.
This format must be used for all question solutions the solution format is best explained in the table below:

<Qx>
ISSL = xxxx
Correct: Good this is correct Length
Wrong: Not the correct length
please check Shigley’s1.1 for the correct steps on finding length
ISSW = xxxx
Correc: Good this is correct
width
Wrong: Not the correct length
please check Shigley’s1.1 for the correct steps on finding length
FAA=xxxx
Correct:
Good you seem to understand how to find the area of a square    cross-section of a beam. Do consider this an idealisation, in the real world a beam may not be as geometrically precise.
Wrong: Please ensure you have the correct Length and width, remember, these multiply, not divide.

Instructors can repeat this format as many times as necessary.



Example: 
Original Question: 
Measure the sides of the rectangle below and calculate its area. 

Instructor’s text-file:
<Q1> ISSL = 4569 , correct:Good this is correct Length; wrong: Not the correct length please check Shigley's 1.1 for the correct steps on finding length; ISSW = 944; Correct Good ,you understand the use of width in finding the area of a square cross-section; wrong : please see shigley's for how to obtain correct dimensions; FAA = 4313136; correct: you found the right area!;wrong please ensure you have the correct values for length and width. These simply multiply

<Q2> ISSF = 500 , correct:Good this is correct Force; wrong: Not the correct Force please check Shigley's 3.1 for the correct steps on finding Force; ISSA = 90; Correct Good ,you understand the use of Area in finding the stress on a beam of a square cross-section; wrong : please see shigley's for how to obtain correct Area; FAStress = 45 000; correct: you found the right Stress! Do keep in mind that the axial force is not the only stress that we need to account for. in future we look at more stresses


(In this question if the value of A is wrong, the bot will give feedback on how to find A and when the student cannot figure it out then they can type “check previous parts” and it will prompt them for their values of L and W. If L and/or  W are correct it will say correct values and if not it will provide feedback on the values of L and W.)



