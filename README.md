# Seeing Is Believing! towards Knowledge-Infused Multi-modal Medical Dialogue Generation (LREC-COLING 2024)
[PDF](https://aclanthology.org/2024.lrec-main.1264.pdf)


![Working](https://github.com/sbera7/KI-MMDG/blob/main/KI-MMDG_f-1.png)


This repository contains the official code and dataset for the paper "Knowledge-Infused Multi-Modal Medical Dialogue Generation (KI-MMDG)" which explores the integration of visual cues and medical knowledge in telemedicine for automatic disease diagnosis.


# Abstract
Over the last few years, artificial intelligence-based clinical assistance has gained immense popularity and demand in telemedicine, including automatic disease diagnosis. Patients often describe their signs and symptoms to doctors using visual aids, which provide vital evidence for identifying a medical condition. In addition to learning from our experiences, we learn from well established theories/ knowledge. With the motivation of leveraging visual cues and medical knowledge, we propose a transformer-based, knowledge-infused multi-modal medical dialogue generation (KI-MMDG) framework. In addition, we present a discourse-aware image identifier (DII) that recognizes signs and their severity by leveraging the current conversation context in addition to the image of the signs. We first curate an empathy and severity-aware multi-modal medical dialogue (ES-MMD) corpus in English, which is annotated with intent, symptoms, and visual signs with severity information. Experimental results show the superior performance of the proposed KI-MMDG model over uni-modal and non-knowledge infused generative models, demonstrating the importance of visual signs and knowledge infusion in symptom investigation and diagnosis. We also observed that the DII model surpasses the existing state-of-the-art model by 7.84%, indicating the crucial significance of dialogue context for identifying a sign image surfaced during conversations.

# Install the dependencies
```
git clone https://github.com/NLP-RL/KI-MMDG.git
cd KI-MMDG
conda create --name <env_name> --file requirements.txt
```
# Pre-processinng
(a) First, create train test data from the raw dataset: 
```
python dataset_preparation.py
```
(b) To process the knowledge graph: 
```  
python KG.py
```
# Model training and testing:
``` 
 python KI-MMDG.py
```
# Request Access to the ES-MMD Dataset

We provide the ES-MMD Dataset for research and academic purposes. To request access to the dataset, please follow the instructions below:

## How to Access the Dataset

1. **Fill Out the Request Form**: To access the ES-MMD Dataset, you need to submit a request through our [Google Form](https://forms.gle/C5q7jDprPGsCuYcD6).

2. **Review and Approval**: After submitting the form, your request will be reviewed. If approved, you will receive an email with a link to download the dataset.

3. **Terms of Use**: By requesting access, you agree to:
    - Use the dataset solely for non-commercial, educational, and research purposes.
    - Not use the dataset for any commercial activities.
    - Attribute the creators of this resource in any works (publications, presentations, or other public dissemination) utilizing the dataset.
    - Not disseminate the dataset without prior permission from the appropriate authorities.


# Citation
If you find this code useful in your research, please consider citing:
```
@inproceedings{tiwari-etal-2024-seeing,
    title = "Seeing Is Believing! towards Knowledge-Infused Multi-modal Medical Dialogue Generation",
    author = "Tiwari, Abhisek  and
      Bera, Shreyangshu  and
      Verma, Preeti  and
      Manthena, Jaithra Varma  and
      Saha, Sriparna  and
      Bhattacharyya, Pushpak  and
      Dhar, Minakshi  and
      Tiwari, Sarbajeet",
    editor = "Calzolari, Nicoletta  and
      Kan, Min-Yen  and
      Hoste, Veronique  and
      Lenci, Alessandro  and
      Sakti, Sakriani  and
      Xue, Nianwen",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italia",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.1264",
    pages = "14513--14523",
    abstract = "Over the last few years, artificial intelligence-based clinical assistance has gained immense popularity and demand in telemedicine, including automatic disease diagnosis. Patients often describe their signs and symptoms to doctors using visual aids, which provide vital evidence for identifying a medical condition. In addition to learning from our experiences, we learn from well-established theories/ knowledge. With the motivation of leveraging visual cues and medical knowledge, we propose a transformer-based, knowledge-infused multi-modal medical dialogue generation (KI-MMDG) framework. In addition, we present a discourse-aware image identifier (DII) that recognizes signs and their severity by leveraging the current conversation context in addition to the image of the signs. We first curate an empathy and severity-aware multi-modal medical dialogue (ES-MMD) corpus in English, which is annotated with intent, symptoms, and visual signs with severity information. Experimental results show the superior performance of the proposed KI-MMDG model over uni-modal and non-knowledge infused generative models, demonstrating the importance of visual signs and knowledge infusion in symptom investigation and diagnosis. We also observed that the DII model surpasses the existing state-of-the-art model by 7.84{\%}, indicating the crucial significance of dialogue context for identifying a sign image surfaced during conversations. The code and dataset are available at https://github.com/NLP-RL/KI-MMDG.",
}
```

