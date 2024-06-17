### Please create a new environment for the dependencies using the following command:

	conda create --name <env_name> --file requirements.txt
### Dataset access
The dataset can be accessed from the [google drive](https://docs.google.com/spreadsheets/d/1iiE1Jat41-XQIFVit0KnJQM6BOpcq4SvsTxv4RZDrRw/edit?pli=1&gid=1462925978#gid=1462925978) and the images are available [here](https://drive.google.com/drive/folders/1xAhX-m79Ufi9Q1Z20-_8l-QxunnW-dTe).
### Pre-processinng

  (a) First of all create train test data from the raw dataset: 
  
      python dataset_preparation.py
      
  (b) To process the knowledge graph: 
  
       python KG.py

### Model training and testing:
 
        python KI-MMDG.py

