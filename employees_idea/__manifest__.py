{
	'name' : 'Employee Ideas Application',
	'description': 'This module allow employees in the company to raise and create ideas and after approval of ideas other employees in departments can vote for that idea',
	'author': 'Faiz Abdussalam',
	'depends': ['base','hr'],
	'application': True,
	'data': ['views/employee_ideas_menu.xml',
	'views/ideas_view.xml',
	'views/ideas_types_view.xml',
	'views/employee_vote_wizard.xml',
	],
}