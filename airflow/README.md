## Airflow
Apache Airflow is an open-source platform for programmatically authoring, scheduling, and monitoring workflows. It's commonly used for orchestrating complex data workflows, but it can be used for a wide range of automation and scheduling tasks. 

use a virtual environment to manage your Python dependencies.
### 1. Installation
```
  pip install apache-airflow
```
### 2. Initialize the Airflow Database:
Airflow uses a database to store metadata and state information about your workflows. 
```
  airflow db init
```
### 3. Airflow Configuration:
configuration file for Airflow is located in the airflow.cfg file. You can find it in the $AIRFLOW_HOME directory. By default, $AIRFLOW_HOME is ~/airflow. You can configure various settings in this file, like the database connection and executor type.

### 4. Command to start airflow server and Schedular
The web server is the main user interface for Airflow, and the scheduler is responsible for scheduling and executing your workflows.
```
  airflow webserver
  airflow scheduler

```

```
  airflow standalone
```
Login with username: admin  password: Ktx5QHyaacQhaeuK
