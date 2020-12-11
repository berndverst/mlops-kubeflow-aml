# MLOps Workflow with Kubeflow and AML

This showcases a ML Ops workflow to go from Jupyter notebook to training in Kubeflow and deploying a trained model to Azure ML


## Initial File Structure

```
├── .gitignore               <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if 
│                               needed
├── conda_env.yml            <- Conda environment definition for ensuring consistent setup across environments
├── LICENSE
├── README.md                <- The top-level README for developers using this project.
├── requirements.txt         <- The requirements file for reproducing the analysis environment, e.g.
│                               generated with `pip freeze > requirements.txt`. Might not be needed if using conda.
├── setup.py                 <- Metadata about your project for easy distribution.
│
├── data
│   ├── interim_[desc]       <- Interim files - give these folders whatever name makes sense.
│   ├── processed            <- The final, canonical data sets for modeling.
│   ├── raw                  <- The original, immutable data dump.
│   ├── temp                 <- Temporary files.
│   └── training             <- Files relating to the training process
│
├── docs                     <- Documentation
│
├── extras                   <- Miscellaneous extras.
│
├── notebooks                <- Notebooks for analysis and testing
│
├── scripts                  <- Standalone scripts
│   ├── deploy               <- MLOps scripts for deployment (WIP)
│   │   └── score.py         <- Scoring script
│   ├── train                <- MLOps scripts for training
│   │   ├── submit-train.py  <- Script for submitting a training run to Azure ML Service
│   │   ├── submit-train-local.py <- Script for local training using Azure ML
│   │   └── train.py         <- Example training script using the iris dataset
│   ├── example.py           <- Example sctipt
│   └── MLOps.ipynb          <- End to end MLOps example (To be refactored into the above)
│
├── src                      <- Code for use in this project.
│   └── mlopsworkflowwithkubeflowandaml       <- Example python package - place shared code in such a package
│       ├── __init__.py      <- Python package initialisation
│       ├── examplemodule.py <- Example module with functions and naming / commenting best practices
│       ├── features.py      <- Feature engineering functionality
│       ├── io.py            <- IO functionality
│       └── pipeline.py      <- Pipeline functionality
│
└── tests                    <- Test cases (named after module)
    ├── test_notebook.py     <- Example testing that Jupyter notebooks run without errors
    └── mlopsworkflowwithkubeflowandaml       <- mlopsworkflowwithkubeflowandaml tests
        ├── examplemodule    <- examplemodule tests (1 file per method tested)
        ├── features         <- features tests
        ├── io               <- io tests
        └── pipeline         <- pipeline tests
```

## References
* http://docs.python-guide.org/en/latest/writing/structure/
* https://github.com/Azure/Microsoft-TDSP
* https://drivendata.github.io/cookiecutter-data-science/

