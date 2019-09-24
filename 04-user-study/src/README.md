# User Study

This Unity application was developed for the user study for predicting body movements. The participant is virtually placed via OptiTracks motion capturing system and an HTC Vive as head mounted device in a scene similar to the real surroundings where the study takes place. Via external adjustments the motion captured body movements are getting intercepted, changed and projected on the participants virtual model based on different prediction values.

The application can be subdivided into three main purposes:

### Body Visualization

At start the participant is located without any configuration in a replica of the studio. The different body movement predictions and their effects can be experienced while moving freely or by predefined tasks.

### Evaluating Self-Perception

After some time where the participant could adjust itself to the altered movement predictions a questionnaire can be enabled externally for evaluating made experiences. 

The questionnaire is segmented into two contentual parts with the first part being questions from the IPQ questionnaire and and secondly questions regarding limb ownership. The questions from each segment are randomly sorted each time the questionnaire is getting started while the segment order remains static.

The questionnaire can be started by "touching" the virtually placed start button. After selection of one of the five offered answer options a forward button is displayed until no questions remain where the questionnaire is disabled again automatically.

### Performance Task

For this task the two whiteboards have to be enabled in the scene externally while placing the real world equivalents at the predefined same positions. While the participant touches virtually and in reality each whiteboard in alternation for a specific time the repetitions are getting counted and recorded by the study master.

# Usage

The starting scene configuration should be with
* the **questionnaire** object being **disabled**,
* the **whiteboards outside** the marked area **enabled** and
* the **whiteboards inside** the marked area **disabled**. 

Before the study can be conducted and the scene started a participant id has to be specified for being able to associate results to a participant:
> IMAGE

During the study 
* the **questionnaire** object has to be **enabled** when needed (disabled automatically) and
* the **whiteboard** objects switched in its availibility status for the performance task.

# Results

> where to find and how to read results
