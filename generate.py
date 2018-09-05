from github import Github

#Enter Github login information
username = ""
password = ""

#Enter repository information
repository = "" # Example "smartdevicelink/sdl_core"
project_name="" # Example "5.0.0"

completed_list_names = ["Completed Features", "Completed Bug Fixes"] # Project Column names that you want to include in the release notes
markdown_titles = ["Implemented Proposals", "Bug Fixes"] # Markdown titles you want to use in place of the project column names. These correspond to the completed_list_names.
split_by_labels = True

g = Github(username, password)
repo = g.get_repo(repository)
projects = repo.get_projects()

for project in projects:
	if(project.name == project_name):
		print(project.name)
		markdown_str = ""
		columns = project.get_columns()
		count = 0
		for name in completed_list_names: 
			for column in columns:
				if column.name == name:
					markdown_str += "## " + markdown_titles[count] + "\n\n"
					print(markdown_titles[count])
					cards = column.get_cards()
					label_dict = {"no_label": ""}
					for card in cards: 
						issue = card.get_content()
						print(issue.title)
						print(issue.html_url)
						labels = issue.labels
						if len(labels) > 0 and split_by_labels == True:
							key = str(labels[0].name)
							if key in label_dict:								
								label_dict[str(labels[0].name)] += "- [" + issue.title + "]" + "(" + issue.html_url + ")\n\n"
							else: 
								label_dict[str(labels[0].name)] = "- [" + issue.title + "]" + "(" + issue.html_url + ")\n\n"
						else:
							label_dict["no_label"] += "- [" + issue.title + "]" + "(" + issue.html_url + ")\n\n"
					for key in label_dict:
						markdown_str += "## " + key + "\n\n"
						markdown_str += label_dict[key]
					count = count + 1
		file_name = project_name + "_release_notes.md"
		print("Writing notes to: " + file_name)
		file = open(file_name, "w")
		file.write(markdown_str.encode('ascii', 'ignore'))
