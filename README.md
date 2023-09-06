# MagicKit - IT Workstation Automation

MagicKit is a command-line tool (CLI) created in Python that aims to automate the process of setting up new workstations in the IT department. The main goal of the project is to streamline the installation of essential packages on new computers and expedite deployment.

## Features

1. **Automatic Package Installation**: MagicKit installs a basic set of packages using Chocolatey (choco).

2. **Domain Operations**: Features have been added to join computers to a domain and change computer names.

3. **Automatic Reporting**: MagicKit allows for automatic reporting of information about newly created computers to a database.

4. **Network Card Management**: The tool offers quick access to manipulating network cards on new computers.

5. **MS Office Module**: An MS Office module has been added, enabling the installation of MS Office software on a computer and managing user accounts using a built-in password manager.

## Quick Start

### 1. Clone the Repository

Clone the MagicKit repository to your computer using the Git command:

```shell
git clone https://github.com/twój-username/MagicKit.git
```

### 2. Install Required Libraries

Navigate to the MagicKit directory:

```shell
cd MagicKit
```

Then, install the required libraries using pip:

```shell
pip install -r requirements.txt
```

### 3. Run MagicKit

Now, you can run MagicKit to initiate the process of automatically creating an IT workstation:

```shell
python main.py
```

### 4. Create an Executable File (Optional)

We recommend converting MagicKit into an executable file (exe) using available Python libraries. You can then create a portable "toolbox" on a removable drive containing the ready-to-use MagicKit.

This allows you to have access to MagicKit in the form of an executable file on any computer where you need to automate IT workstation setup.
