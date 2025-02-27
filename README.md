# Virtual Environment and Django Setup Guide

## Step 1: Installing virtualenv
To install `virtualenv`, run the following command:
```sh
pip install virtualenv
```

## Step 2: Test your Installation
Check if `virtualenv` is installed correctly by running:
```sh
virtualenv --version
```

## Step 3: Naming the Virtual Environment
Create a virtual environment named `my_env`:
```sh
virtualenv my_env
```

## Step 4: Activating the Virtual Environment
Activate the virtual environment using:
```sh
source ./my_env/Scripts/activate
```
**Note:** If the `source` command does not work, try running:
```sh
./my_env/Scripts/activate
```

## Step 5: Deactivating the Virtual Environment
To deactivate the virtual environment, use:
```sh
deactivate
```

---

# Checking and Installing Django

## Step 1: Check if Django is Installed
To verify if Django is installed, check its version:
```sh
python -m django --version
```

## Step 2: Installing Django
If Django is not installed, install it using:
```sh
pip install django
```

---

# Creating a Django Project and Application

## Step 1: Create a Django Project
Run the following command to create a new Django project:
```sh
django-admin startproject project_name
```

## Step 2: Change Directory
Navigate to the project directory:
```sh
cd project_name
```

## Step 3: Create a Django Application
To create an application within the project, use:
```sh
django-admin startapp app_name
```

## Step 4: Run the Project on Local Server
Start the development server with:
```sh
py manage.py runserver
```

