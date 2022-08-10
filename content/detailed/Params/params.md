# Params
## Params of Env Simulator
This will introduce the details about environmental simulators' Parameters 
#### CityFlow Config File
Referred from: https://cityflow.readthedocs.io/en/latest/start.html#data-access-api
```
{
  "interval": 1.0,
  "seed": 0,
  "dir": "data/",
  "roadnetFile": "cityflow_1x1/roadnet.json",
  "flowFile": "cityflow_1x1/flow.json",
  "rlTrafficLight": true,
  "saveReplay": false,
  "roadnetLogFile": "cityflow_1x1/replay/2022_07_19-09_28_40.json",
  "replayLogFile": "cityflow_1x1/replay/2022_07_19-09_28_40.txt"
}
```

- interval: time of each simulation step (in seconds).
- seed: random seed.
- dir: root directory, all file path will be relative to this directory.
- roadnetFile: path for roadnet file.
- flowFile: path for flow file. 
- rlTrafficLight: whether to enable traffic light control through python API. If set to `false`, default traffic light plan defined in `roadnetFile` will be used.
- saveReplay: whether to save simulation for replay. If set to `true`, `roadnetLogFile` and `replayLogFile` are required.
- roadnetLogFile: path for roadnet replay file. This is a special roadnet file for replay, not the same as `roadnetFile`.
- replayLogFile: path for replay. This file contains vehicle positions and traffic light situation of each simulation step.

#### SUMO Config File

```
{
  "interval": 1.0,
  "seed": 0,
  "dir": "data/",
  "combined_file": "cityflow_1x1/cityflow_1x1.sumocfg",
  "roadnetFile": "cityflow_1x1/cityflow_1x1.net.xml",
  "flowFile": "cityflow_1x1/cityflow_1x1.rou.xml",
  "convertroadnetFile": "cityflow_1x1/cityflow_1x1_roadnet.json",
  "convertflowFile": "cityflow_1x1/cityflow_1x1_flow.json",
  "no_warning": true,
  "name": "debug",
  "yellow_length": 5,
  "gui": false
}
```
- interval: time of each simulation step (in seconds).
- seed: random seed.
- dir: root directory, all file path will be relative to this directory.
- combined_file: path for SUMO configuration file.
- roadnetFile: path for SUMO roadnet file.
- flowFile: path for SUMO flow file.
- convertroadnetFile: path for SUMO roadnet file.
- convertflowFile: path for SUMO flow file.
- **no_warning:** 
- **name:** 
- yellow_length: default yellow time. The default is set to 5 s.
- gui: whether to use SUMO-GUI tools.

## Params of TSC Process and Agents
Parameters about training proccess and agents
#### base.yml

common parameters of the framework

```
task:
  description: Use RL methods to optimize traffic signal control problem
  task_name: tsc
world:
# necessary and distinctive parameters for simulators
  interval: 1.0
  seed: 0
  dir: data/

  saveReplay: False
  report_log_mode: normal # cbengine
  report_log_rate: 10

  no_warning: True
  gui: False

  rlTrafficLight: True

trainer:
  thread: 4
  ngpu: -1
  learning_start: 5000
  buffer_size: 5000
  steps: 3600
  test_steps: 3600
  yellow_length: 5
  action_interval: 10
  episodes: 200
  update_model_rate: 1
  update_target_rate: 10
  test_when_train: True

model:
  name: "non-rl"
  train_model: False
  test_model: True
  load_model: False
  graphic: False
  vehicle_max: 1
  learning_rate: 0.001
  batch_size: 64
  gamma: 0.95
  epsilon: 0.5
  epsilon_decay: 0.99
  epsilon_min: 0.05
  grad_clip: 5.0

  one_hot: False
  phase: False

logger:
  root_dir: "data/output_data/"
  log_dir: "logger/"
  replay_dir: "replay/"
  model_dir: "model/"
  data_dir: "dataset/"
  save_model: True
  save_rate: 200
  attention: False
```

- Task
    - description: description of task
    - task_name: task name
- World
    - interval: time of each simulation step (in seconds).
    - seed: random seed.
    - dir: root directory, all file path will be relative to this directory.
    - saveReplay: whether to save simulation for replay. Used for CityFlow.
    - **report_log_mode:** 
    - report_log_rate: rate of report log.
    - **no_warning:** 
    - gui: whether use SUMO-GUI tools
    - rlTrafficLight: whether to enable traffic light control through python API. If set to false, default traffic light plan defined in roadnetFile will be used.
