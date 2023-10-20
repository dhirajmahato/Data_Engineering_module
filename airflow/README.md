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
- `airflow db check` will check the status of your database (eg. connected, not connected, etc).
- `airflow db upgrade` will upgrade the information and metadata of your database. Perform upgrade regularly to prevent any dependency issue.
- `airflow db shell` will give you access to the database itself. Please proceed with care.


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
- `airflow dags list` will list our a list of DAGs that you currently have running.

Testing a DAG 
- `airflow dags test <DAG_ID> <EXECUTION_TIME>` will perform a single test on your task. No changes will occur on the database.

- `airflow dags delete <DAG_ID>` will delete all the data in DB related to the task.
- `airflow dags show <DAG_ID>` will show the structure and dependencies of a DAG.

Showing a DAG structure and dependencies (image from airflow.org)
- `airflow dags show <DAG_ID> --save <FILE_NAME.png>` will save the above image to a local file. There are many extensions you can use, including png, jpg , and pdf


### 8. Tasks

- `airflow tasks list <DAG_ID>` will list down all tasks related to a given DAG.
  
List of tasks in a DAG (image by author)
- `airflow tasks test <DAG_ID> <TASK_ID> <EXECUTION_TIME>` will perform test on a specific task in a DAG.


###  Web Authentication on Web UI
By default, Airflow requires users to specify a password prior to login.

Since Airflow 2.0, the default UI is the Flask App Builder RBAC (Role-Based Access Control). 

A webserver_config.py configuration file is automatically generated and can be used to configure the Airflow to support authentication methods like OAuth, OpenID, LDAP, REMOTE_USER.

src: https://airflow.apache.org/docs/apache-airflow/stable/security/webserver.html#disable-deployment-exposure-warning

  1. **RBAC**: It assigns users to roles that determine their access permissions within the Airflow web UI.
      - Roles: Common roles include Admin, User, Viewer, and Public.
  2. **LDAP** (Lightweight Directory Access Protocol) Authentication:
  3. **OAuth** (Open Authorization) Authentication: It allows users to log in using their existing credentials from a trusted third-party identity provider (e.g., Google, Microsoft, or GitHub).


To deactivate the authentication and allow users to be identified as Anonymous, the following entry in $AIRFLOW_HOME/webserver_config.py needs to be set with the desired role that the Anonymous user will have by default:

`AUTH_ROLE_PUBLIC = 'Admin'`

If you are using the airflow standalone command then you will get the user and password in the terminal itself

#### Creating Users
There is no default username and password created if you are just using python wheel.

To check list of users
```
  airflow users list
  airflow users show admin
  airflow users delete admin
  airflow users reset-password admin
```

You can use the following CLI commands to create an account:
```
  airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
  or
  airflow users create -u <username> -p <password> -r <role> -e <email>
```

COMMAND
- add-role  : Add role to a user
- create    : Create a user
- delete    : Delete a user
- export    : Export all users
- import    : Import users
- list      : List users
- remove-role :     Remove role from a user

