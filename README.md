# MLOps Workflow with Kubeflow and AML

This showcases a ML Ops workflow to go from Jupyter notebook to training in Kubeflow and deploying a trained model to Azure ML


## Initial File Structure

```
├── .gitignore               <- Files that should be ignored by git. Add seperate .gitignore files in sub folders if 
│                               needed
├── LICENSE
├── README.md                <- The top-level README for developers using this project.
├── data
│   ├── processed            <- The trained models
│   └── training             <- Data used for training
│
├── notebooks                <- Drop box for notebook used as pipeline input
│
├── code
│   ├── pipeline             <- The Kubeflow Pipelines definition
│   ├── train                <- MLOps scripts for training
│   ├── dataprep             <- MLOps scripts for training
│   └── processnotebook      <- Code for nbdev to extract code from notebook
│
├── scripts                  <- Misc scripts
```

## References
* http://docs.python-guide.org/en/latest/writing/structure/
* https://github.com/Azure/Microsoft-TDSP
* https://drivendata.github.io/cookiecutter-data-science/