- Trainer
    - thread: number of threads.
    - ngpu: number of gpu to be used.
    - learning_start: how many steps start to update model.
    - buffer_size: size of memory buffer.
    - steps: number of training steps in one episode.
    - test_steps: number of test steps in one episode.
    - yellow_length: yellow time.
    - action_interval: time interval to perform actions.
    - episodes: number of one complete process.
    - update_model_rate: rate of updating model.
    - update_target_rate: rate of updating target model.
    - test_when_train: whether to test model after each episode.
- Model
  - name: type of model, support non-rl and rl models.
  - train_model: whether to train model, False for non-rl models, True for rl models.
  - test_model: whether to test model.
  - load_model: whether to load pretrained model.
  - graphic: whether to use graph to train model. Now it support DGL.
  - **vehicle_max:** 
  - learning_rate: the step size at each iteration while moving toward a minimum of a loss function.
  - batch_size: the number of samples utilized in one iteration.
  - gamma: discount factor.
  - epsilon: probability of random actions.
  - epsilon_decay: decay of  epsilon on the next training episode.
  - epsilon_min: minimum value of epsilon.
  - grad_clip: clip gradients according to this parameter.
  - one_hot: whether to encode phase.
  - phase: whether to add phase into model's feature.
- Logger
  - root_dir: root directory, all file path of output data will be relative to this directory.
  - log_dir: root directory of logger.
  - replay_dir: root directory of replay.
  - model_dir: root directory of model.
  - data_dir: root directory of dataset.
  - save_model: whether to save model's parameters.
  - save_rate: rate of saving related parameters.
  - **attention:** 



**Note:** The value of common parameters will be overwritten if it appears in a model file when loading parameters in training process.

#### FixedTime.yml

```
includes:
  - configs/tsc/base.yml

model:
  name: fixedtime
  t_fixed: 10

trainer:
  episodes: 1
  buffer_size: 0
  action_interval: 10
  learning_rate: 0
  learning_start: 0
  update_model_rate: 0
  update_target_rate: 0

logger:
  save_rate: 1
  train_model: False
  test_model: True
  load_model: False
```

#### MaxPressure.yml

```
includes:
  - configs/tsc/base.yml

model:
  name: maxpressure
  t_min: 10

trainer:
  buffer_size: 0
  action_interval: 10
  learning_rate: 0
  learning_start: 0
  update_model_rate: 0
  update_target_rate: 0

logger:
  save_rate: 0
  train_model: False
  test_model: True
  load_model: False
```

+ **t_min:** 

#### SOTL.yml

```
includes:
  - configs/tsc/base.yml

model:
  name: sotl
  min_green_vehicle: 3
  max_red_vehicle: 6
  t_min: 5

trainer:
  episodes: 1
  buffer_size: 0
  learning_rate: 0
  learning_start: 0
  update_model_rate: 0
  update_target_rate: 0

logger:
  save_rate: 0
  train_model: False
  test_model: True
  load_model: False
```

#### IDQN.yml

```
includes:
  - configs/tsc/base.yml

model:
  name: dqn
  train_model: True
```

#### MAPG.yml
```
includes:
  - configs/tsc/base.yml

model:
  name: magd
  train_model: True
  local_q_learn: False
  tau: 0.01
  learning_rate: 0.01
  batch_size: 256
  grad_clip: 0.5
  epsilon: 0.5
  epsilon_decay: 0.998
  epsilon_min: 0.05

trainer:
  episodes: 2000
  update_model_rate: 30
  update_target_rate: 30
  action_interval: 20
```

#### IPPO.yml
```
includes:
  - configs/tsc/base.yml

model:
  name: ppo
  graphic: False
  vehicle_max: 1
  learning_rate: 0.001
  update_interval: 1024
  batch_size: 64
  gamma: 0.95
  epsilon: 0.1
  epsilon_decay: 0.995
  epsilon_min: 0.01
  grad_clip: 5.0
  NEIGHBOR_NUM: 4
  NEIGHBOR_EDGE_NUM: 4

trainer:
  learning_start: 1000
  buffer_size: 1024
```

#### PressLight.yml
```
includes:
  - configs/tsc/base.yml

model:
  name: presslight
  train_model: True
  d_dense: 20
  epsilon: 0.1
  epsilon_decay: 0.995
  epsilon_min: 0.01
  one_hot: True
  phase: True

trainer:
  learning_start: 1000
```

