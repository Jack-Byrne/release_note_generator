# Release Note Generator

Generates a markdown document from a repository project page

## Setup

### Install PyGithub package
Currently the Github api "Project" feature is under development. Please install this branch of PyGithub until the feature is completed
```
pip install git+https://github.com/bbi-yggy/PyGithub@dev.project-support
```

### Set Script Parameters
Open a text editor and set some parameters. These steps will show how a release note document can be created from this repository's project: [Example](https://github.com/JackLivio/release_note_generator/projects/1)

#### Github Login Info
> username = "JackLivio"
> password = "password123"

#### Repository & Project Information

> repository = "JackLivio/release_note_generator" 
> project_name = "Example"

The following should be the names of columns you want to pull cards from. This is an array of strings, in case you want to pull cards from multiple columns. ie ( "Implemented Proposals" & "Bug Fixes")

> completed_list_names = ["Completed Issues"]

#### Markdown Information
The array "markdown_titles" is the title you like to give different sections of the release notes. This array corresponds directly to the column names provided in "completed_list_names". For each column in the project, there should be a markdown title to go with it. 
> markdown_titles = ["Resolved Issues"]

#### Run the script
> python generate.py


#### Output

```
## Resolved Issues

- [Create script that generates release notes](https://github.com/JackLivio/release_note_generator/issues/1)

```
