# Predicting Avatar Movement in Virtual Reality to Increase Presence and Performance
![Starting Scene](https://github.com/Cele3x/practical-seminar/blob/master/submission/Images%20General/teaser.PNG)
This repository was used for the project "Predicting Avatar Movement in Virtual Reality to Increase Presence and Performance" carried out as part of the course "Praxisseminar" in the summer semester 2019 at the University of Regensburg. 
Furthermore, this repository will be used to submit the final product. 

For the actual submission only the folder __submission__ , found in the root directory of this repository, is relevant. The folder contains several subfolders, sorted alphabetically: 
- [Data Acquisiton Study](https://github.com/Cele3x/practical-seminar/tree/master/submission/Data%20Acquisiton%20Study)
- [Docs](https://github.com/Cele3x/practical-seminar/tree/master/submission/Docs)
- [Evaluation Study](https://github.com/Cele3x/practical-seminar/tree/master/submission/Evaluation%Study)
- [Images General](https://github.com/Cele3x/practical-seminar/tree/master/submission/Images%General)
- [Intercepter Client](https://github.com/Cele3x/practical-seminar/tree/master/submission/Intercepter%Client)
- [Latency Test Framework](https://github.com/Cele3x/practical-seminar/tree/master/submission/Latency%Test%Framework)
- [Neural Network](https://github.com/Cele3x/practical-seminar/tree/master/submission/Neural%Network)


Each subfolder will be described in the following, starting with __Data Acquisition Study__: 

## Data Acquisiton Study

This folder contains all the material needed and obtained for and during the data acquisiton study. It is structured as follows: 
- Demographics: Contains a list of the demographics of all study participants, as well as some information about whether they were wearing glasses or not. Additionally it contains information about previous experience in VR and sportiness of the participants. 
- Video: Showing one voluniteer participanting in the conducted acquisiton study. Consense to show the video was obtained. 


## Docs 

This folder comprises two subfolder with the following containment:
- Paper: Final version of the scientific paper written during the project. 
- Projekt Handbuch: This is a document which elabroates how to use the developed movement prediciton system. It, as well, explaines a bit more technical back ground compared to the presented paper above. Additonally it grants deeper insight in the developed and presented Latency Test Framework. 

## Evaluation Study 
## Image General
This folder contains all needed image for this repository, as well as all images needed for the paper and the "Projekt Handbuch". 
## Intercepter Client
This folder is used for the developed Intercepter Client and all its dependencies, its containment is structured as follows: 
- Folder 1
- Folder 2 
- Folder 3 
## Latency Test Framework
This folder contains everything needed to conduct the in the paper described latency tests. The content is organized as shown below:
- Arduino Sketches: The sketches used to run the LTF can be found here. There are two seperated folders, one containing the early test variant to establish a connection between an external computer and the Arduino. The second script is the actual script used to measure latency. It connects one digital sensor and one analog sensor, waits for the to trigger and sends the corresponding event to the connected external computer. 
- Python Scripts: This folder contains the script to obtain information from the arduino. This script gathers the two distinc timestamps received from the Arduino, compares them and prints a latency value to the console and a CSV file. 

## Neural Network 