#### CoLight.yml
```
includes:
  - configs/tsc/base.yml

model:
  name: colight
  graphic: True
  vehicle_max: 1
  learning_rate: 0.001
  batch_size: 64
  gamma: 0.95
  epsilon: 0.8
  epsilon_decay: 0.9995
  epsilon_min: 0.01
  grad_clip: 5.0
  NEIGHBOR_NUM: 4
  NEIGHBOR_EDGE_NUM: 4
  N_LAYERS: 1
  INPUT_DIM: [128, 128]
  OUTPUT_DIM: [128, 128]
  NODE_EMB_DIM: [128, 128]
  NUM_HEADS: [5, 5]
  NODE_LAYER_DIMS_EACH_HEAD: [16, 16]
  OUTPUT_LAYERS: []
  one_hot: True
  phase: False

trainer:
  learning_start: 1000
  train_model: True
```

#### FRAP.yml
```
includes:
  - configs/agents/tsc/base.yml

model:
  name: frap
  n_layers: 2
  rotation: true
  conflict_matrix: true
  merge: multiply
  d_dense: 20
  learning_rate: 0.001
  batch_size: 64
  gamma: 0.95
  epsilon: 0.1
  epsilon_decay: 0.995
  epsilon_min: 0.01
  grad_clip: 5.0
  demand_shape: 1
  one_hot: False
  phase: True

trainer: 
  learning_start: 1000
  train_model: True

world:
  phases: ['NT_ST','WT_ET','NL_SL','WL_EL','NL_NT','SL_ST','WL_WT','EL_ET']
  
  list_lane_order: ['ET','EL','ST','SL','WT','WL','NT','NL']

  phase_expansion: {
    1: [0, 0, 1, 0, 0, 0, 1, 0],
    2: [1, 0, 0, 0, 1, 0, 0, 0],
    3: [0, 0, 0, 1, 0, 0, 0, 1],
    4: [0, 1, 0, 0, 0, 1, 0, 0],
    5: [0, 0, 0, 0, 0, 0, 1, 1],
    6: [0, 0, 1, 1, 0, 0, 0, 0],
    7: [0, 0, 0, 0, 1, 1, 0, 0],
    8: [1, 1, 0, 0, 0, 0, 0, 0]
  }

  phase_expansion_4_lane: {1: [0,0,1,1],2: [1,1,0,0]}

  signal_config: {
    grid4x4: {
      phase_pairs: [[1, 7], [2, 8], [1, 2], [7, 8], [4, 10], [5, 11], [10, 11], [4, 5]],
      valid_acts: null,
      cf_order: {'N': 0,'E': 1,'S': 2, 'W': 3},
      sumo_order: {'N': 2,'E': 3,'S': 0, 'W': 1}
    },
    hz1x1: {
      # phases: ['ET_WT','NT_ST','EL_WL','NL_SL','WL_WT','EL_ET','SL_ST','NL_NT']
      phase_pairs: [[2, 6], [0, 4], [3, 7], [1, 5], [6, 7], [2, 3], [4, 5], [0, 1]],
      # phases: ['NT_ST','WT_ET','NL_SL','WL_EL','NL_NT','SL_ST','WL_WT','EL_ET']
      # phase_pairs: [[1, 5], [3, 7], [0, 4], [2, 6], [0, 1], [4, 5], [6, 7], [2, 3]],
      valid_acts: null,
      cf_order: {'N': 0,'E': 1,'S': 2, 'W': 3},
      sumo_order: {'N': 2,'E': 3,'S': 0, 'W': 1}
    },
    hz4x4: {
      # phases: ['NT_ST','WT_ET','NL_SL','WL_EL','NL_NT','SL_ST','WL_WT','EL_ET']
      phase_pairs: [[4, 10], [1, 7], [3, 9], [0, 6], [9, 10], [3, 4], [6, 7], [0, 1]],
      valid_acts: null,
      cf_order: {'N': ,'E': ,'S': , 'W': },
      sumo_order: {'N': ,'E': ,'S': , 'W': }
    },
    cologne1: {
      phase_pairs: [[1, 5], [0, 4], [3, 7], [2, 6]],
      valid_acts: null,
      cf_order: {'N': 3,'E': 0,'S': 1, 'W': 2},
      sumo_order: {'N': 1,'E': 2,'S': 3, 'W': 0}
    },
    cologne3: {
      phase_pairs: [[1, 7], [2, 8], [1, 2], [7, 8], [4, 10], [5, 11], [10, 11], [4, 5], [9, 11]],
      valid_acts: {
        GS_cluster_2415878664_254486231_359566_359576: {4: 0, 5: 1, 0: 2, 1: 3},
        360086: {4: 0, 5: 1, 0: 2, 1: 3},
        360082: {4: 0, 5: 1, 1: 2}
      },
      cf_order: {
        '360082': {'N': -1,'E': 0,'S': 1, 'W': 2},
        '360086': {'N': 3,'E': 0,'S': 1, 'W': 2},
        'cluster_2415878664_254486231_359566_359576': {'N': 3,'E': 0,'S': 1, 'W': 2}
        },
      sumo_order: {
        '360082': {'N': -1,'E': 1,'S': 2, 'W': 0},
        '360086': {'N': 1,'E': 2,'S': 3, 'W': 0},
        'cluster_2415878664_254486231_359566_359576': {'N': 1,'E': 2,'S': 3, 'W': 0}
      }
    }
  }
```

