# :card_file_box: File Manager 

A file manager to analyse, structure and classify documents automatically.


## :trophy: Main objectives / Driving goals / Leitmotiv

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


## :spiral_calendar: Dates

### :rocket: Started 
Project pitched the _8th october 2020_, and started the _22nd october 2020_

### :dart: Release date 
First expected release the friday **13th november 2020** 


## :clipboard: Tasks

### File Generator

- [x] Pick random file
- [x] Open file 
- [x] Read the content 
- [x] Pick random name
- [x] Keep file's first char 
- [x] Create a file named : {first char}_{random name} 
- [x] Save the name in the newly created file 


### Directory Generator

- [ ] Create random directories
- [ ] Create random files in those directories


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
- [ ] Provide some global stats
- [ ] Enhance the data gathered stats
- [ ] Create an ID (human readable or UUID ?)


### Structure Modifyer

- [x] Get the list of files to store
- [x] Modify the files paths based on their creation dates
- [x] Modify the files paths based on their exts
- [x] Generate and save the json file in the right directory
- [ ] Specify entries to ignore

### Worker

- [ ] Input two Analized files : Initial & Final => défini les actions à faire
- [ ] Apply filter 


### Global 

- [ ] Link every steps together and allow multiple filter flows (linking the steps) 

### Automatic cleaning 

- [ ] Listen to a source directory and apply a cleaner automatically 