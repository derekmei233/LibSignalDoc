# Start

## Run Model Pipline

Our library has a uniform structure that empowers users to start their experiments with just one click. Users can start an experiment by setting arguments in the run.py file and start with their customized settings. The following part is the arguments provided to customize.

```
python run.py
```

Supporing parameters:

- <font color=red> thread_num:  </font> number of threads for cityflow simulation

- <font color=red> ngpu:  </font> how many gpu resources used in this experiment

- <font color=red> task:  </font> task type to run

- <font color=red> agent:  </font> agent type of agents in RL environment

- <font color=red> world:  </font> simulator type

- <font color=red> dataset:  </font> type of dataset in training process

- <font color=red> path:  </font> path to configuration file

- <font color=red> prefix:  </font> the number of predix in this running process

- <font color=red> seed:  </font> seed for pytorch backend
