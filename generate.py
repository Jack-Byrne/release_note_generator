from github import Github

#Enter Github personal access token information
# https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
# Add read permissions for token
access_token = ""

#Enter repository information
repository = "smartdevicelink/rpc_spec" # Example "smartdevicelink/sdl_core"
project_name="7.0.0" # Example "5.0.0"

completed_list_names = ["Done"] # Project Column names that you want to include in the release notes
markdown_titles = ["Done"] # Markdown titles you want to use in place of the project column names. These correspond to the completed_list_names.
split_by_labels = False

g = Github(access_token)
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
				print("name " + name)
				print(column.name)
				if column.name == name:
					print("colum name")
					markdown_str += "## " + markdown_titles[count] + "\n\n"
					print(markdown_titles[count])
					cards = column.get_cards()
					label_dict = {"no_label": ""}
					for card in cards: 
						issue = card.get_content()
						if issue == None:
							continue
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
		file.write(markdown_str)
