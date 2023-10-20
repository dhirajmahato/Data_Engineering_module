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
### 5. Access the Web UI:
By default, the Airflow web server will run on http://localhost:8080.

### 6. First DAG (Directed Acyclic Graph):

A DAG is the core concept in Airflow. It defines the workflow you want to automate. You can create a Python script for your DAG, typically stored in the dags/ directory within your $AIRFLOW_HOME.

Here's a simple example of a DAG that prints "Hello, Airflow!":
```
  from airflow import DAG
  from airflow.operators.python import PythonOperator
  from datetime import datetime
  
  def say_hello():
      print("Hello, Airflow!")
  
  default_args = {
      'owner': 'your_name',
      'start_date': datetime(2023, 10, 20)
  }
  
  dag = DAG('hello_airflow', default_args=default_args, schedule_interval=None)
  
  task = PythonOperator(
      task_id='print_hello',
      python_callable=say_hello,
      dag=dag
  )
```
save this script in the dags/ directory.

### 7. Trigger Your DAG:

You can trigger your DAG from the web UI or by using the command line. To run it from the command line, use the airflow dags trigger command:
```
  airflow dags trigger hello_airflow
```
***
## Web Authentication
By default, Airflow requires users to specify a password prior to login.

Since Airflow 2.0, the default UI is the Flask App Builder RBAC. A webserver_config.py configuration file is automatically generated and can be used to configure the Airflow to support authentication methods like OAuth, OpenID, LDAP, REMOTE_USER.

src: https://airflow.apache.org/docs/apache-airflow/stable/security/webserver.html#disable-deployment-exposure-warning

To deactivate the authentication and allow users to be identified as Anonymous, the following entry in $AIRFLOW_HOME/webserver_config.py needs to be set with the desired role that the Anonymous user will have by default:

`AUTH_ROLE_PUBLIC = 'Admin'`

If you are using the airflow standalone command then you will get the user and password in the terminal itself

## Creating Users
There is no default username and password created if you are just using python wheel.

To check list of users
```
  airflow users list
```

You can use the following CLI commands to create an account:
```
  airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
```

COMMAND
- add-role   Add role to a user
- create     Create a user
- delete     Delete a user
- export     Export all users
- import     Import users
- list       List users
- remove-role     Remove role from a user

