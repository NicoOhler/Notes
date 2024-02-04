### Overview
+ assign a relevance score r to a new item based on specific user
	+ decide how relevant an unknown item $I_{new}$ is to user $U_0$
+ $r=f(U,I,U_0,I_{new})$
	+ set of users U
	+ set of items I
+ unlike [[Information Retrieval]] recommendation is proactive
	+ no explicite query
	+ results often based on implicitly collected data

### Recommender System Types/Paradigms
+ [[Collaborative Filtering]]
	+ based on user interactions with items in a system
	+ interactions such as
		+ user ratings
		+ clicks
		+ purchase
+ content based
	+ based on description of users and items in terms of content
	+ e.g. new fantasy novel for fantasy fan based on
		+ metadata
			+ keywords
			+ genre
		+ content analysis
	+ similarity between user interest and content-wise description of items
+ knowledge based
	+ based on explicitly modelled constraints on items
	+ simillar to basic filtering
	+ e.g. all all-inclusive hotels in Egypt with beach access within a certain price range...
+ hybrid of different recommendation paradigms

### Challenges
+ ![](../../../../z_images/Pasted%20image%2020220502175423.png)
+ ![](../../../../z_images/Pasted%20image%2020220502180102.png)
+ ![](../../../../z_images/Pasted%20image%2020220502180245.png)