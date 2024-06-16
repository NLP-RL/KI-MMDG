### Please create a new environment for the dependencies using the following command:

	conda create --name <env_name> --file requirements.txt
### Dataset
You can find the dataset [here](https://docs.google.com/spreadsheets/d/1iiE1Jat41-XQIFVit0KnJQM6BOpcq4SvsTxv4RZDrRw/edit?pli=1&gid=1462925978#gid=1462925978).
### Pre-processinng

  (a) First of all create train test data from the raw dataset: 
  
      python dataset_preparation.py
      
  (b) To process the knowledge graph: 
  
       python KG.py

### Model training and testing:
 
        python KI-MMDG.py