#### MPLight.yml
```
includes:
  - configs/tsc/base.yml

model:
  name: mplight
  train_model: True
  n_layers: 2
  rotation: true
  conflict_matrix: true
  merge: multiply
  d_dense: 20
  learning_rate: 0.001
  batch_size: 32
  gamma: 0.99
  eps_start: 1.0
  eps_end: 0.0
  eps_decay: 220
  target_update: 500
  demand_shape: 1
  phase: True

trainer: 
  learning_start: -1
  buffer_size: 10000

world:
  phases: ['NT_ST','WT_ET','NL_SL','WL_EL','NL_NT','SL_ST','WL_WT','EL_ET']
  
  list_lane_order: ['ET','EL','ST','SL','WT','WL','NT','NL']

  phase_expansion: {
    1: [0, 0, 1, 0, 0, 0, 1, 0],
    2: [1, 0, 0, 0, 1, 0, 0, 0],
    3: [0, 0, 0, 1, 0, 0, 0, 1],
    4: [0, 1, 0, 0, 0, 1, 0, 0],
    5: [0, 0, 0, 0, 0, 0, 1, 1],
    6: [0, 0, 1, 1, 0, 0, 0, 0],
    7: [0, 0, 0, 0, 1, 1, 0, 0],
    8: [1, 1, 0, 0, 0, 0, 0, 0]
  }

  phase_expansion_4_lane: {1: [0,0,1,1],2: [1,1,0,0]}

  signal_config: {
    grid4x4: {
      phase_pairs: [[1, 7], [2, 8], [1, 2], [7, 8], [4, 10], [5, 11], [10, 11], [4, 5]],
      valid_acts: null
    },
    cityflow1x1: {
      # phases: ['ET_WT','NT_ST','EL_WL','NL_SL','WL_WT','EL_ET','SL_ST','NL_NT']
      # phase_pairs: [[3, 7], [1, 5], [2, 6], [0, 4], [6, 7], [2, 3], [4, 5], [0, 1]],
      # phases: ['NT_ST','WT_ET','NL_SL','WL_EL','NL_NT','SL_ST','WL_WT','EL_ET']
      phase_pairs: [[1, 5], [3, 7], [0, 4], [2, 6], [0, 1], [4, 5], [6, 7], [2, 3]],
      valid_acts: null
    },
    cityflow4x4: {
      # phases: ['NT_ST','WT_ET','NL_SL','WL_EL','NL_NT','SL_ST','WL_WT','EL_ET']
      phase_pairs: [[4, 10], [1, 7], [3, 9], [0, 6], [9, 10], [3, 4], [6, 7], [0, 1]],
      valid_acts: null
    },
    cologne1: {
      phase_pairs: [[1, 7], [2, 8], [4, 10], [5, 11]],
      valid_acts: null
    },
    cologne3: {
      phase_pairs: [[1, 7], [2, 8], [1, 2], [7, 8], [4, 10], [5, 11], [10, 11], [4, 5], [9, 11]],
      valid_acts: {
        GS_cluster_2415878664_254486231_359566_359576: {4: 0, 5: 1, 0: 2, 1: 3},
        360086: {4: 0, 5: 1, 0: 2, 1: 3},
        360082: {4: 0, 5: 1, 1: 2}
      }
    }
  }
```




