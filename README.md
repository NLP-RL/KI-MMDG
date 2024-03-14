### Please create a new environment for the dependencies using the following command:

	conda create --name <env_name> --file requirements.txt

### Pre-processinng

  (a) First of all create train test data from the raw dataset: 
  
      python dataset_preparation.py
      
  (b) To process the knowledge graph: 
  
       python KG.py

### Model training and testing:
 
        python KI-MMDG.py

