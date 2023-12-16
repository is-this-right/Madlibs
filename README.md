MAD LIBS Generator

USE CASE: Create stories based on user-input

Main Success Scenario:
* User "madlibs" are displayed

Precondition:
* User able to choose between pre-made madlib or D.I.Y.
* If D.I.Y., user must be able to create own sentences and specify how many "madlibs" are to be used

Functional Requirements:
* user input is stored and displayed

Flow:
* (INIT) Ask: pre-made or diy
* If pre-made:
    * iterate through MADLIB array
        * display description
        * take user input
        * store in ANSWER array
    * put Story and MADLIB together according to ORDER array
* If diy:
* (LOOP) Ask for type of next input: (e.g. MADLIB, Story, end)
    * If MADLIB:
        * ask for type
        * store in MADLIB array
        * LOOP
    * If Story: 
        * store in story
        * LOOP
    * If end: continue
* INIT


Initial Implementation:
* Uses the following methods:
    * Main
    * Template Creator
    * Madlib Assembly
* Main:
    * Assembles flow and logic of whole program
* Template Creator
    * must have recurring input reader
    * refer to diy in Flow
    * 