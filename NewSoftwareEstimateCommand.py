import sublime
import sublime_plugin

class NewSoftwareEstimateCommand(sublime_plugin.WindowCommand):
	def run(self):
		print("Starting New Software Estimtae command...")

		self.projectName = ""

		#
		# Ask for project name
		#
		self.window.show_input_panel("Project name", "", self.projectNameOnDone, None, None)

	def projectNameOnDone(self, input):
		print("User entered %s for project name" % (input,))
		self.projectName = input

		buffer = self.window.new_file()
		buffer.run_command("new_software_estimate_text", {
			"projectName": self.projectName
		})


class NewSoftwareEstimateTextCommand(sublime_plugin.TextCommand):
	def run(self, edit, projectName):
		template = """# %s Estimate

## Description

Put your project description here.

## Objectives and Observations

* Objective 1
* Observation
	- Stuff

## Tasks

|Task                                            |Rate    |Hours  |Amount    |
|:----------------------------------------------:|:------:|:-----:|:--------:|
|Perform task for objective 1                    |$1.00   |1      |$1.00     |
|                                                |        |       |          |
|                                                |        |       |Total     |
|                                                |        |       |$1.00     |

## Notes and Terms

The above tasks and total are an *estimate* based on initial analysis and observations. Through the course of work more issues, observations, or tasks may be revealed and could increase or decrease the amount of time required to complete the job. I will communicate any issues and potential increase in time and total cost as they come up. If you wish to discontinue work payment for services rendered up to the point of stopping will be invoiced and due.

Once work is completed, or services are terminated, an invoice of work and services completed will be sent. Payment is due 30 days from issue of invoice.

Thanks for your business!

Your name here

Email address@address.com
Phone number
""" % (projectName,)

		self.view.insert(edit, 0, template)
