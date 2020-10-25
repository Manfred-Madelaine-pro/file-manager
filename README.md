# File Manager 

File manager to analyse, structure and classify documents and directories automatically.


## Main objectives / Driving goals / Leitmotiv

- Facilitate user's experience with files and directories management
	- Cleanning a dirty directory (only once or dynamically)
	- Listening to a directory for every updates and applying the cleaning
- Archiving files and scheduling zip
- Statistique sur l'état des données 
	- Plus vieux fichiers
	- Espace total 
	- ... 
- Collecting & sharing files with others 
	- Listening to different sources


## Dates

### Started 
Project pitched the 8th october 2020, and started the 22nd october 2020 

### Release date 
First expected release the friday 13th november 2020


## Tasks

### File Generator

- [x] Pick random file
- [x] Open file 
- [x] Read the content 
- [x] Pick random name
- [x] Keep file's first char 
- [x] Create a file named : {first char}_{random name} 
- [x] Save the name in the newly created file 


### Directory Generator

- [] Create random directories
- [] Create random files in those directories


### Structure Analyzer

- [x] Identify name and extension
- [x] Gather basic infos about each files
	- Name
	- Extension 
	- Date 
	- Size
	- Author (Official ?)
	- ...
- [x] Put the infos in a json  
- [x] Store data somewhere (flat file, db...)
- [x] Display result summary
- [] Provide some global stats
- [] Enhance the data gathered stats
- [] Create an ID (human readable or UUID ?)


### Structure Modifyer

- [] Get root, root's analyzed structure file, & filter action
- [] List possible filter actions
- [] Specify entries to ignore 
- [] 
- [] 


### Worker

- [] Input two Analized files : Initial & Final => défini les actions à faire
- [] Apply filter 
- [] 


### Global 

- [] Link every steps together and allow multiple filter flows (linking the steps) 
