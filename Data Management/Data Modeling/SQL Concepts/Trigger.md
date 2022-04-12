# Trigger
### Overview
+ similar to [[Procedures and Functions]] but execute on event
	+ on delete/insert/update
+ allow complex check constraints and active behaviour
	+ replication
	+ auto deletion
	+ auditing
+ very powerful but complex
	+ need to be careful
	+ lots of implicite dependencies
	+ trigger may trigger other triggers
		+ infinite loop

	
### Trigger Template
![[Pasted image 20220412154145.png]]

[[SQL Concepts]]